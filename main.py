import subprocess
import json
import os
import base64

IMAGE_REF = "ghcr.io/taha2samy/wolfi-openssl-fips:latest"
REPO = IMAGE_REF.split(':')[0]
OUTPUT_DIR = "./extracted_metadata"

if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

def run_cmd(command, is_binary=False):
    try:
        res = subprocess.run(command, capture_output=True, check=True)
        return res.stdout if is_binary else res.stdout.decode('utf-8').strip()
    except: return None

def identify_content(raw_data):
    try:
        data = json.loads(raw_data.decode('utf-8'))
        p_type = data.get("predicateType")
        if not p_type and "payload" in data:
            try:
                p_load = json.loads(base64.b64decode(data["payload"]).decode('utf-8'))
                p_type = p_load.get("predicateType")
            except: pass
        
        if p_type:
            if "spdx" in p_type or "sbom" in p_type or "cyclonedx" in p_type: return "SBOM", p_type, data
            if "provenance" in p_type: return "PROVENANCE", p_type, data
        
        # فحص الكلمات المفتاحية لو النوع مش صريح
        str_body = str(data).lower()
        if "spdx" in str_body or "cyclonedx" in str_body: return "SBOM", "detected_via_body", data
        if "provenance" in str_body: return "PROVENANCE", "detected_via_body", data
        
        return "UNKNOWN", "unknown", data
    except: return "BINARY", "binary", None

def main():
    print(f"\n" + "="*60)
    print(f"🔍 STEP 1: Fetching Root Index for {IMAGE_REF}")
    manifest_raw = run_cmd(["crane", "manifest", IMAGE_REF])
    if not manifest_raw: return

    index = json.loads(manifest_raw)
    print(f"✅ Root Index Loaded. Found {len(index.get('manifests', []))} total manifests in Index.")

    # فصل الصور عن الملحقات
    images = [m for m in index['manifests'] if 'platform' in m and m['platform'].get('architecture') != 'unknown']
    attestations = [m for m in index['manifests'] if m not in images]

    print(f"👉 Detected Architectures: {[m['platform']['architecture'] for m in images]}")
    print(f"👉 Detected Internal Attestation Manifests: {len(attestations)}")

    tree_map = {"platforms": []}

    for img in images:
        arch = img['platform']['architecture']
        img_sha = img['digest']
        print(f"\n" + "-"*60)
        print(f"🏗️  ANALYZING ARCHITECTURE: [{arch.upper()}]")
        print(f"   Image Digest: {img_sha}")

        arch_node = {"architecture": arch, "image_digest": img_sha, "files": []}

        # 1. البحث عن الروابط الداخلية (Bake)
        print(f"   🔎 Looking for Internal Bake Metadata (via Annotations)...")
        for m in attestations:
            ref_digest = m.get('annotations', {}).get('vnd.docker.reference.digest')
            if ref_digest == img_sha:
                meta_sha = m['digest']
                print(f"   📍 Found Linked Bake Manifest: {meta_sha[:15]}...")
                
                # فتح الـ Manifest بتاع الـ Attestation
                meta_manifest = json.loads(run_cmd(["crane", "manifest", f"{REPO}@{meta_sha}"]))
                layers = meta_manifest.get('layers', [])
                print(f"      📦 This manifest has {len(layers)} Layers (Blobs).")
                
                for i, layer in enumerate(layers):
                    l_sha = layer['digest']
                    print(f"      🔹 Layer {i+1}: Downloading Blob {l_sha[:15]}...")
                    
                    raw_blob = run_cmd(["crane", "blob", f"{REPO}@{l_sha}"], is_binary=True)
                    label, p_type, content = identify_content(raw_blob)
                    
                    fname = f"{arch}_bake_{label.lower()}_{l_sha[7:15]}.json"
                    with open(os.path.join(OUTPUT_DIR, fname), "w") as f: json.dump(content, f, indent=2)
                    
                    print(f"         ✨ IDENTIFIED AS: {label} ({p_type})")
                    print(f"         💾 SAVED TO: {fname}")
                    arch_node["files"].append({"type": label, "source": "bake", "sha": l_sha, "file": fname})

        # 2. البحث عن الروابط الخارجية (GitHub Referrers)
        print(f"   🔎 Looking for External Referrers (via Registry API)...")
        referrers_raw = run_cmd(["crane", "referrers", f"{REPO}@{img_sha}"])
        if referrers_raw:
            refs = json.loads(referrers_raw).get('manifests', [])
            print(f"      📍 Found {len(refs)} external referrers.")
            for r in refs:
                r_sha = r['digest']
                print(f"      🔹 Downloading Referrer Blob {r_sha[:15]}...")
                raw_blob = run_cmd(["crane", "blob", f"{REPO}@{r_sha}"], is_binary=True)
                label, p_type, content = identify_content(raw_blob)
                
                fname = f"{arch}_github_{label.lower()}_{r_sha[7:15]}.json"
                with open(os.path.join(OUTPUT_DIR, fname), "w") as f: json.dump(content, f, indent=2)
                
                print(f"         ✨ IDENTIFIED AS: {label} ({p_type})")
                print(f"         💾 SAVED TO: {fname}")
                arch_node["files"].append({"type": label, "source": "github", "sha": r_sha, "file": fname})

        tree_map["platforms"].append(arch_node)

    with open("supply_chain_map.json", "w") as f: json.dump(tree_map, f, indent=2)
    print("\n" + "="*60)
    print("🚀 FINISHED: Map saved to supply_chain_map.json")

if __name__ == "__main__": main()