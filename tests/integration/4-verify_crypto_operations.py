import subprocess
import sys

def log_success(test_number, category, justification):
    print(f"[SUCCESS] TEST {test_number:02d} - {category}: PASSED ({justification})")

def log_failure(test_number, category, justification, error_details=None):
    sys.stderr.write(f"[FAILURE] TEST {test_number:02d} - {category}: FAILED ({justification})\n")
    if error_details:
        sys.stderr.write(f"Root Cause: {error_details}\n")
    sys.exit(1)

def run_container_command(image_tag, args):
    cmd = ["docker", "run", "--rm", image_tag] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def inspect_container_config(image_tag, format_string):
    cmd = ["docker", "inspect", f"--format={format_string}", image_tag]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"INSPECT_ERROR: {str(e)}"

def test_08_rsa_key_generation(image_tag):
    cat = "Asymmetric Key Generation (RSA)"
    code, stdout, stderr = run_container_command(image_tag, ["genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048"])
    if code == 0 and "BEGIN PRIVATE KEY" in stdout:
        log_success(8, cat, "FIPS-approved RSA 2048-bit generation successful.")
    else:
        log_failure(8, cat, "RSA key generation failed.", f"Stderr: {stderr}")

def test_09_fips_cipher_availability(image_tag):
    cat = "Symmetric Cipher Availability (FIPS)"
    code, stdout, stderr = run_container_command(image_tag, ["list", "-cipher-algorithms", "-propquery", "fips=yes"])
    if code == 0 and "AES-256-GCM" in stdout.upper():
        log_success(9, cat, "AES-GCM identified via FIPS provider.")
    else:
        log_failure(9, cat, "FIPS algorithms not found.", f"Stdout: {stdout}")

def test_10_non_root_user_enforcement(image_tag):
    cat = "Container Security (Non-Root User)"
    user = inspect_container_config(image_tag, '{{.Config.User}}')
    if user == "openssl":
        log_success(10, cat, "Verified: runs as 'openssl' user.")
    else:
        log_failure(10, cat, "Security failure.", f"Found: {user}")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    target = sys.argv[1]
    test_08_rsa_key_generation(target)
    test_09_fips_cipher_availability(target)
    test_10_non_root_user_enforcement(target)
    print(f"\n[DONE] ALL TESTS PASSED ON: {target}")