import subprocess
import json
import gzip
import io
import base64

IMAGE_REF = "ghcr.io/taha2samy/wolfi-openssl-fips:latest"
REPO = IMAGE_REF.split(':')[0]

def run_command(command, is_binary=False):
    try:
        if is_binary:
            result = subprocess.run(command, capture_output=True, check=True)
            return result.stdout
        else:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
    except Exception as e:
        return None

def parse_attestation_content(raw_data):
    """محاولة قراءة البيانات سواء كانت مضغوطة أو نص صريح"""
    content = None
    # 1. جرب فك الضغط لو بدأ بـ علامة gzip (1f 8b)
    if raw_data.startswith(b'\x1f\x8b'):
        try:
            with gzip.GzipFile(fileobj=io.BytesIO(raw_data)) as f:
                content = f.read().decode('utf-8')
        except: pass
    
    # 2. لو لسه مفيش محتوى، جرب تقرأه كـ نص عادي (بما إنه بدأ بـ {)
    if not content:
        try:
            content = raw_data.decode('utf-8')
        except:
            return None, "Binary Data (Unknown)"

    # 3. تحليل الـ JSON
    try:
        data = json.loads(content)
        
        # ملاحظة مهمة: الـ Attestations غالباً بتكون DSSE Envelope
        # يعني البيانات الحقيقية جوه حقل اسمه payload وتكون base64 encoded
        p_type = "Unknown"
        if "payload" in data:
            # لو هو DSSE envelope
            p_type = data.get("payloadType", "Unknown")
            # نحاول نفك الـ payload عشان نعرف الـ predicateType الحقيقي
            try:
                decoded_payload = json.loads(base64.b64decode(data["payload"]).decode('utf-8'))
                p_type = decoded_payload.get("predicateType", p_type)
            except: pass
        else:
            # لو هو In-toto statement مباشر
            p_type = data.get("predicateType", "Unknown")
            
        return data, p_type
    except:
        return None, "Not a valid JSON"

def start_analysis():
    print(f"🔍 Analyzing Image: {IMAGE_REF}")
    manifest_raw = run_command(["crane", "manifest", IMAGE_REF])
    if not manifest_raw: return
    
    index = json.loads(manifest_raw)
    manifests = index.get('manifests', [])

    images = [m for m in manifests if 'platform' in m and 'attestation' not in m.get('annotations', {}).get('vnd.docker.reference.type', '')]
    attestations = [m for m in manifests if m not in images]

    for img in images:
        arch = img.get('platform', {}).get('architecture')
        img_sha = img.get('digest')
        
        print(f"\n🏗️  Architecture: {arch.upper()}")
        print(f"  🔹 Image SHA: {img_sha}")

        linked = [a for a in attestations if a.get('annotations', {}).get('vnd.docker.reference.digest') == img_sha]

        for attr in linked:
            attr_sha = attr.get('digest')
            print(f"  🎁 Attestation Bundle: {attr_sha}")
            
            attr_manifest_raw = run_command(["crane", "manifest", f"{REPO}@{attr_sha}"])
            if not attr_manifest_raw: continue
            
            attr_manifest = json.loads(attr_manifest_raw)
            for i, layer in enumerate(attr_manifest.get('layers', [])):
                l_sha = layer.get('digest')
                # تحميل الـ Blob
                raw_blob = run_command(["crane", "blob", f"{REPO}@{l_sha}"], is_binary=True)
                
                # --- Debugging Print ---
                prefix = raw_blob[:60]
                print(f"     📂 Layer {i+1} ({l_sha[:12]})")
                print(f"        [DEBUG] First 60 bytes: {prefix}")
                
                data, p_type = parse_attestation_content(raw_blob)
                
                # تمييز النوع
                label = "📦 Unknown"
                filename = f"unknown_{arch}_{l_sha[:8]}.json"
                
                if "spdx" in p_type or "cyclonedx" in p_type:
                    label = "📄 SBOM"
                    filename = f"sbom_{arch}.json"
                elif "provenance" in p_type:
                    label = "🛡️ SLSA"
                    filename = f"provenance_{arch}.json"
                
                print(f"        [TYPE]  Identified as: {p_type}")
                print(f"        [FILE]  Saved to: {filename}")
                
                with open(filename, "w") as f:
                    json.dump(data, f, indent=2)
        print("-" * 60)

if __name__ == "__main__":
    start_analysis()