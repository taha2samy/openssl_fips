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

def test_19_fips_provider_metadata(image_tag: str):
    category = "FIPS Module Metadata Validation"
    
    # We check the specific version of the FIPS provider to ensure it's the validated 3.1.2 module
    code, stdout, stderr = run_container_command(image_tag, ["list", "-providers", "-verbose"])

    if code == 0 and "name: OpenSSL FIPS Provider" in stdout and "version: 3.1.2" in stdout:
        log_success(
            19, category,
            "FIPS provider metadata matches the NIST-validated module version (3.1.2)."
        )
    else:
        log_failure(
            19, category,
            "FIPS provider metadata mismatch or provider not found.",
            f"Output: {stdout.strip()}"
        )

def test_20_mandatory_fips_property(image_tag: str):
    category = "Mandatory FIPS Property Enforcement"
    
    # We try to force SHA256 using a non-FIPS implementation by setting fips=no.
    # If the policy 'default_properties = fips=yes' is working, this MUST fail.
    code, stdout, stderr = run_container_command(image_tag, ["dgst", "-sha256", "-propquery", "fips=no", "/dev/null"])

    if code != 0 and ("unsupported" in stderr or "fetch failed" in stderr):
        log_success(
            20, category,
            "Strict Policy Enforcement: System correctly rejected a request to bypass FIPS via property query (fips=no)."
        )
    elif code == 0:
        log_failure(
            20, category,
            "Security Bypass Detected: The system allowed a non-FIPS property query.",
            "The configuration 'default_properties = fips=yes' is not being enforced."
        )
    else:
        log_failure(
            20, category,
            "Unexpected behavior during mandatory property test.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

if __name__ == "__main__":
    print("-" * 80)
    print("FIPS GLOBAL POLICY & METADATA VALIDATION SUITE")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_fips_policy_metadata.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_19_fips_provider_metadata(target_image)
    test_20_mandatory_fips_property(target_image)

    print("-" * 80)
    print(f"[SUCCESS] POLICY & METADATA STATUS: PASSED (Target: {target_image})")
    print("-" * 80)