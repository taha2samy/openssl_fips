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
    cmd = ["docker", "run", "--rm", image_tag] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_23_fips_status_indicator(image_tag: str):
    category = "FIPS 140-3 Service Indicator"
    code, stdout, stderr = run_container_command(image_tag, ["list", "-providers", "-verbose"])

    if code == 0 and "status: active" in stdout and "name: OpenSSL FIPS Provider" in stdout:
        log_success(
            23, category,
            "Service indicator confirms the module is in a FIPS-approved operational state."
        )
    else:
        log_failure(
            23, category,
            "Module failed to provide a positive FIPS service indicator.",
            f"Output: {stdout.strip()}"
        )

def test_24_approved_kdf_operation(image_tag: str):
    category = "Approved Service (PBKDF2 Derivation)"
    
    # NIST SP 800-132 mandates a minimum salt length of 128 bits (16 bytes).
    # Using a compliant 16-byte salt: '1234567890123456'
    compliant_salt = "1234567890123456" 
    
    args = [
        "kdf", "-kdfopt", "digest:SHA256", 
        "-kdfopt", "pass:password", 
        "-kdfopt", f"salt:{compliant_salt}", 
        "-kdfopt", "iter:10000", 
        "-keylen", "32", "PBKDF2"
    ]
    
    code, stdout, stderr = run_container_command(image_tag, args)

    if code == 0 and len(stdout.strip()) > 0:
        log_success(
            24, category,
            "FIPS-approved Key Derivation Function (PBKDF2) executed successfully with NIST-compliant salt length (128-bit)."
        )
    else:
        log_failure(
            24, category,
            "The module rejected the KDF service request even with compliant parameters.",
            f"Stderr: {stderr.strip()}"
        )

if __name__ == "__main__":
    print("-" * 80)
    print("FIPS 140-3 CORE OPERATIONAL VALIDATION")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_fips_140_3_core.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_23_fips_status_indicator(target_image)
    test_24_approved_kdf_operation(target_image)

    print("-" * 80)
    print(f"[SUCCESS] 140-3 CORE STATUS: PASSED (Target: {target_image})")
    print("-" * 80)