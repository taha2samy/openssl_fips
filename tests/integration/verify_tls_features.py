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

def run_container_command(image_tag: str, args: list, stdin_input: str = None) -> tuple[int, str, str]:
    cmd = ["docker", "run", "--rm", image_tag] + args
    try:
        result = subprocess.run(
            cmd,
            input=stdin_input,
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        return -1, "", "Docker executable not found in PATH."
    except Exception as e:
        return -1, "", str(e)

def test_11_certificate_parsing(image_tag: str):
    category = "X.509 Certificate Parsing"
    code, stdout, stderr = run_container_command(image_tag, ["x509", "-in", "/etc/ssl/certs/ca-certificates.crt", "-noout", "-text"])

    if code == 0 and "Certificate:" in stdout and "Subject:" in stdout:
        log_success(11, category, "OpenSSL x509 utility successfully parsed a certificate file from the filesystem.")
    else:
        log_failure(11, category, "Failed to read and parse a local certificate file.", f"Exit Code: {code}, Stderr: {stderr.strip()}")

def test_12_cipher_suite_enforcement(image_tag: str):
    category = "TLS Cipher Suite Enforcement"
    cipher_suite = "TLS_AES_256_GCM_SHA384"
    
    code, stdout, stderr = run_container_command(image_tag, ["s_client", "-connect", "www.google.com:443", "-ciphersuites", cipher_suite], stdin_input="Q\n")
    combined_output = stdout + stderr

    # --- FINAL FIX: Search for 'Cipher' and the suite name anywhere in the same line ---
    cipher_match = any("Cipher" in line and cipher_suite in line for line in combined_output.splitlines())

    if code == 0 and cipher_match:
        log_success(
            12, category,
            f"Successfully established a TLSv1.3 connection using the enforced FIPS-approved cipher ({cipher_suite})."
        )
    elif "no ciphers available" in combined_output:
        log_failure(
            12, category,
            "The requested FIPS-approved cipher suite is not available for TLS negotiation.",
            "This indicates a critical failure in the FIPS provider's integration with the TLS stack."
        )
    else:
        log_failure(
            12, category,
            f"Failed to connect using the mandatory cipher suite '{cipher_suite}'.",
            f"Exit Code: {code}, Output: {combined_output.strip()}"
        )

if __name__ == "__main__":
    print("-" * 80)
    print("ADVANCED TLS FEATURES & CERTIFICATE HANDLING VALIDATION SUITE")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_tls_features.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_11_certificate_parsing(target_image)
    test_12_cipher_suite_enforcement(target_image)

    print("-" * 80)
    print(f"[SUCCESS] TLS FEATURES STATUS: PASSED (Target: {target_image})")
    print("-" * 80)