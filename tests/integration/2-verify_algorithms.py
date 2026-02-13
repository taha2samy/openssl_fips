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

def test_03_algorithm_rejection(image_tag: str):
    category = "FIPS Algorithm Restrictions (MD5)"
    
    code, stdout, stderr = run_container_command(image_tag, ["dgst", "-md5", "/dev/null"])

    if code != 0:
        error_msg = stderr.strip()
        if "unsupported" in error_msg or "fetch failed" in error_msg or "properties" in error_msg:
            log_success(
                3, category,
                "MD5 algorithm correctly rejected by FIPS provider enforcement."
            )
        else:
            log_failure(
                3, category,
                "MD5 failed execution but with an unexpected error message.",
                f"Error: {error_msg}"
            )
    else:
        log_failure(
            3, category,
            "MD5 algorithm was allowed execution despite FIPS mode.",
            "Configuration Failure: Weak algorithms are not being blocked."
        )

def test_04_algorithm_acceptance(image_tag: str):
    category = "FIPS Approved Algorithm (SHA-256)"
    
    code, stdout, stderr = run_container_command(image_tag, ["dgst", "-sha256", "/dev/null"])

    if code == 0:
        log_success(
            4, category,
            "SHA-256 algorithm successfully executed under FIPS restrictions."
        )
    else:
        log_failure(
            4, category,
            "SHA-256 approved algorithm failed execution.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

if __name__ == "__main__":
    print("-" * 80)
    print("CRYPTOGRAPHIC ALGORITHM VALIDATION SUITE (DOCKER WRAPPER)")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_algorithms.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_03_algorithm_rejection(target_image)
    test_04_algorithm_acceptance(target_image)

    print("-" * 80)
    print(f"[SUCCESS] ALGORITHM CHECKS STATUS: PASSED (Target: {target_image})")
    print("-" * 80)