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
        # We send 'Q\n' to stdin to cleanly quit the s_client session
        result = subprocess.run(
            cmd,
            input="Q\n", 
            capture_output=True,
            text=True,
            check=False 
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        return -1, "", "Docker executable not found in PATH."
    except Exception as e:
        return -1, "", str(e)

def test_05_tcp_connectivity(image_tag: str):
    category = "Network Stack (TCP/IP Sockets)"
    
    code, stdout, stderr = run_container_command(image_tag, ["s_client", "-connect", "1.1.1.1:443"])

    # --- FIX: Combine stdout and stderr for a robust check ---
    combined_output = stdout + stderr

    if code == 0 and ("CONNECTION ESTABLISHED" in combined_output or "Verification: OK" in combined_output):
        log_success(
            5, category,
            "Raw TCP/IP socket connection established successfully to 1.1.1.1:443."
        )
    elif "Network is unreachable" in combined_output:
         log_failure(
            5, category,
            "Container failed to create network socket.",
            f"Output: {combined_output.strip()}"
        )
    else:
        log_failure(
            5, category,
            "Failed to establish connection to direct IP address.",
            f"Exit Code: {code}, Output: {combined_output.strip()}"
        )

def test_06_dns_resolution(image_tag: str):
    category = "DNS Resolution (libc/libnss)"
    
    code, stdout, stderr = run_container_command(image_tag, ["s_client", "-connect", "google.com:443"])

    # --- FIX: Combine stdout and stderr for a robust check ---
    combined_output = stdout + stderr

    if code == 0 and ("CONNECTION ESTABLISHED" in combined_output or "Verification: OK" in combined_output):
        log_success(
            6, category,
            "DNS resolution for google.com succeeded, confirming resolver libraries are present."
        )
    else:
        error_msg = combined_output.strip()
        if "gethostbyname failure" in error_msg or "Name or service not known" in error_msg:
             log_failure(
                6, category,
                "DNS lookup failed. Missing glibc resolver libraries or /etc/resolv.conf configuration.",
                f"Error: {error_msg}"
            )
        else:
            log_failure(
                6, category,
                "Failed to resolve or connect to hostname.",
                f"Exit Code: {code}, Error: {error_msg}"
            )

if __name__ == "__main__":
    print("-" * 80)
    print("NETWORK & DNS VALIDATION SUITE (DOCKER WRAPPER)")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_network_dns.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_05_tcp_connectivity(target_image)
    test_06_dns_resolution(target_image)

    print("-" * 80)
    print(f"[SUCCESS] NETWORK CHECKS STATUS: PASSED (Target: {target_image})")
    print("-" * 80)