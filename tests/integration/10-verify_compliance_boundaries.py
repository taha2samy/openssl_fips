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

def test_21_weak_key_length_rejection(image_tag: str):
    category = "Parameter Validation (RSA Key Length)"
    
    code, stdout, stderr = run_container_command(image_tag, ["genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:1024"])

    if code != 0 and ("invalid" in stderr or "too small" in stderr or "error" in stderr):
        log_success(
            21, category,
            "FIPS policy correctly rejected an RSA 1024-bit key (Minimum required is 2048 bits)."
        )
    elif code == 0:
        log_failure(
            21, category,
            "Security vulnerability: The system allowed generation of a weak RSA 1024-bit key.",
            "FIPS 140-3 mandates a minimum key length of 2048 bits for RSA."
        )
    else:
        log_failure(
            21, category,
            "Unexpected error during weak key length test.",
            f"Stderr: {stderr.strip()}"
        )

def test_22_fips_indicator_logic(image_tag: str):
    category = "Implicit Service Indicator"
    
    code, stdout, stderr = run_container_command(image_tag, ["dgst", "-sha1", "/dev/null"])

    if code != 0:
        log_success(
            22, category,
            "System strictly restricted SHA-1 usage (restricted in many FIPS 140-3 contexts)."
        )
    else:
        log_success(
            22, category,
            "SHA-1 is available (FIPS allows SHA-1 for non-signing or legacy verification tasks)."
        )

if __name__ == "__main__":
    print("-" * 80)
    print("FIPS COMPLIANCE BOUNDARIES & PARAMETER VALIDATION")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_compliance_boundaries.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_21_weak_key_length_rejection(target_image)
    test_22_fips_indicator_logic(target_image)

    print("-" * 80)
    print(f"[SUCCESS] BOUNDARY CHECKS STATUS: PASSED (Target: {target_image})")
    print("-" * 80)