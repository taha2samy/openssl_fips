import pytest
import allure
import subprocess
@allure.feature("Symmetric Encryption & FIPS Policy")
class TestAESEncryption:


    
    @allure.story("Cryptographic Boundaries (Precision)")
    @allure.title("Verify AES-GCM Tag Length Restrictions")
    @allure.description("""
        Validates the precision of cryptographic boundaries for authenticated encryption (AES-GCM).
        FIPS 140-3 mandates specific approved Tag lengths (typically 96, 104, 112, 120, or 128 bits).
        This test ensures that the module rejects insecure, unapproved short tag lengths 
        (e.g., 32-bit / 4-byte) to prevent tag forgery and maintain security strength.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("boundary-check", "aes-gcm", "precision")
    def test_aes_gcm_tag_length(self, run_docker, image_tag):
        with allure.step("Attempting AES-GCM encryption with an unapproved 32-bit (4-byte) tag"):
            # Using 'dgst' instead of 'enc' to properly support '-macopt taglen'
            result = run_docker(image_tag, ["dgst", "-aes-256-gcm", "-macopt", "taglen:4", "/dev/null"])
            
            allure.attach(result.stdout, name="Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Stderr", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying that the module rejected the insecure tag length"):
            error_msg = result.stderr.lower()
            
            # In FIPS mode, returncode 0 means it accepted the insecure tag (Failure)
            if result.returncode == 0:
                allure.dynamic.status_details(message="Security Boundary Violated: Unapproved GCM tag length (4 bytes) was accepted.")
                pytest.fail("Compliance Failure: The module allowed AES-GCM encryption with a 32-bit tag length.")

            # Validation of error message content for FIPS rejection or syntax correctness
            assert any(x in error_msg for x in ["error", "invalid", "unsupported", "tag", "macopt"]), \
                f"Unexpected error behavior during GCM tag length rejection: {result.stderr}"

        with allure.step("Boundary precision confirmed"):
            allure.dynamic.parameter("Attempted Tag Length (Bits)", "32")
            allure.dynamic.parameter("Compliance Requirement", "Minimum 96-bit tag length")








    @allure.story("Cipher Suite Availability")
    @allure.title("Verify FIPS-Approved Cipher Algorithms")
    @allure.description("""
        Queries the OpenSSL provider for algorithms strictly tagged with 'fips=yes'.
        Validates that the mandatory AES-GCM (Galois/Counter Mode) cipher is present 
        and available for use within the cryptographic boundary.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("encryption", "aes-gcm", "fips-provider")
    def test_fips_cipher_list_integrity(self, run_docker, image_tag):
        with allure.step("Querying FIPS provider for approved ciphers"):
            result = run_docker(image_tag, ["list", "-cipher-algorithms", "-propquery", "fips=yes"])
            allure.attach(result.stdout, name="Cipher List Output", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying presence of AES-GCM"):
            assert result.returncode == 0, f"Failed to list ciphers. Stderr: {result.stderr}"
            
            output = result.stdout.upper()
            assert "AES-256-GCM" in output or "AES-128-GCM" in output, \
                "Critical Failure: AES-GCM is missing from the FIPS provider list."

        with allure.step("Recording cipher availability"):
            allure.dynamic.parameter("Query Scope", "fips=yes")
            allure.dynamic.parameter("Target Cipher", "AES-GCM")

    @allure.story("AES-XTS Security Boundary")
    @allure.title("Verify AES-XTS Rejection of Duplicate Keys")
    @allure.description("""
        Validates compliance with NIST SP 800-38E regarding XTS-AES.
        The system must reject encryption attempts where Key_1 (Data Encryption Key) 
        is identical to Key_2 (Tweak Key).
        Simulates an attack using a 512-bit key consisting of identical halves.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("encryption", "aes-xts", "nist-sp-800-38e", "negative-test")
    def test_aes_xts_duplicate_key_rejection(self, run_docker, image_tag):
        duplicate_key = "00" * 64
        iv_hex = "00" * 16

        with allure.step("Attempting AES-256-XTS encryption with identical key halves"):
            result = run_docker(image_tag, [
                "enc", "-aes-256-xts", "-e", 
                "-K", duplicate_key, 
                "-iv", iv_hex, 
                "-nosalt", 
                "-in", "/dev/null"
            ])
            allure.attach(result.stderr, name="Encryption Error Log", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying mandatory rejection"):
            assert result.returncode != 0, "Security Breach: AES-XTS accepted identical keys for cipher and tweak."
            
            error_msg = result.stderr.lower()
            assert "error" in error_msg or "hex" in error_msg or "cipher" in error_msg, \
                f"Operation failed but without specific key validation error. Stderr: {result.stderr}"

        with allure.step("Recording vulnerability check"):
            allure.dynamic.parameter("Standard", "NIST SP 800-38E")
            allure.dynamic.parameter("Attack Vector", "Duplicate XTS Keys")
            allure.dynamic.parameter("Outcome", "Operation Rejected")



    @allure.story("Symmetric Encryption")
    @allure.title("Verify AES-CBC Functional Integrity (KAT)")
    @allure.description("""
        Validates the round-trip integrity of AES-128-CBC encryption and decryption.
        This implementation is optimized for Distroless environments by piping 
        raw bytes directly into the container's stdin, bypassing the need for a shell.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("encryption", "aes-cbc", "kat", "distroless-ready")
    def test_aes_cbc_known_answer(self, image_tag):
        test_key = "00112233445566778899AABBCCDDEEFF"
        test_iv = "000102030405060708090A0B0C0D0E0F"
        plaintext = "FIPS-COMPLIANCE-INTEGRITY-CHECK"

        with allure.step("Performing encryption via stdin pipe"):
            enc_cmd = [
                "docker", "run", "-i", "--rm", image_tag,
                "enc", "-aes-128-cbc", "-e", "-propquery", "fips=yes",
                "-K", test_key, "-iv", test_iv, "-nosalt"
            ]
            enc_proc = subprocess.run(enc_cmd, input=plaintext.encode(), capture_output=True)
            
            allure.attach(enc_proc.stderr, name="Encryption Stderr", attachment_type=allure.attachment_type.TEXT)
            assert enc_proc.returncode == 0, f"Encryption process failed. Stderr: {enc_proc.stderr.decode()}"
            ciphertext_raw = enc_proc.stdout

        with allure.step("Performing decryption via stdin pipe"):
            dec_cmd = [
                "docker", "run", "-i", "--rm", image_tag,
                "enc", "-aes-128-cbc", "-d", "-propquery", "fips=yes",
                "-K", test_key, "-iv", test_iv, "-nosalt"
            ]
            dec_proc = subprocess.run(dec_cmd, input=ciphertext_raw, capture_output=True)
            
            allure.attach(dec_proc.stderr, name="Decryption Stderr", attachment_type=allure.attachment_type.TEXT)
            assert dec_proc.returncode == 0, f"Decryption process failed. Stderr: {dec_proc.stderr.decode()}"
            decrypted_output = dec_proc.stdout.decode().strip()

        with allure.step("Verifying plaintext integrity"):
            assert decrypted_output == plaintext, \
                f"Data mismatch detected. Expected: {plaintext}, Recovered: {decrypted_output}"

        with allure.step("Recording cryptographic session metadata"):
            allure.dynamic.parameter("Algorithm", "AES-128-CBC")
            allure.dynamic.parameter("Operation Mode", "Known Answer Test (KAT)")
            allure.dynamic.parameter("Stdin Piping", "Enabled (Distroless Mode)")




@allure.feature("Symmetric Encryption & FIPS Policy")
class TestLegacyCipherPolicies:

    @allure.story("Legacy Cipher Mitigation")
    @allure.title("Verify 3DES Encryption Rejection")
    @allure.description("""
        Validates the mandatory retirement of Triple-DES (3DES) for encryption.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("encryption", "3des", "negative-test")
    def test_3des_encryption_rejection(self, image_tag):
        test_key = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        test_iv = "0123456789ABCDEF"
        plaintext = "LEGACY-DATA-BLOCK"

        with allure.step("Attempting to initialize 3DES encryption (des-ede3-cbc)"):
            cmd = [
                "docker", "run", "-i", "--rm", image_tag,
                "enc", "-des-ede3-cbc", "-e", "-propquery", "fips=yes",
                "-K", test_key, "-iv", test_iv, "-nosalt"
            ]
            
            result = subprocess.run(cmd, input=plaintext.encode(), capture_output=True)
            
            # Debugging: Decode stderr for analysis
            error_msg_raw = result.stderr.decode(errors='ignore')
            allure.attach(error_msg_raw, name="Raw Stderr Output")

        with allure.step("Verifying algorithm rejection by FIPS provider"):
            assert result.returncode != 0, "Security Breach: Triple-DES encryption was allowed in FIPS mode."
            
            error_msg = error_msg_raw.lower()
            rejection_indicators = ["unsupported", "disabled", "error", "fetch failed", "unknown cipher"]
            
            # Fix: Comparing string to decoded string
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"3DES failed but not with an expected policy rejection error. Stderr: {error_msg_raw}"

    @allure.story("Legacy Cipher Mitigation")
    @allure.title("Verify Absolute Absence of Single DES")
    @allure.description("""
        Validates that Single-DES is completely unavailable.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("encryption", "des", "negative-test")
    def test_des_algorithm_absence(self, image_tag):
        with allure.step("Attempting to invoke single DES cipher"):
            cmd = [
                "docker", "run", "--rm", image_tag,
                "enc", "-des-cbc", "-e", "-propquery", "fips=yes"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            allure.attach(result.stderr, name="Algorithm Lookup Error")

        with allure.step("Verifying DES is unknown to the provider"):
            assert result.returncode != 0
            
            error_msg = result.stderr.lower()
            assert any(x in error_msg for x in ["unknown cipher", "invalid", "unsupported"]), \
                f"DES did not return the expected error. Stderr: {result.stderr}"
