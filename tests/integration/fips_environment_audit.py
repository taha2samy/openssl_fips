import subprocess
import sys
import os

def log_audit(test_number: int, category: str, status: str, justification: str):
    icon = "✅" if status == "PASSED" else "❌"
    print(f"{icon} [AUDIT {test_number:02d}] - {category}: {status}")
    print(f"    Justification: {justification}")
    print("-" * 60)

def audit_distroless_env(image_tag):
    print(f"\n# STARTING UNIVERSAL FIPS AUDIT (NO-SHELL COMPATIBLE): {image_tag}")
    print("=" * 70)

    # 1. التحقق من حالة المزود (المرجع الأساسي)
    res = subprocess.run(["docker", "run", "--rm", image_tag, "list", "-providers", "-verbose"], capture_output=True, text=True)
    if "fips" in res.stdout and "status: active" in res.stdout:
        log_audit(1, "FIPS Provider Load", "PASSED", "FIPS module is active and MAC is verified by OpenSSL core.")
    else:
        log_audit(1, "FIPS Provider Load", "FAILED", "FIPS module failed to load.")

    # 2. استخراج الملفات للفحص الخارجي (لأن Distroless لا يوجد بها cat)
    temp_file = "temp_fips_config.cnf"
    # نستخدم حيلة docker cp لاستخراج الملف
    container_id = subprocess.run(["docker", "create", image_tag], capture_output=True, text=True).stdout.strip()
    subprocess.run(["docker", "cp", f"{container_id}:/usr/local/ssl/fipsmodule.cnf", temp_file], capture_output=True)
    subprocess.run(["docker", "rm", container_id], capture_output=True)

    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            content = f.read()
        
        checks = {
            "security-checks = 1": "Global FIPS 140-3 enforcement",
            "hmac-key-check = 1": "HMAC key length validation",
            "pbkdf2-lower-bound-check = 1": "PBKDF2 salt/iter enforcement"
        }

        for key, desc in checks.items():
            if key in content:
                log_audit(2, f"Setting: {key}", "PASSED", f"Found in fipsmodule.cnf: {desc}")
            else:
                log_audit(2, f"Setting: {key}", "FAILED", f"NOT FOUND: {desc}")
        
        os.remove(temp_file)
    else:
        log_audit(2, "Configuration Access", "FAILED", "Could not extract fipsmodule.cnf from distroless image.")

if __name__ == "__main__":
    audit_distroless_env(sys.argv[1])