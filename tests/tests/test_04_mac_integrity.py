import pytest
import allure


import pytest
import allure

@allure.feature("Message Authentication Codes (MAC)")
class TestHMACBoundaries:

    @allure.story("HMAC Key Strength Enforcement")
    @allure.title("Verify Rejection of Weak Keys across SHA-2 Family")
    @allure.description("""
        Performs an exhaustive sweep across the SHA-2 digest family.
        Forces the use of the FIPS provider via property query.
        Validates that a sub-standard 8-bit key is rejected to meet FIPS 140-3 standards.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("hmac", "sha2", "key-length", "strict-fips")
    def test_hmac_sha2_key_length_exhaustive(self, run_docker, image_tag):
        sha2_variants = ["SHA224", "SHA256", "SHA384", "SHA512"]
        failed_variants = []

        for variant in sha2_variants:
            with allure.step(f"Testing HMAC-{variant} with 8-bit key (Strict FIPS)"):
                # أضفنا -propquery fips=yes لإجبار النظام على استخدام معايير FIPS فقط
                result = run_docker(image_tag, [
                    "mac", "-propquery", "fips=yes", 
                    "-digest", variant, 
                    "-macopt", "hexkey:01", "HMAC"
                ])
                
                if result.returncode == 0:
                    failed_variants.append(variant)
                
                allure.attach(result.stderr, name=f"{variant} Error Log")

        with allure.step("Analyzing sweep results"):
            assert not failed_variants, f"Compliance Failure: FIPS provider allowed weak 8-bit key for: {failed_variants}"

    @allure.story("HMAC Key Strength Enforcement")
    @allure.title("Verify Precise 112-bit Security Boundary")
    @allure.description("""
        Validates the exact transition point for HMAC security strength.
        Ensures that 104-bit keys are rejected and 112-bit keys are accepted 
        under strict FIPS property queries.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("hmac", "nist-threshold", "boundary-testing")
    def test_hmac_112bit_security_boundary(self, run_docker, image_tag):
        key_104_bit = "0102030405060708090A0B0C0D"
        key_112_bit = "0102030405060708090A0B0C0D0E"

        with allure.step("Testing sub-threshold key (104-bit) with FIPS query"):
            result_104 = run_docker(image_tag, [
                "mac", "-propquery", "fips=yes", 
                "-digest", "SHA256", 
                "-macopt", f"hexkey:{key_104_bit}", "HMAC"
            ])
            assert result_104.returncode != 0, "Compliance Failure: System accepted 104-bit key under FIPS query."

        with allure.step("Testing minimum compliant key (112-bit) with FIPS query"):
            result_112 = run_docker(image_tag, [
                "mac", "-propquery", "fips=yes", 
                "-digest", "SHA256", 
                "-macopt", f"hexkey:{key_112_bit}", "HMAC"
            ])
            assert result_112.returncode == 0, f"Functional Failure: 112-bit key rejected. Stderr: {result_112.stderr}"

@allure.feature("Message Authentication Codes (MAC)")
class TestModernMACs:

    @allure.story("MAC Policy Consistency")
    @allure.title("Verify CMAC-AES Key Strength Enforcement")
    @allure.description("""
        Validates CMAC-AES key length enforcement using strict FIPS property queries.
        A 64-bit key must be rejected as it is invalid for AES.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("mac", "cmac", "aes-policy")
    def test_cmac_aes_key_policy(self, run_docker, image_tag):
        invalid_key = "0102030405060708"
        
        with allure.step("Attempting CMAC-AES with 64-bit key (Strict FIPS)"):
            result = run_docker(image_tag, [
                "mac", "-propquery", "fips=yes", 
                "-cipher", "AES-128-CBC", 
                "-macopt", f"hexkey:{invalid_key}", "CMAC"
            ])

        with allure.step("Verifying rejection"):
            assert result.returncode != 0, "Compliance Failure: CMAC accepted invalid 64-bit key under FIPS query."

    @allure.story("Modern MAC Enforcement")
    @allure.title("Verify KMAC-SHA3 Security Strength")
    @allure.description("""
        Validates KMAC-128 security strength enforcement.
        Rejects keys below the 112-bit threshold in FIPS mode.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("mac", "kmac", "sha3")
    def test_kmac_sha3_strength(self, run_docker, image_tag):
        weak_key = "01020304"
        
        with allure.step("Attempting KMAC-128 with 32-bit key (Strict FIPS)"):
            result = run_docker(image_tag, [
                "mac", "-propquery", "fips=yes", 
                "-digest", "KMAC128", 
                "-macopt", f"hexkey:{weak_key}", "KMAC"
            ])

        with allure.step("Verifying rejection"):
            assert result.returncode != 0, "Compliance Failure: KMAC accepted weak 32-bit key under FIPS query."            
@allure.feature("Message Authentication Codes (MAC)")
class TestModernMACs:

    @allure.story("MAC Policy Consistency")
    @allure.title("Verify CMAC-AES Key Strength Enforcement")
    @allure.description("""
        Validates the enforcement of cryptographic strength for Block Cipher-based MACs (CMAC).
        The system must reject CMAC-AES operations if the provided key does not meet 
        the mandatory AES bit-length requirements (128, 192, or 256 bits).
        Tests using an invalid 64-bit (8-byte) key.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("mac", "cmac", "aes-policy", "key-validation")
    def test_cmac_aes_key_policy(self, run_docker, image_tag):
        invalid_key = "0102030405060708"
        
        with allure.step("Attempting CMAC-AES with 64-bit key"):
            result = run_docker(image_tag, [
                "mac", "-cipher", "AES-128-CBC", 
                "-macopt", f"hexkey:{invalid_key}", "CMAC"
            ])
            allure.attach(result.stderr, name="CMAC Rejection Log", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying mandatory rejection of invalid key length"):
            assert result.returncode != 0, "Compliance Failure: CMAC accepted an invalid 64-bit AES key."

        with allure.step("Recording CMAC policy metrics"):
            allure.dynamic.parameter("Cipher", "AES-128-CBC")
            allure.dynamic.parameter("Tested Key Length", "64-bit")
            allure.dynamic.parameter("Outcome", "Strictly Rejected")

    @allure.story("Modern MAC Enforcement")
    @allure.title("Verify KMAC-SHA3 Security Strength")
    @allure.description("""
        Validates the security policy for Keccak-based Message Authentication Codes (KMAC).
        In accordance with NIST SP 800-185, KMAC must enforce a minimum security strength.
        This test ensures that the FIPS provider rejects KMAC-128 operations 
        using a weak sub-112 bit (32-bit) key.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("mac", "kmac", "sha3", "nist-sp-800-185")
    def test_kmac_sha3_strength(self, run_docker, image_tag):
        weak_key = "01020304"
        
        with allure.step("Attempting KMAC-128 with 32-bit key"):
            result = run_docker(image_tag, [
                "mac", "-digest", "KMAC128", 
                "-macopt", f"hexkey:{weak_key}", "KMAC"
            ])
            allure.attach(result.stderr, name="KMAC Error Log", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying rejection of weak SHA3-based MAC key"):
            assert result.returncode != 0, "Compliance Failure: KMAC accepted a weak 32-bit key."

        with allure.step("Recording KMAC compliance data"):
            allure.dynamic.parameter("Algorithm", "KMAC-128")
            allure.dynamic.parameter("Standard", "NIST SP 800-185")
            allure.dynamic.parameter("Outcome", "Policy Enforced")




    @allure.story("NIST SP 800-108 KDF Enforcement")
    @allure.title("Verify SP 800-108 Counter Mode KDF Integrity")
    @allure.description("""
        Validates KBKDF in Counter Mode. 
        Note: KBKDF requires an explicit MAC algorithm (HMAC or CMAC).
        This test uses HMAC-SHA256 as the underlying PRF.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("kdf", "kbkdf", "counter-mode", "debug")
    def test_sp800_108_counter_kdf(self, run_docker, image_tag):
        # Step 1: Debug - Check kdf help if needed
        with allure.step("Debugging: Checking KDF tool help"):
            help_res = run_docker(image_tag, ["kdf", "-help"])
            allure.attach(help_res.stderr, name="KDF Help Output")

        with allure.step("Executing KBKDF Counter Mode (HMAC-SHA256)"):
            # Correct parameters: must specify mac:HMAC and digest:SHA256
            result = run_docker(image_tag, [
                "kdf", 
                "-propquery", "fips=yes",
                "-kdfopt", "mac:HMAC",
                "-kdfopt", "digest:SHA256", 
                "-kdfopt", "hexkey:0102030405060708090A0B0C0D0E0F10", 
                "-kdfopt", "mode:COUNTER",
                "-keylen", "16", 
                "KBKDF"
            ])
            
            allure.attach(result.stdout, name="Derived Key Raw")
            allure.attach(result.stderr, name="Stderr Log")

        with allure.step("Verifying successful execution"):
            assert result.returncode == 0, f"KBKDF Counter Mode failed. Stderr: {result.stderr}"
            assert len(result.stdout) > 0

    @allure.story("NIST SP 800-108 KDF Enforcement")
    @allure.title("Verify SP 800-108 Feedback Mode KDF Integrity")
    @allure.description("""
        Validates KBKDF in Feedback Mode using HMAC-SHA256 as the PRF.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("kdf", "kbkdf", "feedback-mode")
    def test_sp800_108_feedback_kdf(self, run_docker, image_tag):
        with allure.step("Executing KBKDF Feedback Mode (HMAC-SHA256)"):
            result = run_docker(image_tag, [
                "kdf", 
                "-propquery", "fips=yes",
                "-kdfopt", "mac:HMAC",
                "-kdfopt", "digest:SHA256", 
                "-kdfopt", "hexkey:0102030405060708090A0B0C0D0E0F10", 
                "-kdfopt", "mode:FEEDBACK",
                "-keylen", "16", 
                "KBKDF"
            ])
            
            allure.attach(result.stdout, name="Derived Key Raw")
            allure.attach(result.stderr, name="Stderr Log")

        with allure.step("Verifying successful execution"):
            assert result.returncode == 0, f"KBKDF Feedback Mode failed. Stderr: {result.stderr}"
            assert len(result.stdout) > 0