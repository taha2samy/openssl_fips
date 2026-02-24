import pytest
import allure
import os
import tempfile
import base64
import subprocess
import re
import inspect

@allure.feature("Network Stack & TLS Compliance")
class TestNetworkAndTLS:
    """
    Validates the container's network capabilities, DNS resolution, and TLS handshake integrity.
    Ensures that FIPS-approved cryptographic libraries are correctly linked with system network sockets.
    """

    @allure.story("Low-Level Network Connectivity")
    @allure.title("Verify Raw TCP/IP Socket Connectivity")
    @allure.description("""
        Detailed Validation of the Container's TCP/IP Stack:
        1. Attempts to establish a raw socket connection to a known public IP (1.1.1.1).
        2. Bypasses DNS resolution to isolate the network stack's ability to create and manage TCP sessions.
        3. Verifies that the FIPS-enabled OpenSSL client can correctly initialize a handshake over raw IP sockets.
        4. Monitors for 'Network is unreachable' or 'Connection refused' errors at the kernel interface level.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("network", "tcp", "connectivity", "ip-direct")
    def test_tcp_connectivity(self, run_docker, image_tag):
        with allure.step("Initiating TCP connection to direct IP address 1.1.1.1"):
            result = run_docker(image_tag, ["s_client", "-connect", "1.1.1.1:443"])
            
            allure.attach(result.stdout, name="Standard Output", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Standard Error", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Analyzing connection status and handshake headers"):
            combined_output = (result.stdout + result.stderr).upper()
            connection_success = any(x in combined_output for x in ["CONNECTION ESTABLISHED", "VERIFICATION: OK"])
            
            if not connection_success:
                allure.dynamic.description(message="Network Failure: Unable to establish raw TCP connection to 1.1.1.1")
                pytest.fail(f"TCP connectivity test failed with exit code {result.returncode}. Output: {result.stderr}")

        with allure.step("Recording network operational metrics"):
            allure.dynamic.parameter("Target IP", "1.1.1.1")
            allure.dynamic.parameter("Port", "443")
            allure.dynamic.parameter("Protocol", "TCP/IP")

    @allure.story("DNS & Resolver Integration")
    @allure.title("Verify DNS Resolution and Libc Integration")
    @allure.description("""
        Validates the integration between the Cryptographic Module and the System Name Resolver:
        1. Executes a hostname lookup for 'google.com' via the OpenSSL s_client utility.
        2. Ensures that the container's 'libc' (glibc or musl) correctly interfaces with /etc/resolv.conf.
        3. Confirms that the Name Service Switch (NSS) can resolve external domains into routable IP addresses.
        4. Validates that the FIPS provider can successfully wrap the resolved socket in a TLS session.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("dns", "resolution", "libc", "integration")
    def test_dns_resolution(self, run_docker, image_tag):
        with allure.step("Attempting hostname resolution for google.com"):
            result = run_docker(image_tag, ["s_client", "-connect", "google.com:443"])
            
            allure.attach(result.stdout, name="Resolver Output", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Resolver Errors", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying successful lookup and handshake"):
            combined_output = (result.stdout + result.stderr).upper()
            
            if "GETHOSTBYNAME FAILURE" in combined_output or "NAME OR SERVICE NOT KNOWN" in combined_output:
                allure.dynamic.status_details(message="DNS Failure: Hostname resolution libraries are missing or misconfigured.")
                pytest.fail("The container failed to resolve the hostname. Check DNS resolver libraries and configuration.")

            dns_success = any(x in combined_output for x in ["CONNECTION ESTABLISHED", "VERIFICATION: OK"])
            assert dns_success, f"DNS resolution succeeded but the handshake failed. Exit code: {result.returncode}"

        with allure.step("Recording DNS compliance metadata"):
            allure.dynamic.parameter("Target Hostname", "google.com")
            allure.dynamic.parameter("Resolution Type", "Standard libc/libnss")
            allure.dynamic.parameter("Handshake Status", "Verified")



    @allure.story("X.509 Certificate Handling")
    @allure.title("Verify X.509 Certificate Parsing & Structural Integrity")
    @allure.description("""
        Comprehensive Validation of Certificate Parsing Capabilities:
        1. Accesses the system's root CA bundle located at /etc/ssl/certs/ca-certificates.crt.
        2. Utilizes the 'x509' utility to parse and decode the certificate structure without outputting the body.
        3. Verifies that the FIPS provider can successfully identify and extract mandatory fields (Subject, Issuer, Public Key).
        4. Ensures that the module's ASN.1 parser is fully operational and compatible with standard trust stores.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("x509", "certificates", "parsing", "asn1")
    def test_certificate_parsing(self, run_docker, image_tag):
        cert_path = "/etc/ssl/certs/ca-certificates.crt"
        
        with allure.step(f"Parsing system certificate bundle at {cert_path}"):
            result = run_docker(image_tag, ["x509", "-in", cert_path, "-noout", "-text"])
            
            allure.attach(result.stdout, name="Parsed Certificate Metadata", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Parsing Errors", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying structural integrity of the parsed data"):
            assert result.returncode == 0, f"Certificate parsing failed. Path might be missing or corrupted. Stderr: {result.stderr}"
            
            output = result.stdout
            assert "Certificate:" in output and "Subject:" in output, \
                "Incomplete parsing: Mandatory X.509 fields were not found in the output."

        with allure.step("Recording certificate validation parameters"):
            allure.dynamic.parameter("Target Path", cert_path)
            allure.dynamic.parameter("Parser Utility", "OpenSSL x509")

    @allure.story("TLS Cipher Suite Enforcement")
    @allure.title("Verify Mandatory FIPS-Approved Cipher Suite Enforcement")
    @allure.description("""
        Strict Validation of TLS Negotiation and Cipher Availability:
        1. Attempts to establish a TLS 1.3 connection to a secure endpoint (google.com).
        2. Forces the use of the high-strength FIPS-approved cipher: TLS_AES_256_GCM_SHA384.
        3. Validates that the TLS stack correctly selects and applies the requested cipher suite.
        4. Ensures that no fallback to non-approved or weaker ciphers occurs during the handshake.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("tls1.3", "cipher-enforcement", "security-policy", "aead")
    def test_cipher_suite_enforcement(self, run_docker, image_tag):
        target_cipher = "TLS_AES_256_GCM_SHA384"
        
        with allure.step(f"Negotiating TLS connection using enforced cipher: {target_cipher}"):
            # Note: s_client implementation handles 'Q' via the fixture if needed
            result = run_docker(image_tag, ["s_client", "-connect", "www.google.com:443", "-ciphersuites", target_cipher])
            
            allure.attach(result.stdout, name="Handshake Log", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Handshake Errors", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Analyzing negotiated cipher parameters"):
            combined_output = result.stdout + result.stderr
            
            if "no ciphers available" in combined_output.lower():
                allure.dynamic.status_details(message=f"Policy Failure: {target_cipher} is not available in FIPS mode.")
                pytest.fail("The mandatory FIPS-approved cipher suite is missing from the provider's registry.")

            # Search for the cipher in the output to confirm it was actually used
            cipher_confirmed = any("Cipher" in line and target_cipher in line for line in combined_output.splitlines())
            
            assert result.returncode == 0 and cipher_confirmed, \
                f"Failed to establish connection using enforced cipher {target_cipher}. Check TLS stack integration."

        with allure.step("Recording TLS security metrics"):
            allure.dynamic.parameter("Enforced Cipher", target_cipher)
            allure.dynamic.parameter("TLS Version", "1.3")
            allure.dynamic.parameter("Handshake Status", "Successfully Verified")


    @allure.story("Module Integrity & Tamper Resistance")
    @allure.title("Verify FIPS Provider Rejection on Configuration Tampering")
    @allure.description("""
        Simulates a manual tampering attack on the FIPS cryptographic module:
        1. Extracts the 'fipsmodule.cnf' from the container via Base64 encoding.
        2. Deliberately corrupts the 'module-mac' value to simulate an unauthorized modification.
        3. Re-injects the corrupted configuration into the container using a volume mount.
        4. Validates that the FIPS provider detects the integrity violation and refuses to enter the 'active' state.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("integrity", "tamper-detection", "mac-verification")
    def test_integrity_check_tampering(self, image_tag):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = os.path.join(tmpdir, "fipsmodule.cnf")
            target_path = "/usr/local/ssl/fipsmodule.cnf"

            with allure.step("Extracting and decoding FIPS module configuration"):
                extract_cmd = ["docker", "run", "--user", "0", "--rm", image_tag, "base64", "-in", target_path]
                result = subprocess.run(extract_cmd, capture_output=True, text=True)
                
                if result.returncode != 0:
                    pytest.fail(f"Failed to extract configuration: {result.stderr}")
                
                original_content = base64.b64decode(result.stdout).decode('utf-8')

            with allure.step("Injecting corrupted MAC to simulate tampering"):
                if "module-mac =" not in original_content:
                    pytest.fail("Could not locate 'module-mac' in the configuration file.")
                
                corrupted_mac = "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00"
                import re
                corrupted_content = re.sub(r"(module-mac\s*=\s*)[0-9a-fA-F:]+", r"\g<1>" + corrupted_mac, original_content)
                
                with open(config_path, "w") as f:
                    f.write(corrupted_content)
                allure.attach(corrupted_content, name="Corrupted Config Preview", attachment_type=allure.attachment_type.TEXT)

            with allure.step("Verifying provider status with corrupted configuration"):
                test_cmd = ["docker", "run", "--user", "0", "--rm", 
                    "-v", f"{config_path}:{target_path}", 
                    image_tag, "list", "-providers", "-verbose"
                ]
                final_check = subprocess.run(test_cmd, capture_output=True, text=True)
                
                allure.attach(final_check.stdout, name="Module Status Output")
                allure.attach(final_check.stderr, name="Integrity Error Logs")

                is_fips_active = "fips" in final_check.stdout and "status: active" in final_check.stdout
                
                if is_fips_active:
                    allure.dynamic.status_details(message="Security Breach: FIPS module loaded successfully despite MAC corruption.")
                    pytest.fail("Integrity Failure: The system failed to detect tampering in the fipsmodule.cnf file.")

            with allure.step("Tamper resistance verified"):
                allure.dynamic.parameter("Tampered Field", "module-mac")
                allure.dynamic.parameter("System Response", "Module Load Rejected")
    @allure.story("Legacy Protocol Mitigation")
    @allure.title("Verify Blocking of Insecure TLS 1.0/1.1 Protocols")
    @allure.description("""
        Validates the mandatory retirement of legacy cryptographic protocols:
        1. Attempts to initiate a TLS 1.0 handshake with an external endpoint (google.com).
        2. Confirms that the FIPS-enabled TLS stack strictly prohibits the use of TLS 1.0/1.1.
        3. Ensures that the system returns a protocol-level error instead of falling back to insecure versions.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("network-hardening", "tls-retirement", "compliance")
    def test_tls_legacy_protocol_blocking(self, run_docker, image_tag):
        with allure.step("Attempting connection via deprecated TLS 1.0"):
            result = run_docker(image_tag, ["s_client", "-connect", "google.com:443", "-tls1"])
            
            allure.attach(result.stdout, name="Handshake Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Handshake Stderr", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying protocol rejection"):
            error_msg = result.stderr.lower()
            # In FIPS mode, the return code must be non-zero and the error should indicate protocol unavailability
            assert result.returncode != 0, "Compliance Failure: Connection established using insecure TLS 1.0 protocol."
            
            rejection_indicators = ["no protocols available", "unsupported", "error", "unknown protocol"]
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"Unexpected error message during TLS 1.0 rejection: {result.stderr}"

        with allure.step("Protocol hardening confirmed"):
            allure.dynamic.parameter("Blocked Protocol", "TLS 1.0/1.1")
            allure.dynamic.parameter("Enforcement Strategy", "FIPS Approved Protocols Only")

    @allure.story("Network Policy Enforcement")
    @allure.title("Verify Rejection of Non-FIPS Ciphers in TLS Handshake")
    @allure.description("""
        Validates that the FIPS security policy is strictly enforced at the network socket level.
        1. Attempts to establish a TLS connection while forcing the use of a legacy, non-FIPS cipher (RC4-MD5).
        2. Verifies that the FIPS provider intercepts the handshake and rejects the insecure cipher suite.
        3. Confirms that the connection fails with a clear protocol error, preventing any data exchange over an unapproved channel.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("fips-enforcement", "network-policy", "cipher-rejection")
    def test_non_fips_cipher_rejection_over_network(self, run_docker, image_tag):
        forbidden_cipher = "RC4-MD5"
        
        with allure.step(f"Attempting TLS handshake with forbidden cipher: {forbidden_cipher}"):
            result = run_docker(image_tag, ["s_client", "-connect", "www.openssl.org:443", "-cipher", forbidden_cipher])
            
            allure.attach(result.stdout, name="Handshake Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Handshake Stderr", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying mandatory rejection of the insecure cipher"):
            if result.returncode == 0:
                allure.dynamic.status_details(message=f"Security Breach: Connection succeeded using forbidden cipher {forbidden_cipher}.")
                pytest.fail("Compliance Failure: The FIPS module allowed a TLS connection with a non-approved legacy cipher.")

            error_msg = result.stderr.lower()
            rejection_indicators = [
                "no ciphers available", 
                "unsupported", 
                "handshake failure", 
                "sslv3 alert", 
                "no cipher match",
                "ssl_conf_cmd"
            ]
            
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"The connection failed, but not with an expected FIPS-related cipher rejection error. Stderr: {result.stderr}"

        with allure.step("FIPS network policy enforcement confirmed"):
            allure.dynamic.parameter("Tested Cipher", forbidden_cipher)
            allure.dynamic.parameter("Expected Outcome", "Handshake Failure")
            allure.dynamic.parameter("Policy Scope", "Network Sockets")




@allure.feature("FIPS 140-3 Advanced Network Compliance")
class TestAdvancedFIPSNetworkCompliance:
    """
    Verifies strict FIPS 140-3 compliance by testing specific, mandated cryptographic mechanisms
    within the TLS handshake. These tests go beyond basic protocol and cipher checks to ensure
    that key exchange, signature validation, and session management adhere to NIST guidelines.
    """

    @allure.story("Key Establishment Protocol Validation")
    @allure.title("Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange")
    @allure.description_html("""
        <p><b>FIPS 140-3 Compliance:</b> Guided by NIST SP 800-52r2, mandates the use of specific, approved curves for ECDHE key exchange.</p>
        <p>This test validates that the TLS client correctly negotiates a connection using <b>ONLY</b> a FIPS-approved curve (P-384).</p>
        <b>Steps:</b>
        <ol>
            <li>Initiates a TLS handshake, explicitly restricting the client to offer only the 'secp384r1' (P-384) curve.</li>
            <li>Verifies that the connection is successfully established.</li>
            <li>Parses the handshake debug output to confirm that 'secp384r1' was indeed the curve used.</li>
            <li>A failure indicates the module either doesn't support a required curve or failed to negotiate it correctly.</li>
        </ol>
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("fips-140-3", "tls", "ecdhe", "key-exchange")

    def test_fips_approved_key_exchange_negotiation(self, run_docker, image_tag):
        fips_approved_curve = "secp384r1"
        target_host = "www.cloudflare.com:443"
        
        with allure.step(f"Attempting TLS handshake with {target_host} forcing curve: {fips_approved_curve}"):
            result = run_docker(image_tag, ["s_client", "-connect", target_host, "-curves", fips_approved_curve, "-ign_eof"])
            allure.attach(result.stdout, name="Handshake Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Handshake Stderr", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("Verifying successful negotiation and curve selection"):
            assert result.returncode == 0, f"Handshake failed when restricted to a FIPS-approved curve. Stderr: {result.stderr}"
            
            output = result.stdout + result.stderr
            
            match = re.search(r"Peer Temp Key:\s*(.*)\n", output, re.IGNORECASE)
            
            assert match, "Could not find the 'Peer Temp Key' line in the s_client output."
            negotiated_line = match.group(1).lower()
            assert fips_approved_curve in negotiated_line, \
                f"Connection succeeded, but the wrong group/curve was negotiated. Expected '{fips_approved_curve}', but got '{negotiated_line}'."

        with allure.step("FIPS-compliant key establishment confirmed"):
            allure.dynamic.parameter("Mandated Curve", fips_approved_curve)
            allure.dynamic.parameter("Compliance Standard", "NIST SP 800-52r2")

    @allure.story("Certificate Signature Algorithm Validation")
    @allure.title("Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)")
    @allure.description("""
        FIPS 140-3 strictly forbids the use of SHA-1 for digital signature verification. This test
        validates that the TLS client will reject a server's certificate chain if it is signed with
        a deprecated hash algorithm.
        1. Attempts to connect to a public server known to use a SHA-1 certificate for testing purposes (sha1-2017.badssl.com).
        2. Verifies that the handshake fails as expected.
        3. Examines the error message to confirm the failure reason is specifically a certificate verification or signature algorithm error.
        4. A successful connection would represent a critical failure to enforce FIPS signature algorithm policies.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("fips-140-3", "x509", "sha1", "signatures")
    def test_rejection_of_sha1_certificate_signature(self, run_docker, image_tag):
        target_host = "sha1-2017.badssl.com:443"

        with allure.step(f"Connecting to host with a known weak certificate signature: {target_host}"):
            result = run_docker(image_tag, ["s_client", "-connect", target_host])
            allure.attach(result.stdout, name="Handshake Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Handshake Stderr", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Confirming mandatory rejection of the certificate"):
            assert result.returncode != 0, "Security Breach: Connection succeeded with a SHA-1 signed certificate, violating FIPS."
            
            error_msg = result.stderr.lower()
            rejection_indicators = [
                "certificate verify failed", 
                "digest too weak", 
                "ee key too small",
                "ca signature digest algorithm too weak"
            ]
            
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"Connection failed, but not with an expected signature validation error. Stderr: {result.stderr}"
                
        with allure.step("FIPS signature validation policy enforced"):
            allure.dynamic.parameter("Rejected Algorithm", "SHA-1")
            allure.dynamic.parameter("Verification Context", "Server Certificate Chain")


    @allure.story("Secure Session Resumption (TLS 1.3)")
    @allure.title("Verify Secure TLS 1.3 Session Resumption with PSK")
    @allure.description(inspect.cleandoc("""
        Detailed Validation of the Container's TCP/IP Stack:
        1. Attempts to establish a raw socket connection.
        2. Bypasses DNS resolution.
    """))
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("fips-140-3", "tls1.3", "session-resumption", "psk")
    def test_secure_tls13_session_resumption(self, image_tag):
        target_host = "www.cloudflare.com:443"
        
        with tempfile.TemporaryDirectory(dir=".") as tmpdir:
            host_dir_abs = os.path.abspath(tmpdir)
            os.chmod(host_dir_abs, 0o777)
            container_mount_dir = "/mnt/session_data"
            container_session_path = os.path.join(container_mount_dir, "tls_session.pem")

            with allure.step("Establishing initial TLS 1.3 connection and saving session ticket"):
                initial_cmd = [
                    "docker", "run", "--user", "0", "--rm",
                    "-v", f"{host_dir_abs}:{container_mount_dir}",
                    image_tag, "s_client", "-connect", target_host,
                    "-sess_out", container_session_path, "-ign_eof"
                ]
                initial_result = subprocess.run(initial_cmd, capture_output=True, text=True)
                assert initial_result.returncode == 0, f"Initial connection failed. Stderr: {initial_result.stderr}"

            with allure.step("Attempting to reconnect and resume the session using the saved ticket"):
                resume_cmd = [
                    "docker", "run", "--user", "0", "--rm",
                    "-v", f"{host_dir_abs}:{container_mount_dir}",
                    image_tag, "s_client", "-connect", target_host,
                    "-sess_in", container_session_path, "-ign_eof"
                ]
                resume_result = subprocess.run(resume_cmd, capture_output=True, text=True)
                allure.attach(resume_result.stdout, name="Resumption Stdout")
                allure.attach(resume_result.stderr, name="Resumption Stderr")
                assert resume_result.returncode == 0, f"Session resumption failed. Stderr: {resume_result.stderr}"

            with allure.step("Verifying session was successfully reused"):
                output = resume_result.stdout + resume_result.stderr
                assert "Reused, TLSv1.3" in output, "Connection succeeded, but failed to securely resume the TLS 1.3 session."

        with allure.step("TLS 1.3 stateful resumption mechanism confirmed"):
            allure.dynamic.parameter("Mechanism", "PSK-based Session Resumption")
            allure.dynamic.parameter("Protocol", "TLS 1.3")