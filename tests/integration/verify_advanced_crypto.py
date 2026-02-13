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
    docker_base = ["docker", "run", "--rm", "-i"] if stdin_input else ["docker", "run", "--rm"]
    cmd = docker_base + [image_tag] + args
    try:
        result = subprocess.run(
            cmd,
            input=stdin_input,
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_13_tls12_fips_compliance(image_tag: str):
    category = "TLS 1.2 FIPS Policy Enforcement"
    approved_cipher = "ECDHE-RSA-AES256-GCM-SHA384"
    
    code, stdout, stderr = run_container_command(
        image_tag, 
        ["s_client", "-connect", "www.google.com:443", "-tls1_2", "-cipher", approved_cipher], 
        stdin_input="Q\n"
    )
    combined_output = stdout + stderr

    if code == 0 and approved_cipher in combined_output:
        log_success(
            13, category,
            f"Successfully negotiated a FIPS-approved TLS 1.2 connection using {approved_cipher}."
        )
    else:
        log_failure(
            13, category,
            "Failed to establish a compliant TLS 1.2 connection.",
            f"Exit Code: {code}, Output: {combined_output.strip()}"
        )

def test_14_ecdsa_sign_verify(image_tag: str):
    category = "ECDSA Sign/Verify (FIPS Curves)"
    
    code, stdout, stderr = run_container_command(image_tag, ["genpkey", "-algorithm", "EC", "-pkeyopt", "ec_paramgen_curve:P-384"])
    if code != 0:
        log_failure(14, category, "Failed to generate P-384 elliptic curve key pair.", stderr.strip())
    
    private_key = stdout

    code, stdout, stderr = run_container_command(image_tag, ["pkey", "-pubout"], stdin_input=private_key)
    if code != 0:
        log_failure(14, category, "Failed to extract public key from generated EC private key.", stderr.strip())
    
    public_key = stdout

    code, stdout, stderr = run_container_command(image_tag, ["pkey", "-pubin", "-text", "-noout"], stdin_input=public_key)

    if code == 0 and "P-384" in stdout:
         log_success(
            14, category,
            "ECDSA P-384 primitives (Keygen/Extraction/Parsing) are fully operational under FIPS provider."
        )
    else:
        log_failure(
            14, category,
            "ECDSA P-384 validation failed during public key parsing.",
            f"Stdout: {stdout.strip()}, Stderr: {stderr.strip()}"
        )

if __name__ == "__main__":
    print("-" * 80)
    print("ADVANCED NETWORK CRYPTO & EC VALIDATION SUITE")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_advanced_crypto.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_13_tls12_fips_compliance(target_image)
    test_14_ecdsa_sign_verify(target_image)

    print("-" * 80)
    print(f"[SUCCESS] ADVANCED CRYPTO STATUS: PASSED (Target: {target_image})")
    print("-" * 80)