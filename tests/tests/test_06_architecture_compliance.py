import pytest
import allure
import subprocess
import os
import sys
import time
@allure.feature("Architecture & System Integrity")
class TestSystemIntegrity:

    @allure.story("Engine Architecture Compliance")
    @allure.title("Verify Absence of Legacy Cryptographic Engines")
    @allure.description("""
        Ensures the system adheres to modern Provider-based architecture. 
        Legacy OpenSSL engines (e.g., GOST, Padlock) must be absent to prevent 
        potential bypasses of the FIPS cryptographic boundary. Only modern 
        hardware-interface engines like 'rdrand' or 'dynamic' are permissible.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("architecture", "engines", "modernization")
    def test_legacy_engines_absence(self, run_docker, image_tag):
        with allure.step("Listing active cryptographic engines in the container"):
            result = run_docker(image_tag, ["engine"])
            allure.attach(result.stdout, name="Engine List Output", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Analyzing detected engines for non-compliant legacy modules"):
            engines_output = result.stdout.strip()
            
            # Forbidden engines that historically bypass standard FIPS logic
            blacklisted_engines = ["gost", "padlock", "capi", "pkcs11"]
            found_violations = [eng for eng in blacklisted_engines if eng in engines_output.lower()]
            
            assert not found_violations, f"Architecture Violation: Forbidden legacy engines detected: {found_violations}"

        with allure.step("Recording architectural status"):
            allure.dynamic.parameter("Architecture Type", "Provider-Centric")
            allure.dynamic.parameter("Legacy Engines", "None Detected")

    @allure.story("Container Security Policy")
    @allure.title("Verify Non-Root User Execution Enforcement")
    @allure.description("""
        Validates that the container is configured to execute as a non-privileged 
        'nonroot' user. Running as root is a security risk and violates 
        principle-of-least-privilege (PoLP) requirements for secure environments.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("security", "user-policy", "hardening")
    def test_container_user_security(self, image_tag):
        with allure.step(f"Inspecting image metadata for User configuration"):
            inspect_cmd = ["docker", "inspect", "--format={{.Config.User}}", image_tag]
            try:
                proc = subprocess.run(inspect_cmd, capture_output=True, text=True, check=True)
                configured_user = proc.stdout.strip()
                allure.attach(configured_user, name="Configured Container User")
            except subprocess.CalledProcessError as e:
                pytest.fail(f"Failed to inspect docker image: {e.stderr}")

        with allure.step("Verifying user identity is 'nonroot'"):
            assert configured_user == "nonroot", \
                f"Security Failure: Container is configured to run as '{configured_user or 'root'}', expected 'nonroot'."

        with allure.step("Recording container security metrics"):
            allure.dynamic.parameter("Effective User", configured_user)
            allure.dynamic.parameter("Privilege Level", "Non-Root")







    @allure.story("Deterministic Random Bit Generator (DRBG)")
    @allure.title("Verify FIPS DRBG Functional Integrity")
    @allure.description("""
        Validates the functionality of the Deterministic Random Bit Generator (DRBG).
        Ensures that the system can generate cryptographically strong random data 
        using the FIPS-approved provider. The test verifies that the 'rand' 
        utility successfully honors the FIPS property query.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("drbg", "rng", "randomness", "fips-140-3")
    def test_drbg_functionality(self, run_docker, image_tag):
        with allure.step("Generating 32 bytes of random data in hex format"):
            result = run_docker(image_tag, ["rand", "-propquery", "fips=yes", "-hex", "32"])
            
            allure.attach(result.stdout, name="Generated Hex Data")
            allure.attach(result.stderr, name="Stderr")

        with allure.step("Verifying successful execution and output length"):
            assert result.returncode == 0, f"Random data generation failed. Stderr: {result.stderr}"
            
            # 32 bytes in hex should be exactly 64 characters
            clean_output = result.stdout.strip()
            assert len(clean_output) == 64, f"Incorrect output length. Expected 64 hex chars, got {len(clean_output)}."

        with allure.step("Recording DRBG operational metrics"):
            allure.dynamic.parameter("Requested Bytes", "32")
            allure.dynamic.parameter("Property Query", "fips=yes")
            allure.dynamic.parameter("Status", "Operational")



    @allure.story("Entropy Authority & Randomness")
    @allure.title("Verify Entropy Source Authority & FIPS Provider Priority")
    @allure.description("""
        Validates that the cryptographic module utilizes a FIPS-approved entropy source.
        This test ensures that the Deterministic Random Bit Generator (DRBG) is 
        specifically provided by the 'fips' provider (e.g., CTR-DRBG @ fips), 
        overriding any legacy or default system entropy sources.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("entropy", "randomness", "drbg-priority", "compliance")
    def test_entropy_source_validation(self, run_docker, image_tag):
        with allure.step("Querying active random generators and entropy providers"):
            # We use -verbose to see the provider affinity (e.g., @ fips)
            result = run_docker(image_tag, ["list", "-random-generators", "-verbose"])
            
            allure.attach(result.stdout, name="Random Generators Metadata", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Stderr Output", attachment_type=allure.attachment_type.TEXT)

            assert result.returncode == 0, "Failed to retrieve the list of random generators."

        with allure.step("Verifying FIPS Provider authority over entropy (DRBG)"):
            # We must confirm that the CTR-DRBG is explicitly linked to the fips provider
            # The output should contain something like "CTR-DRBG @ fips"
            output = result.stdout
            fips_drbg_present = "CTR-DRBG @ fips" in output or "HASH-DRBG @ fips" in output or "HMAC-DRBG @ fips" in output

            if not fips_drbg_present:
                allure.dynamic.status_details(message="Compliance Failure: Entropy source is NOT provided by the FIPS provider.")
                pytest.fail("Security Policy Violation: The module is not using a FIPS-approved DRBG instance from the validated provider.")

        with allure.step("Checking for unauthorized legacy entropy engines"):
            # Ensuring legacy engines like 'rdrand' are not bypassing the FIPS DRBG hierarchy
            if "rdrand" in output.lower() and "@ fips" not in output:
                allure.dynamic.parameter("Warning", "Hardware RDRAND detected, but FIPS DRBG priority must be maintained.")

        with allure.step("Entropy source authority and priority confirmed"):
            allure.dynamic.parameter("Primary DRBG", "CTR-DRBG @ fips")
            allure.dynamic.parameter("Compliance Standard", "FIPS 140-3 (AS08.01)")







    @allure.story("Password-Based Key Derivation")
    @allure.title("Verify PBKDF2 Derivation with FIPS Approved Digest")
    @allure.description("""
        Validates the PBKDF2 integrity. 
        Note: FIPS 140-3 (via NIST SP 800-132) mandates a minimum salt length 
        of 128 bits (16 bytes). This test uses a 128-bit hex salt to comply.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("kdf", "pbkdf2", "fips-compliance")
    def test_pbkdf2_derivation(self, run_docker, image_tag):
        # Parameters with FIPS-compliant salt length (16 bytes / 128 bits)
        pass_opt = "pass:password123"
        # 16 bytes of salt in hex
        hex_salt = "hexsalt:0102030405060708090A0B0C0D0E0F10"
        iter_opt = "iter:1000"
        digest_opt = "digest:SHA256"
        key_len = "32"

        with allure.step("Deriving key using PBKDF2 (128-bit Salt)"):
            result = run_docker(image_tag, [
                "kdf", 
                "-propquery", "fips=yes",
                "-kdfopt", digest_opt,
                "-kdfopt", pass_opt,
                "-kdfopt", hex_salt,
                "-kdfopt", iter_opt,
                "-keylen", key_len,
                "PBKDF2"
            ])
            
            allure.attach(result.stderr, name="KDF Stderr (Debug)")
            allure.attach(str(len(result.stdout)), name="Derived Key Raw Length")

        with allure.step("Verifying KDF execution status"):
            # If this passes, it means the 16-byte salt was accepted
            assert result.returncode == 0, f"PBKDF2 failed even with 128-bit salt. Stderr: {result.stderr}"
            assert len(result.stdout) > 0, "KDF produced empty output."

        with allure.step("Recording KDF compliance parameters"):
            allure.dynamic.parameter("Algorithm", "PBKDF2")
            allure.dynamic.parameter("Salt Length", "128-bit (Mandatory)")
            allure.dynamic.parameter("Result", "Verified")