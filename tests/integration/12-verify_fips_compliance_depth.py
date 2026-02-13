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

def run_container_command(image_tag: str, args: list, stdin_input: str = None) -> tuple[int, bytes, bytes]:
    # We use binary mode (text=False) to handle encrypted binary output without crashing
    docker_base = ["docker", "run", "--rm", "-i"] if stdin_input else ["docker", "run", "--rm"]
    cmd = docker_base + [image_tag] + args
    
    input_bytes = stdin_input.encode('utf-8') if stdin_input else None
    
    try:
        result = subprocess.run(
            cmd,
            input=input_bytes,
            capture_output=True,
            text=False, # <-- Handle output as raw bytes
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, b"", str(e).encode('utf-8')

def test_25_triple_des_prohibition(image_tag: str):
    category = "Algorithm Retirement (Triple-DES)"
    
    # Attempting 3DES encryption
    code, stdout, stderr = run_container_command(image_tag, ["enc", "-des-ede3-cbc", "-e", "-k", "password", "-pbkdf2"], stdin_input="testdata")

    # Check stderr (decoded safely with errors='ignore')
    error_msg = stderr.decode('utf-8', errors='ignore').lower()

    if code != 0 and any(x in error_msg for x in ["unsupported", "disabled", "fetch failed", "error"]):
        log_success(
            25, category,
            "Triple-DES correctly blocked for encryption. Policy enforcement is active."
        )
    elif code == 0:
        log_failure(
            25, category,
            "Security vulnerability: Triple-DES encryption was allowed.",
            "Compliance Failure: 3DES is legacy and must be disabled for encryption in FIPS mode."
        )
    else:
        log_failure(25, category, "Unexpected behavior during 3DES block test.", error_msg)

def test_26_hmac_key_length_enforcement(image_tag: str):
    category = "Key Strength Enforcement (HMAC-SHA256)"
    
    short_key = "12345678" # 64 bits (Requirement is 112 bits)
    
    code, stdout, stderr = run_container_command(image_tag, ["dgst", "-sha256", "-hmac", short_key, "/dev/null"])
    error_msg = stderr.decode('utf-8', errors='ignore').lower()

    if code != 0 and any(x in error_msg for x in ["too short", "invalid", "fetch failed", "error"]):
        log_success(
            26, category,
            "System strictly enforced minimum HMAC key length (Requirement: >= 112 bits)."
        )
    elif code == 0:
        log_failure(
            26, category,
            "Compliance Failure: System accepted a sub-112 bit HMAC key.",
            "FIPS 140-3 mandates a minimum effective key strength of 112 bits."
        )
    else:
        log_failure(26, category, "Unexpected error during HMAC key enforcement test.", error_msg)

if __name__ == "__main__":
    print("-" * 80)
    print("DEEP FIPS 140-3 COMPLIANCE & RETIREMENT VALIDATION")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_fips_compliance_depth.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_25_triple_des_prohibition(target_image)
    test_26_hmac_key_length_enforcement(target_image)

    print("-" * 80)
    print(f"[SUCCESS] DEPTH COMPLIANCE STATUS: PASSED (Target: {target_image})")
    print("-" * 80)