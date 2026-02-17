import subprocess
import json
import os
import base64

REPO = "ghcr.io/taha2samy/wolfi-openssl-fips"
OUTPUT_DIR = "./repo_audit"
if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

def run_cmd(command, is_binary=False):
    try:
        res = subprocess.run(command, capture_output=True, check=True)
        return res.stdout if is_binary else res.stdout.decode('utf-8').strip()
    except: return None

def identify_and_save(raw_data, tag_name):
    try:
        data = json.loads(raw_data.decode('utf-8'))
        content = data
        p_type = data.get("predicateType", "unknown")
        
        if "payload" in data:
            try:
                p_load = json.loads(base64.b64decode(data["payload"]).decode('utf-8'))
                p_type = p_load.get("predicateType", "unknown")
                content = p_load
            except: pass

        label = "unknown"
        if any(x in str(p_type).lower() or x in str(data).lower() for x in ["spdx", "sbom", "cyclonedx"]):
            label = "sbom"
        elif "provenance" in str(p_type).lower() or "provenance" in str(data).lower():
            label = "provenance"

        fname = f"{tag_name}_{label}.json".replace(":", "-")
        with open(os.path.join(OUTPUT_DIR, fname), "w") as f:
            json.dump(content, f, indent=2)
        return label, p_type
    except: return None, None

def audit():
    print(f"🛰️  Fetching ALL tags for: {REPO}")
    tags_raw = run_cmd(["crane", "ls", REPO])
    if not tags_raw:
        print("❌ Could not list tags. Are you logged in?")
        return

    tags = tags_raw.split('\n')
    print(f"📊 Found {len(tags)} total tags. Scanning for metadata...")

    for tag in tags:
        if tag.startswith("sha256-") and (tag.endswith(".att") or tag.endswith(".sig")):
            print(f"🔎 Inspecting Tag: {tag[:30]}...")
            
            manifest_raw = run_cmd(["crane", "manifest", f"{REPO}:{tag}"])
            if not manifest_raw: continue
            
            manifest = json.loads(manifest_raw)
            layers = manifest.get('layers', [])
            
            for i, layer in enumerate(layers):
                blob = run_cmd(["crane", "blob", f"{REPO}@{layer['digest']}"], is_binary=True)
                label, p_type = identify_and_save(blob, f"{tag}_{i}")
                if label:
                    print(f"   ✨ FOUND: {label.upper()} | Type: {p_type}")

audit()