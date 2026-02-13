import subprocess
import sys
import re

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
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False 
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        return -1, "", "Docker executable not found in PATH."
    except Exception as e:
        return -1, "", str(e)

def test_01_provider_presence(image_tag: str):
    category = "FIPS Provider Availability"
    
    code, stdout, stderr = run_container_command(image_tag, ["list", "-providers"])

    if code != 0:
        log_failure(
            1, category,
            "OpenSSL exited with an error code during provider listing.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

    pattern = re.compile(r"fips\s+name:.*status:\s*active", re.DOTALL)
    
    if pattern.search(stdout):
        log_success(
            1, category,
            "OpenSSL successfully lists 'fips' provider with 'active' status, confirming proper integration."
        )
    else:
        log_failure(
            1, category,
            "FIPS provider is missing or not in active state.",
            f"Output snippet: {stdout[:100]}..."
        )

def test_02_module_integrity(image_tag: str):
    category = "FIPS Module Integrity Self-Test"
    
    code, stdout, stderr = run_container_command(image_tag, ["list", "-providers", "-verbose"])

    if code != 0:
        error_msg = stderr.strip()
        if "checksum mismatch" in error_msg or "integrity check" in error_msg:
            log_failure(
                2, category,
                "The FIPS module failed its Power-On Self-Test (POST) due to checksum mismatch.",
                error_msg
            )
        else:
            log_failure(
                2, category,
                "OpenSSL crashed or aborted during verbose provider listing.",
                f"Exit Code: {code}, Error: {error_msg}"
            )

    if "fips" in stdout and "status: active" in stdout:
        log_success(
            2, category,
            "Module self-test verified via verbose status check; no checksum or MAC mismatches reported."
        )
    else:
        log_failure(
            2, category,
            "Module loaded without error but status is not explicitly active in verbose mode.",
            "Potential configuration inconsistency."
        )

if __name__ == "__main__":
    print("-" * 80)
    print("CRYPTOGRAPHIC COMPLIANCE VALIDATION SUITE (DOCKER WRAPPER)")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_fips_audit.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_01_provider_presence(target_image)
    test_02_module_integrity(target_image)

    print("-" * 80)
    print(f"[SUCCESS] OVERALL STATUS: PASSED (Target: {target_image})")
    print("-" * 80)