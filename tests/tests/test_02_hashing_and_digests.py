import pytest
import allure

@allure.feature("Cryptographic Algorithms")
class TestMessageDigests:

    @allure.story("Hash Functions & Message Digests")
    @allure.title("Verify MD5 Algorithm Rejection")
    @allure.description("""
        Validates that the MD5 message digest algorithm is strictly prohibited.
        Any attempt to invoke MD5 via the provider must result in a failure state,
        returning an error indicating that the algorithm is unsupported or fetch failed.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("hashing", "md5", "compliance", "negative-test")
    def test_md5_execution_rejection(self, run_docker, image_tag):
        with allure.step("Attempting to execute MD5 digest calculation"):
            result = run_docker(image_tag, ["dgst", "-md5", "/dev/null"])
            allure.attach(result.stderr, name="Error Output", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying rejection logic"):
            assert result.returncode != 0, "Security Breach: MD5 algorithm execution succeeded in FIPS mode."
            
            error_msg = result.stderr.lower()
            rejection_indicators = ["unsupported", "fetch failed", "properties", "unknown", "invalid"]
            
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"MD5 failed but with an unexpected error message: {result.stderr}"

        with allure.step("Recording compliance metric"):
            allure.dynamic.parameter("Algorithm", "MD5")
            allure.dynamic.parameter("Enforcement", "Strict Rejection")

    @allure.story("Hash Functions & Message Digests")
    @allure.title("Verify SHA-256 Algorithm Availability")
    @allure.description("""
        Confirms that the SHA-256 algorithm (SHA-2 Family) is fully operational.
        This is a blocker requirement as it is the standard hashing algorithm for FIPS 140-3.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("hashing", "sha256", "core-functionality")
    def test_sha256_availability(self, run_docker, image_tag):
        with allure.step("Calculating SHA-256 digest for empty input"):
            result = run_docker(image_tag, ["dgst", "-sha256", "/dev/null"])
            allure.attach(result.stdout, name="Digest Output", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying digest generation integrity"):
            assert result.returncode == 0, f"SHA-256 execution failed. Stderr: {result.stderr}"
            assert "SHA256" in result.stdout or "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" in result.stdout

        with allure.step("Recording availability metric"):
            allure.dynamic.parameter("Algorithm", "SHA-256")
            allure.dynamic.parameter("Status", "Operational")

    @allure.story("Hash Functions & Message Digests")
    @allure.title("Verify SHA-3 Algorithm Availability")
    @allure.description("""
        Validates the availability of the SHA-3 family (NIST SP 800-202).
        Ensures that modern KMAC and SHAKE functions have the necessary underlying primitives.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("hashing", "sha3", "nist-sp-800-202")
    def test_sha3_availability(self, run_docker, image_tag):
        with allure.step("Calculating SHA3-256 digest"):
            result = run_docker(image_tag, ["dgst", "-sha3-256", "/dev/null"])
            allure.attach(result.stdout, name="SHA-3 Output", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying SHA-3 functionality"):
            assert result.returncode == 0, f"SHA-3 execution failed. Stderr: {result.stderr}"
            assert "SHA3-256" in result.stdout

        with allure.step("Recording SHA-3 support"):
            allure.dynamic.parameter("Algorithm", "SHA3-256")
            allure.dynamic.parameter("Standard", "FIPS 202")


    @allure.story("Hash Functions & Message Digests")
    @allure.title("Verify SHAKE XOF Functionality")
    @allure.description("""
        Validates the functionality of SHAKE128 (Extendable Output Function).
        Ensures the algorithm is available and functional within the FIPS boundary.
        Accepts both 'SHAKE128' and 'SHAKE-128' naming conventions.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("hashing", "shake128", "xof", "fips-202")
    def test_shake_xof_functionality(self, run_docker, image_tag):
        with allure.step("Attempting SHAKE128 digest calculation"):
            result = run_docker(image_tag, [
                "dgst", 
                "-propquery", "fips=yes", 
                "-shake128", 
                "/dev/null"
            ])
            
            allure.attach(result.stdout, name="Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Stderr", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying algorithm execution and output format"):
            assert result.returncode == 0, f"SHAKE128 execution failed. Stderr: {result.stderr}"
            
            output_clean = result.stdout.upper().replace("-", "")
            assert "SHAKE128" in output_clean, f"Unexpected output format for SHAKE128. Output: {result.stdout}"

        with allure.step("Recording XOF compliance metrics"):
            allure.dynamic.parameter("Algorithm", "SHAKE128/SHAKE-128")
            allure.dynamic.parameter("Status", "Operational")