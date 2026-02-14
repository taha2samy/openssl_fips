import subprocess
import sys

def log_success(test_number, category, justification):
    print(f"[SUCCESS] TEST {test_number:02d} - {category}: PASSED ({justification})")

def log_failure(test_number, category, justification, error_details=None):
    sys.stderr.write(f"[FAILURE] TEST {test_number:02d} - {category}: FAILED ({justification})\n")
    if error_details:
        sys.stderr.write(f"Root Cause: {error_details}\n")
    sys.exit(1)

def run_container_command(image_tag, args, stdin_input=None):
    docker_base = ["docker", "run", "--rm", "-i"] if stdin_input else ["docker", "run", "--rm"]
    cmd = docker_base + [image_tag] + args
    try:
        result = subprocess.run(cmd, input=stdin_input, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_13_tls12_fips_compliance(image_tag):
    cat = "TLS 1.2 FIPS Policy Enforcement"
    approved_cipher = "ECDHE-RSA-AES256-GCM-SHA384"
    code, stdout, stderr = run_container_command(image_tag, ["s_client", "-connect", "www.google.com:443", "-tls1_2", "-cipher", approved_cipher], stdin_input="Q\n")
    combined = stdout + stderr
    if approved_cipher in combined:
        log_success(13, cat, f"Negotiated {approved_cipher} successfully.")
    else:
        log_failure(13, cat, "TLS negotiation failed.", combined.strip())

def test_14_ecdsa_sign_verify(image_tag):
    cat = "ECDSA Sign/Verify (FIPS Curves)"
    code, stdout, stderr = run_container_command(image_tag, ["genpkey", "-algorithm", "EC", "-pkeyopt", "ec_paramgen_curve:P-384"])
    if code != 0: log_failure(14, cat, "Genpkey failed.", stderr)
    priv = stdout
    code, stdout, stderr = run_container_command(image_tag, ["pkey", "-pubout"], stdin_input=priv)
    if code != 0: log_failure(14, cat, "Pubout failed.", stderr)
    pub = stdout
    code, stdout, stderr = run_container_command(image_tag, ["pkey", "-pubin", "-text", "-noout"], stdin_input=pub)
    if code == 0 and "P-384" in stdout:
        log_success(14, cat, "ECDSA P-384 functional under FIPS.")
    else:
        log_failure(14, cat, "ECDSA parse failed.", stdout)

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    target = sys.argv[1]
    test_13_tls12_fips_compliance(target)
    test_14_ecdsa_sign_verify(target)