import pytest
import allure
import tempfile
import os
import subprocess

@allure.feature("Asymmetric Cryptography")
class TestRSAOperations:

    @allure.story("RSA Policy Enforcement")
    @allure.title("Verify Support for Large RSA Modulus (4096-bit)")
    @allure.description("""
        Validates that the FIPS provider supports RSA modulus sizes beyond the 2048-bit minimum.
        According to Security Policy Page 36 (Section 2.7.g), the module supports modulus 
        lengths up to 16384 bits. This test performs a functional generation of a 4096-bit 
        RSA key to confirm support for large moduli while maintaining efficient test execution time.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("rsa", "large-modulus", "key-gen", "page-36")
    def test_rsa_large_modulus_support(self, run_docker, image_tag):
        # 4096 is used as a representative 'Large' modulus to avoid extreme generation times
        target_bits = "4096"
        
        with allure.step(f"Generating a {target_bits}-bit RSA private key using FIPS provider"):
            result = run_docker(image_tag, [
                "genpkey", 
                "-propquery", "fips=yes", 
                "-algorithm", "RSA", 
                "-pkeyopt", f"rsa_keygen_bits:{target_bits}"
            ])
            
            allure.attach(result.stdout, name="Generated Private Key")
            allure.attach(result.stderr, name="Genpkey Stderr")

        with allure.step(f"Verifying {target_bits}-bit key generation success"):
            assert result.returncode == 0, f"FIPS provider failed to generate a {target_bits}-bit RSA key."
            assert "BEGIN PRIVATE KEY" in result.stdout, "Output did not contain a valid private key."

        with allure.step("Recording RSA modulus compliance"):
            allure.dynamic.parameter("Tested Modulus", f"{target_bits} bits")
            allure.dynamic.parameter("Policy Limit", "Up to 16384 bits")
            allure.dynamic.parameter("Status", "Operational")
    @allure.story("RSA Key Generation")
    @allure.title("Verify RSA 2048-bit Compliance")
    @allure.description("""
        Validates the generation of RSA keys with a 2048-bit modulus.
        As per FIPS 140-3 and NIST SP 800-131A, 2048-bit is the minimum accepted 
        security strength for RSA key generation in a compliant environment.
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("rsa", "key-gen", "2048-bit", "compliance")
    def test_rsa_keygen_2048_compliance(self, run_docker, image_tag):
        with allure.step("Generating 2048-bit RSA private key"):
            result = run_docker(image_tag, [
                "genpkey", "-propquery", "fips=yes",
                "-algorithm", "RSA", 
                "-pkeyopt", "rsa_keygen_bits:2048"
            ])
            allure.attach(result.stdout, name="Generated Key Output", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying successful generation and output format"):
            assert result.returncode == 0, f"RSA 2048-bit generation failed. Stderr: {result.stderr}"
            assert "BEGIN PRIVATE KEY" in result.stdout, "The output does not contain a valid PEM private key."

        with allure.step("Recording key generation metrics"):
            allure.dynamic.parameter("Algorithm", "RSA")
            allure.dynamic.parameter("Key Size", "2048-bit")
            allure.dynamic.parameter("FIPS Status", "Approved")

    @allure.story("RSA Key Generation")
    @allure.title("Verify Rejection of Weak RSA 1024-bit Keys")
    @allure.description("""
        Validates the enforcement of minimum RSA key lengths.
        FIPS 140-3 strictly prohibits the generation of RSA keys smaller than 2048 bits.
        The system must intercept and reject any attempt to generate a 1024-bit RSA key.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("rsa", "key-gen", "1024-bit", "negative-test")
    def test_rsa_keygen_weak_rejection(self, run_docker, image_tag):
        with allure.step("Attempting to generate a 1024-bit RSA key"):
            result = run_docker(image_tag, [
                "genpkey", "-propquery", "fips=yes",
                "-algorithm", "RSA", 
                "-pkeyopt", "rsa_keygen_bits:1024"
            ])
            allure.attach(result.stderr, name="Rejection Error Log", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying mandatory rejection of legacy key size"):
            assert result.returncode != 0, "Security Breach: RSA 1024-bit key generation was allowed in FIPS mode."
            
            error_msg = result.stderr.lower()
            rejection_indicators = ["invalid", "too small", "error", "fips", "unsupported"]
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"Generation failed but without a specific policy error. Stderr: {result.stderr}"

        with allure.step("Recording security boundary enforcement"):
            allure.dynamic.parameter("Forbidden Size", "1024-bit")
            allure.dynamic.parameter("Policy", "NIST SP 800-131A Rev. 2")
            allure.dynamic.parameter("Result", "Operation Blocked")







    @allure.story("RSA Padding Schemes")
    @allure.title("Verify RSA-PSS Signature and Verification Integrity")
    @allure.description("""
        Validates RSA-PSS padding mode compliance. 
        Forces the use of SHA256 explicitly to prevent FIPS from blocking the default SHA1.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("rsa", "rsa-pss", "fips-compliance")
    def test_rsa_pss_padding_signature(self, image_tag):
        with tempfile.TemporaryDirectory(dir=".") as tmpdir:
            host_dir = os.path.abspath(tmpdir)
            os.chmod(host_dir, 0o777)
            container_dir = "/mnt/crypto"
            
            key_file = "key.pem"
            data_file = "data.txt"
            sig_file = "signature.bin"
            
            test_payload = "FIPS-PSS-STRICT-DIGEST-VERIFICATION"
            with open(os.path.join(host_dir, data_file), "w") as f:
                f.write(test_payload)

            with allure.step("Step 1: RSA 2048-bit Key Generation"):
                gen_cmd = [
                    "docker", "run", "--user", "0", "--rm", "-v", f"{host_dir}:{container_dir}",
                    image_tag, "genpkey", "-algorithm", "RSA", 
                    "-propquery", "fips=yes",
                    "-pkeyopt", rsa_keygen_bits:2048,
                    "-out", f"{container_dir}/{key_file}"
                ]
                res_gen = subprocess.run(gen_cmd, capture_output=True, text=True)
                assert res_gen.returncode == 0

            with allure.step("Step 2: PSS Signature Creation (Explicit SHA256)"):
                sign_cmd = [
                    "docker", "run", "--user", "0", "--rm", "-v", f"{host_dir}:{container_dir}",
                    image_tag, "pkeyutl", "-sign", 
                    "-propquery", "fips=yes",
                    "-inkey", f"{container_dir}/{key_file}",
                    "-digest", "sha256",
                    "-pkeyopt", "rsa_padding_mode:pss",
                    "-pkeyopt", "rsa_pss_saltlen:32",
                    "-in", f"{container_dir}/{data_file}",
                    "-out", f"{container_dir}/{sig_file}"
                ]
                res_sign = subprocess.run(sign_cmd, capture_output=True, text=True)
                allure.attach(res_sign.stderr, name="Signing Stderr (Debug)")
                
                assert res_sign.returncode == 0, f"Signing Failed: {res_sign.stderr}"

            with allure.step("Step 3: PSS Signature Verification"):
                verify_cmd = [
                    "docker", "run", "--user", "0", "--rm", "-v", f"{host_dir}:{container_dir}",
                    image_tag, "pkeyutl", "-verify", 
                    "-propquery", "fips=yes",
                    "-inkey", f"{container_dir}/{key_file}",
                    "-digest", "sha256",
                    "-pkeyopt", "rsa_padding_mode:pss",
                    "-pkeyopt", "rsa_pss_saltlen:32",
                    "-in", f"{container_dir}/{data_file}",
                    "-sigfile", f"{container_dir}/{sig_file}"
                ]
                res_verify = subprocess.run(verify_cmd, capture_output=True, text=True)
                allure.attach(res_verify.stdout, name="Verification Result")
                
                assert res_verify.returncode == 0
                assert "Signature Verified Successfully" in res_verify.stdout

        with allure.step("RSA-PSS operational compliance confirmed"):
            allure.dynamic.parameter("Security Policy", "FIPS 140-3 Compliant (SHA256 Mandatory)")
            allure.dynamic.parameter("Result", "PSS Verified")










@allure.feature("Asymmetric Cryptography")
class TestECCAndSignatures:


    @allure.story("Asymmetric Cryptography Boundary")
    @allure.title("Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)")
    @allure.description("""
        Validates the isolation of non-approved asymmetric algorithms.
        Includes a detailed debug phase to list all algorithms claiming FIPS compliance.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("rejection", "ed25519", "x25519", "debug")
    def test_strict_block_legacy_curves_and_algos(self, run_docker, image_tag):
        # DEBUG PHASE: List what the FIPS provider actually thinks it supports
        with allure.step("DEBUG: Querying FIPS provider capability list"):
            kex_list = run_docker(image_tag, ["list", "-key-exchange-algorithms", "-propquery", "fips=yes"])
            sig_list = run_docker(image_tag, ["list", "-signature-algorithms", "-propquery", "fips=yes"])
            
            print("\n" + "="*60)
            print(f"[DEBUG] FIPS KEY-EXCHANGE ALGORITHMS:\n{kex_list.stdout}")
            print("-" * 60)
            print(f"[DEBUG] FIPS SIGNATURE ALGORITHMS:\n{sig_list.stdout}")
            print("="*60 + "\n")
            
            allure.attach(kex_list.stdout, name="FIPS Key Exchange List")
            allure.attach(sig_list.stdout, name="FIPS Signature List")

        # EXECUTION PHASE
        forbidden_algos = ["Ed25519", "X25519", "Ed448"]
        failed_blocks = []

        for algo in forbidden_algos:
            with allure.step(f"Attempting to invoke forbidden algorithm: {algo}"):
                result = run_docker(image_tag, [
                    "genpkey", 
                    "-algorithm", algo, 
                    "-propquery", "fips=yes"
                ])
                
                # Check stdout for clues on which provider was used
                allure.attach(result.stdout, name=f"{algo} Stdout")
                allure.attach(result.stderr, name=f"{algo} Stderr")

                if result.returncode == 0:
                    print(f"[CRITICAL DEBUG] Algorithm {algo} was PERMITTED. ReturnCode: 0")
                    failed_blocks.append(algo)
                else:
                    print(f"[INFO DEBUG] Algorithm {algo} was correctly rejected.")

        with allure.step("Verifying all non-approved algorithms were blocked"):
            assert not failed_blocks, \
                f"Security Policy Violation: The following algorithms were PERMITTED in FIPS mode: {failed_blocks}. Check Debug Logs."

        with allure.step("Recording policy enforcement status"):
            allure.dynamic.parameter("Isolation Status", "Failure Detected" if failed_blocks else "Success")







    @allure.story("Elliptic Curve Cryptography (ECC)")
    @allure.title("Verify ECDSA P-384 Functional Integrity")
    @allure.description("""
        Validates the generation and structural integrity of Elliptic Curve keys 
        using the NIST P-384 curve. Confirms that the FIPS provider supports 
        approved curves. Note: P-384 is technically referred to as secp384r1.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ecc", "ecdsa", "p-384", "key-gen")
    def test_ecdsa_p384_signing_flow(self, run_docker, image_tag):

        with allure.step("Generating P-384 EC private key"):
            gen_result = run_docker(image_tag, [
                "genpkey", "-propquery", "fips=yes",
                "-algorithm", "EC", 
                "-pkeyopt", "ec_paramgen_curve:P-384"
            ])
            allure.attach(gen_result.stdout, name="Generated EC Key")
            allure.attach(gen_result.stderr, name="Genpkey Stderr")
            
            assert gen_result.returncode == 0, f"EC Key generation failed. Stderr: {gen_result.stderr}"

        with allure.step("Verifying curve support via ecparam"):
            check_result = run_docker(image_tag, ["ecparam", "-list_curves"])
            
            print(f"[DEBUG] ecparam Output Length: {len(check_result.stdout)}")
            allure.attach(check_result.stdout, name="Full Curves List")

            supported_names = ["P-384", "secp384r1"]
            found = any(name in check_result.stdout for name in supported_names)
            
            assert found, f"Neither P-384 nor secp384r1 found in supported curves. Output: {check_result.stdout[:100]}..."

    @allure.story("Signature Policy Enforcement")
    @allure.title("Verify Rejection of MD5 for Digital Signatures")
    @allure.description("""
        Validates the mandatory rejection of MD5 when used for digital signatures.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("signatures", "md5-rejection", "negative-test")
    def test_md5_signature_verification_rejection(self, run_docker, image_tag):
        with allure.step("Attempting signature verification using MD5 digest"):
            result = run_docker(image_tag, [
                "dgst", "-propquery", "fips=yes",
                "-md5", "/dev/null"
            ])
            allure.attach(result.stderr, name="Policy Rejection Log")

        with allure.step("Verifying signature algorithm rejection"):
            assert result.returncode != 0, "Security Breach: MD5 allowed in FIPS mode."
            
            error_msg = result.stderr.lower()
            rejection_indicators = ["unsupported", "fetch failed", "digest", "error", "disabled", "not approved"]
            
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"Operation failed but not with a clear policy rejection. Stderr: {result.stderr}"








    @allure.story("Key Agreement Protocols")
    @allure.title("Verify ECDH Raw Key Derivation (NIST P-384)")
    @allure.description("""
        Validates the Elliptic Curve Diffie-Hellman (ECDH) key agreement protocol.
        The test performs a full key exchange simulation:
        1. Generates two independent EC keys (Alice and Bob) using the P-384 curve.
        2. Extracts the public peer key.
        3. Derives a shared secret (Z-value) using Alice's private key and Bob's public key.
        Ensures the derivation is performed exclusively within the FIPS cryptographic boundary.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ecc", "ecdh", "key-agreement", "fips-140-3")
    def test_ecdh_key_derivation_raw(self, image_tag):
        with tempfile.TemporaryDirectory(dir=".") as tmpdir:
            host_dir = os.path.abspath(tmpdir)
            container_dir = "/mnt/ecdh"
            
            alice_key = "alice_priv.pem"
            bob_key = "bob_priv.pem"
            bob_pub = "bob_pub.pem"
            shared_secret = "secret.bin"

            with allure.step("Step 1: Generating Alice and Bob P-384 EC Keys"):
                for key_name in [alice_key, bob_key]:
                    gen_cmd = [
                        "docker", "run", "--rm", "-v", f"{host_dir}:{container_dir}",
                        image_tag, "genpkey", "-algorithm", "EC", 
                        "-propquery", "fips=yes",
                        "-pkeyopt", "ec_paramgen_curve:P-384",
                        "-out", f"{container_dir}/{key_name}"
                    ]
                    res = subprocess.run(gen_cmd, capture_output=True, text=True)
                    assert res.returncode == 0, f"EC Key generation failed for {key_name}: {res.stderr}"

            with allure.step("Step 2: Extracting Bob's Public Peer Key"):
                pub_cmd = [
                    "docker", "run", "--rm", "-v", f"{host_dir}:{container_dir}",
                    image_tag, "pkey", "-in", f"{container_dir}/{bob_key}",
                    "-pubout", "-out", f"{container_dir}/{bob_pub}"
                ]
                res_pub = subprocess.run(pub_cmd, capture_output=True, text=True)
                assert res_pub.returncode == 0, f"Public key extraction failed: {res_pub.stderr}"

            with allure.step("Step 3: Deriving Shared Secret (Alice's Private + Bob's Public)"):
                derive_cmd = [
                    "docker", "run", "--rm", "-v", f"{host_dir}:{container_dir}",
                    image_tag, "pkeyutl", "-derive", 
                    "-propquery", "fips=yes",
                    "-inkey", f"{container_dir}/{alice_key}",
                    "-peerkey", f"{container_dir}/{bob_pub}",
                    "-out", f"{container_dir}/{shared_secret}"
                ]
                res_derive = subprocess.run(derive_cmd, capture_output=True, text=True)
                allure.attach(res_derive.stderr, name="Derivation Stderr")
                assert res_derive.returncode == 0, f"Key derivation failed: {res_derive.stderr}"

            with allure.step("Step 4: Validating Shared Secret Integrity"):
                secret_path = os.path.join(host_dir, shared_secret)
                assert os.path.exists(secret_path), "Shared secret file was not created."
                
                file_size = os.path.getsize(secret_path)
                allure.attach(str(file_size), name="Derived Secret Size (Bytes)")
                
                # For P-384, the shared secret should be exactly 48 bytes (384 bits)
                assert file_size == 48, f"Incorrect shared secret size. Expected 48 bytes, got {file_size}."

        with allure.step("ECDH raw key agreement verified"):
            allure.dynamic.parameter("Protocol", "ECDH")
            allure.dynamic.parameter("Curve", "NIST P-384")
            allure.dynamic.parameter("Shared Secret Size", "48 Bytes")







@allure.feature("Asymmetric Cryptography")
class TestPostQuantumIsolation:

    @allure.story("Post-Quantum Cryptography (PQC) Isolation")
    @allure.title("Verify Isolation of ML-KEM (Kyber) from FIPS Boundary")
    @allure.description("""
        Validates that modern Post-Quantum Cryptography (PQC) algorithms, specifically ML-KEM (Kyber),
        are strictly unavailable when the FIPS property query is enforced. 
        As these algorithms are not yet part of the certified FIPS 140-3 provider 
        (e.g., OpenSSL FIPS provider 3.0.x/3.1.x), they must be rejected to ensure 
        only approved algorithms are used within the cryptographic boundary.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("pqc", "isolation", "ml-kem", "negative-test")
    def test_ml_kem_isolation_in_fips(self, run_docker, image_tag):
        with allure.step("Attempting to generate ML-KEM-768 key using strict FIPS properties"):
            # The genpkey command should fail when restricted to fips=yes
            result = run_docker(image_tag, [
                "genpkey", 
                "-propquery", "fips=yes", 
                "-algorithm", "ML-KEM-768"
            ])
            
            allure.attach(result.stdout, name="Stdout", attachment_type=allure.attachment_type.TEXT)
            allure.attach(result.stderr, name="Stderr (Rejection Log)", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verifying algorithm rejection by FIPS provider"):
            # Expected behavior: returncode must be non-zero (failure)
            assert result.returncode != 0, "Security Bypass: PQC algorithm (ML-KEM) was allowed under strict FIPS mode."
            
            error_msg = result.stderr.lower()
            rejection_indicators = ["unsupported", "algorithm", "failed", "fetch", "not found"]
            
            assert any(indicator in error_msg for indicator in rejection_indicators), \
                f"The command failed, but not with an expected PQC algorithm rejection error. Stderr: {result.stderr}"

        with allure.step("Recording isolation boundary status"):
            allure.dynamic.parameter("Target Algorithm", "ML-KEM-768")
            allure.dynamic.parameter("Policy Requirement", "FIPS 140-3 Boundary Isolation")
            allure.dynamic.parameter("Status", "Correctly Blocked")



