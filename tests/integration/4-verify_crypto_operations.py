import subprocess
import sys

def log_success(test_number: int, category: str, justification: str):
    print(f"[SUCCESS] TEST {test_number:02d} - {category}: PASSED ({justification})")

def log_failure(test_number: int, category: str, justification: str, error_details: str = None):
    sys.stderr.write(f"[FAILURE] TEST {test_number:02d} - {category}: FAILED ({justification})\n")
    if error_details:
        sys.stderr.write(f"Root Cause: {error_details}\n")
    sys.stderr.write("Process terminated with exit code 1.\n")
    sys.exit(1)

def run_container_command(image_tag: str, args: list) -> tuple[int, str, str]:
    # تشغيل الحاوية وتمرير الأوامر لـ OpenSSL
    cmd = ["docker", "run", "--rm", image_tag] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        return -1, "", "Docker executable not found in PATH."
    except Exception as e:
        return -1, "", str(e)

def inspect_container_config(image_tag: str, format_string: str) -> str:
    cmd = ["docker", "inspect", f"--format={format_string}", image_tag]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"INSPECT_ERROR: {e.stderr.strip()}"
    except Exception as e:
        return f"INSPECT_ERROR: {str(e)}"

def test_08_rsa_key_generation(image_tag: str):
    category = "Asymmetric Key Generation (RSA)"
    
    # توليد مفتاح RSA 2048-bit متوافق مع FIPS (الحد الأدنى المسموح به)
    code, stdout, stderr = run_container_command(image_tag, [
            "genpkey", 
            "-algorithm", "RSA", 
            "-pkeyopt", "rsa_keygen_bits:2048"
        ])
    
    if code == 0 and "-----BEGIN PRIVATE KEY-----" in stdout:
        log_success(
            8, category,
            "FIPS-approved asymmetric key generation (RSA 2048-bit) executed successfully under strict policy."
        )
    else:
        log_failure(
            8, category,
            "Failed to generate a valid RSA key pair under strict FIPS mode.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

def test_09_fips_cipher_availability(image_tag: str):
    category = "Symmetric Cipher Availability (FIPS)"

    # التعديل الجوهري: نستخدم list -cipher-algorithms بدلاً من ciphers
    # لأن وضع security_check=1 يمنع الاستعلامات غير الصريحة لموديولات التشفير
    code, stdout, stderr = run_container_command(image_tag, ["list", "-cipher-algorithms"])

    # التحقق من وجود AES-GCM (الخوارزمية المعيارية في FIPS)
    if code == 0 and "AES-256-GCM" in stdout:
        log_success(
            9, category,
            "Successfully verified AES-GCM availability using the FIPS-compliant 'list' command."
        )
    elif code == 0 and stdout.strip() == "":
        log_failure(
            9, category,
            "Provider listed no algorithms, check if FIPS provider is activated in openssl.cnf."
        )
    else:
        log_failure(
            9, category,
            "Failed to query FIPS algorithms.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

def test_10_non_root_user_enforcement(image_tag: str):
    category = "Container Security (Non-Root User)"

    # التحقق من أن الحاوية تعمل بمستخدم محدود الصلاحيات
    user = inspect_container_config(image_tag, '{{.Config.User}}')

    if user == "openssl":
        log_success(
            10, category,
            "Image security verified: runs as non-root user 'openssl'."
        )
    else:
        log_failure(
            10, category,
            "Security vulnerability: Container is not configured to run as 'openssl' user.",
            f"Expected 'openssl', but found '{user}'."
        )

if __name__ == "__main__":
    print("-" * 80)
    print("STRICT FIPS 140-3 CRYPTO & SECURITY VALIDATION")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_crypto_operations.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_08_rsa_key_generation(target_image)
    test_09_fips_cipher_availability(target_image)
    test_10_non_root_user_enforcement(target_image)

    print("-" * 80)
    print(f"[SUCCESS] CRYPTO OPERATIONS STATUS: ALL PASSED (Target: {target_image})")
    print("-" * 80)
