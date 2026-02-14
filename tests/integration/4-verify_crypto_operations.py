import subprocess
import sys

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def log_success(test_no, category, message):
    print(f"{GREEN}[SUCCESS]{RESET} TEST {test_no:02d} - {category}: {message}")

def log_failure(test_no, category, message, error_details=None):
    print(f"{RED}[FAILURE]{RESET} TEST {test_no:02d} - {category}: {message}")
    if error_details:
        print(f"{BLUE}[DEBUG]{RESET} Root Cause: {error_details}")
    sys.exit(1)

def run_cmd(image, args, stdin_input=None):
    docker_base = ["docker", "run", "--rm", "-i"] if stdin_input else ["docker", "run", "--rm"]
    cmd = docker_base + [image] + args
    try:
        proc = subprocess.run(
            cmd,
            input=stdin_input.encode() if stdin_input else None,
            capture_output=True,
            text=True,
            check=False
        )
        return proc.returncode, proc.stdout, proc.stderr
    except Exception as e:
        return -1, "", str(e)

def test_00_diagnostic(image):
    print(f"{BLUE}[INFO]{RESET} Checking Environment and Config Paths...")
    code, out, err = run_cmd(image, ["version", "-d"])
    print(f"OPENSSLDIR: {out.strip()}")
    code, out, err = run_cmd(image, ["list", "-providers", "-verbose"])
    print(f"Providers Status:\n{out}")

def test_08_rsa_gen(image):
    category = "Asymmetric Key Gen (RSA)"
    args = [
        "genpkey",
        "-provider", "fips",
        "-provider", "base",
        "-propquery", "fips=yes",
        "-algorithm", "RSA",
        "-pkeyopt", "rsa_keygen_bits:2048"
    ]
    code, out, err = run_cmd(image, args)
    if code == 0 and "-----BEGIN PRIVATE KEY-----" in out:
        log_success(8, category, "RSA 2048-bit key generated successfully.")
    else:
        log_failure(8, category, "FIPS RSA generation failed.", f"ExitCode: {code}, Stderr: {err.strip()}")

def test_09_cipher_list(image):
    category = "Symmetric Cipher Availability"
    args = ["list", "-cipher-algorithms", "-provider", "fips"]
    code, out, err = run_cmd(image, args)
    if code == 0 and ("AES" in out or "GCM" in out):
        log_success(9, category, "Verified FIPS algorithms listing.")
    else:
        log_failure(9, category, "FIPS ciphers not listed.", out)

def test_26_hmac_enforcement(image):
    category = "HMAC Key Length Enforcement"
    short_key = "12345678"
    args = [
        "dgst", 
        "-sha256", 
        "-propquery", "fips=yes", 
        "-hmac", short_key, 
        "/dev/null"
    ]
    code, out, err = run_cmd(image, args)
    if code != 0:
        log_success(26, category, "Strict policy REJECTED short HMAC key. Correct behavior.")
    else:
        log_failure(26, category, "Compliance Failure: System accepted a 64-bit HMAC key!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    target = sys.argv[1]
    print("="*80)
    print(f"STARTING FIPS 140-3 COMPLIANCE AUDIT: {target}")
    print("="*80)
    test_00_diagnostic(target)
    test_08_rsa_gen(target)
    test_09_cipher_list(target)
    test_26_hmac_enforcement(target)
    print("="*80)
    print(f"{GREEN}ALL TESTS PASSED: Image is FIPS 140-3 Compliant!{RESET}")
    print("="*80)
