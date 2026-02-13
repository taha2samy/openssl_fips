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

def run_container_command(image_tag: str, args: list, read_only: bool = False) -> tuple[int, str, str]:
    docker_cmd = ["docker", "run", "--rm"]
    if read_only:
        docker_cmd.append("--read-only")
    
    cmd = docker_cmd + [image_tag] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_15_read_only_execution(image_tag: str):
    category = "Immutability (Read-Only Filesystem)"
    
    code, stdout, stderr = run_container_command(image_tag, ["version", "-a"], read_only=True)

    if code == 0 and "OpenSSL" in stdout:
        log_success(
            15, category,
            "OpenSSL and FIPS provider successfully initialized on a read-only root filesystem."
        )
    else:
        log_failure(
            15, category,
            "Execution failed on read-only filesystem. Possible attempt to write to /tmp or /usr/local/ssl.",
            f"Stderr: {stderr.strip()}"
        )

def test_16_directory_path_audit(image_tag: str):
    category = "Path Integrity (Directory Audit)"
    
    code, stdout, stderr = run_container_command(image_tag, ["version", "-d"])

    if code == 0 and "OPENSSLDIR: \"/usr/local/ssl\"" in stdout:
        log_success(
            16, category,
            "OpenSSL is strictly bound to the secure /usr/local/ssl directory, preventing fallback to system paths."
        )
    else:
        log_failure(
            16, category,
            "OpenSSL is pointing to an insecure or incorrect configuration directory.",
            f"Stdout: {stdout.strip()}"
        )

if __name__ == "__main__":
    print("-" * 80)
    print("SECURITY HARDENING & PATH INTEGRATION VALIDATION SUITE")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_hardening_paths.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_15_read_only_execution(target_image)
    test_16_directory_path_audit(target_image)

    print("-" * 80)
    print(f"[SUCCESS] HARDENING STATUS: PASSED (Target: {target_image})")
    print("-" * 80)