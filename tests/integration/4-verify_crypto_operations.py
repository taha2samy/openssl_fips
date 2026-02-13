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
    
    # Generate a FIPS-compliant 2048-bit RSA key.
    code, stdout, stderr = run_container_command(image_tag, ["genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048"])

    if code == 0 and stdout.startswith("-----BEGIN PRIVATE KEY-----"):
        log_success(
            8, category,
            "FIPS-approved asymmetric key generation primitive (RSA 2048-bit) executed successfully."
        )
    else:
        log_failure(
            8, category,
            "Failed to generate a valid RSA key pair under FIPS mode.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

def test_09_fips_cipher_availability(image_tag: str):
    category = "Symmetric Cipher Availability"

    # List only the ciphers available through the FIPS provider.
    code, stdout, stderr = run_container_command(image_tag, ["ciphers", "FIPS"])

    if code == 0 and "AES" in stdout and "GCM" in stdout:
        log_success(
            9, category,
            "Successfully listed FIPS-approved ciphers, confirming AES-GCM suite is available."
        )
    elif code == 0 and stdout.strip() == "":
        log_failure(
            9, category,
            "Command succeeded but returned no FIPS ciphers, indicating a provider property issue."
        )
    else:
        log_failure(
            9, category,
            "Failed to query for FIPS-approved cipher suites.",
            f"Exit Code: {code}, Stderr: {stderr.strip()}"
        )

def test_10_non_root_user_enforcement(image_tag: str):
    category = "Container Security (Non-Root User)"

    # We check the image metadata directly, as 'distroless' has no shell to run 'id'.
    user = inspect_container_config(image_tag, '{{.Config.User}}')

    if user == "openssl":
        log_success(
            10, category,
            "Image is correctly configured to run as the dedicated non-root user 'openssl'."
        )
    else:
        log_failure(
            10, category,
            "Image is not configured to run as a non-root user, violating security best practices.",
            f"Expected user 'openssl', but found '{user}'."
        )

if __name__ == "__main__":
    print("-" * 80)
    print("CRYPTO OPERATIONS & SECURITY VALIDATION SUITE")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_crypto_operations.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_08_rsa_key_generation(target_image)
    test_09_fips_cipher_availability(target_image)
    test_10_non_root_user_enforcement(target_image)

    print("-" * 80)
    print(f"[SUCCESS] CRYPTO OPERATIONS STATUS: PASSED (Target: {target_image})")
    print("-" * 80)