# 🛡️ FIPS Compliance Audit Report

> **Generated on:** 2026-02-18 08:33:34 UTC  
> **Status:** ![Status](https://img.shields.io/badge/tests-failed%2012-red)


## 📋 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Build Configuration](#-build-configuration)
3. [Supply Chain & Packages](#-supply-chain--packages)
4. [Test Results Detail](#-test-results-detail)


## 📊 Executive Summary

| Metric | Count | Status |
| :--- | :---: | :--- |
| **Total Tests** | `92` | 🔍 Scoped |
| **Passed** | `80` | ✅ Passing |
| **Failed** | `12` | ❌ Critical |
| **Broken** | `0` | ⚠️ Error |


## 🏗️ Build Configuration

### Core Artifact Specs
| Parameter | Configuration |
| :--- | :--- |
| **FIPS Module** | `3.1.2` |
| **OpenSSL Core** | `3.5.5` |
| **Image Tag** | `ghcr.io/taha2samy/wolfi-openssl-fips` |


### 2. Target Artifacts (Outputs)
| Variant | Full Image Reference |
| :--- | :--- |
| **Standard** | `ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5` |
| **Distroless** | `ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless` |

### 3. Base Image Provenance (Inputs)
| Used For | Source Image Digest |
| :--- | :--- |
| **Standard Build** | `cgr.dev/chainguard/wolfi-base@sha256:b5f4a33fa2fee95dd79535e069bafd60f52085c5786677da5724414374c5194c` |
| **Distroless Build**| `cgr.dev/chainguard/static@sha256:9cef3c6a78264cb7e25923bf1bf7f39476dccbcc993af9f4ffeb191b77a7951e` |



The following key packages were pinned during the build process:

| Package Name | Version |
| :--- | :--- |
| **Build Base** | `1-r9` |
| **Perl** | `5.42.0-r2` |
| **Linux Headers** | `6.19-r0` |
| **Wget** | `1.25.0-r7` |
| **Ca Certificates** | `20251003-r3` |
| **Libstdc Plus Plus** | `15.2.0-r9` |
| **Zlib** | `1.3.1.2-r3` |
| **Tzdata** | `2025c-r0` |
| **Posix Libc Utils** | `2.43-r1` |









### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `203ms` |
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `212ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `2142ms` |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `1413ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `203ms` |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `200ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `211ms` |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `212ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `197ms` |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `203ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `202ms` |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `205ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `222ms` |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `210ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `204ms` |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `207ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `218ms` |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `204ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `413ms` |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `419ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `210ms` |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `216ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `203ms` |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `201ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `218ms` |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `240ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `208ms` |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `212ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `205ms` |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `210ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `209ms` |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `214ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `207ms` |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `208ms` |



#### 🔻 Failure Analysis for tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary


**🔴 Verify Precise 112-bit Security Boundary**
>   
        Validates the exact transition point for HMAC security strength.  
        Ensures that 104-bit keys are rejected and 112-bit keys are accepted   
        under strict FIPS property queries.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:60: in test_hmac_112bit_security_boundary
    assert result_104.returncode != 0, "Compliance Failure: System accepted 104-bit key under FIPS query."
E   AssertionError: Compliance Failure: System accepted 104-bit key under FIPS query.
E   assert 0 != 0
E    +  where 0 = CleanResult(returncode=0, stdout='AF310B4D5EAE49576A38C421DC3B8483E810491E0988BE623AA25C1CE7A91631\n', stderr='').returncode
```
---

**🔴 Verify Precise 112-bit Security Boundary**
>   
        Validates the exact transition point for HMAC security strength.  
        Ensures that 104-bit keys are rejected and 112-bit keys are accepted   
        under strict FIPS property queries.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:60: in test_hmac_112bit_security_boundary
    assert result_104.returncode != 0, "Compliance Failure: System accepted 104-bit key under FIPS query."
E   AssertionError: Compliance Failure: System accepted 104-bit key under FIPS query.
E   assert 0 != 0
E    +  where 0 = CleanResult(returncode=0, stdout='AF310B4D5EAE49576A38C421DC3B8483E810491E0988BE623AA25C1CE7A91631\n', stderr='').returncode
```
---



<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `827ms` |
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `830ms` |



#### 🔻 Failure Analysis for tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive


**🔴 Verify Rejection of Weak Keys across SHA-2 Family**
>   
        Performs an exhaustive sweep across the SHA-2 digest family.  
        Forces the use of the FIPS provider via property query.  
        Validates that a sub-standard 8-bit key is rejected to meet FIPS 140-3 standards.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:39: in test_hmac_sha2_key_length_exhaustive
    assert not failed_variants, f"Compliance Failure: FIPS provider allowed weak 8-bit key for: {failed_variants}"
E   AssertionError: Compliance Failure: FIPS provider allowed weak 8-bit key for: ['SHA224', 'SHA256', 'SHA384', 'SHA512']
E   assert not ['SHA224', 'SHA256', 'SHA384', 'SHA512']
```
---

**🔴 Verify Rejection of Weak Keys across SHA-2 Family**
>   
        Performs an exhaustive sweep across the SHA-2 digest family.  
        Forces the use of the FIPS provider via property query.  
        Validates that a sub-standard 8-bit key is rejected to meet FIPS 140-3 standards.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:39: in test_hmac_sha2_key_length_exhaustive
    assert not failed_variants, f"Compliance Failure: FIPS provider allowed weak 8-bit key for: {failed_variants}"
E   AssertionError: Compliance Failure: FIPS provider allowed weak 8-bit key for: ['SHA224', 'SHA256', 'SHA384', 'SHA512']
E   assert not ['SHA224', 'SHA256', 'SHA384', 'SHA512']
```
---



<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `212ms` |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `204ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `196ms` |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `201ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `426ms` |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `420ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `212ms` |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `209ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `633ms` |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `625ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw


**🔴 Verify ECDH Raw Key Derivation (NIST P-384)**
>   
        Validates the Elliptic Curve Diffie-Hellman (ECDH) key agreement protocol.  
        The test performs a full key exchange simulation:  
        1. Generates two independent EC keys (Alice and Bob) using the P-384 curve.  
        2. Extracts the public peer key.  
        3. Derives a shared secret (Z-value) using Alice's private key and Bob's public key.  
        Ensures the derivation is performed exclusively within the FIPS cryptographic boundary.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:348: in test_ecdh_key_derivation_raw
    assert res_pub.returncode == 0, f"Public key extraction failed: {res_pub.stderr}"
E   AssertionError: Public key extraction failed: Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied
E     
E   assert 1 == 0
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpxdi_z2ue:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
```
---

**🔴 Verify ECDH Raw Key Derivation (NIST P-384)**
>   
        Validates the Elliptic Curve Diffie-Hellman (ECDH) key agreement protocol.  
        The test performs a full key exchange simulation:  
        1. Generates two independent EC keys (Alice and Bob) using the P-384 curve.  
        2. Extracts the public peer key.  
        3. Derives a shared secret (Z-value) using Alice's private key and Bob's public key.  
        Ensures the derivation is performed exclusively within the FIPS cryptographic boundary.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:348: in test_ecdh_key_derivation_raw
    assert res_pub.returncode == 0, f"Public key extraction failed: {res_pub.stderr}"
E   AssertionError: Public key extraction failed: Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied
E     
E   assert 1 == 0
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpf433u4eg:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `417ms` |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `427ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `206ms` |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `210ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1036ms` |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1037ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos


**🔴 Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**
>   
        Validates the isolation of non-approved asymmetric algorithms.  
        Includes a detailed debug phase to list all algorithms claiming FIPS compliance.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:231: in test_strict_block_legacy_curves_and_algos
    assert not failed_blocks, \
E   AssertionError: Security Policy Violation: The following algorithms were PERMITTED in FIPS mode: ['X25519']. Check Debug Logs.
E   assert not ['X25519']
```
---

**🔴 Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**
>   
        Validates the isolation of non-approved asymmetric algorithms.  
        Includes a detailed debug phase to list all algorithms claiming FIPS compliance.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:231: in test_strict_block_legacy_curves_and_algos
    assert not failed_blocks, \
E   AssertionError: Security Policy Violation: The following algorithms were PERMITTED in FIPS mode: ['X25519']. Check Debug Logs.
E   assert not ['X25519']
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `223ms` |
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `206ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `232ms` |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `235ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `212ms` |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `214ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `323ms` |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `1204ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `521ms` |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `465ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature


**🔴 Verify RSA-PSS Signature and Verification Integrity**
>   
        Validates RSA-PSS padding mode compliance.   
        Forces the use of SHA256 explicitly to prevent FIPS from blocking the default SHA1.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:155: in test_rsa_pss_padding_signature
    assert res_sign.returncode == 0, f"Signing Failed: {res_sign.stderr}"
E   AssertionError: Signing Failed: Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied
E     pkeyutl: Error loading key
E     
E   assert 1 == 0
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpk2ce5khu:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
```
---

**🔴 Verify RSA-PSS Signature and Verification Integrity**
>   
        Validates RSA-PSS padding mode compliance.   
        Forces the use of SHA256 explicitly to prevent FIPS from blocking the default SHA1.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:155: in test_rsa_pss_padding_signature
    assert res_sign.returncode == 0, f"Signing Failed: {res_sign.stderr}"
E   AssertionError: Signing Failed: Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied
E     pkeyutl: Error loading key
E     
E   assert 1 == 0
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpacy033eo:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `47ms` |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `50ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `213ms` |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `206ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `210ms` |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `203ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `209ms` |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `201ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `210ms` |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `203ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15282ms` |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15277ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `513ms` |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `437ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15280ms` |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15277ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption


**🔴 Verify Secure TLS 1.3 Session Resumption with PSK**
> Detailed Validation of the Container's TCP/IP Stack:  
1. Attempts to establish a raw socket connection.  
2. Bypasses DNS resolution.

**Trace:**
```text
tests/tests/test_11_network_tls.py:402: in test_secure_tls13_session_resumption
    assert initial_result.returncode == 0, f"Initial connection failed. Stderr: {initial_result.stderr}"
E   AssertionError: Initial connection failed. Stderr: Connecting to 104.16.124.96
E     depth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4
E     verify return:1
E     depth=1 C=US, O=Google Trust Services, CN=WE1
E     verify return:1
E     depth=0 CN=www.cloudflare.com
E     verify return:1
E     Error writing session file /mnt/session_data/tls_session.pem
E     read:errno=13
E     
E   assert 13 == 0
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp19rdkud6:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQG...f d2 d5 7d   .K..s.......?..}\n    0030 - 77 ab 76 f6 8e c5 60 d5-c2 4d bf ee 7d ac d5 03   w.v...`..M..}...\n    0040 - 82 26 97 35 71 71 29 47-18 ef 4b a4 c6 41 37 5f   .&.5qq)G..K..A7_\n    0050 - a5 b5 43 b5 ec 08 7a a0-43 e0 e6 3a 5f 2c f1 75   ..C...z.C..:_,.u\n    0060 - af 11 16 61 a1 78 58 cf-40 60 93 1f 0d a5 37 b3   ...a.xX.@`....7.\n    0070 - 4b 9b ee 37 04 9a 4f c0-2b 89 7c 6f d8 21 1c 6b   K..7..O.+.|o.!.k\n    0080 - f5 c6 d5 32 18 61 99 5a-78 2d 65 05 dd 0c 0c 74   ...2.a.Zx-e....t\n    0090 - d3 53 c3 32 a2 b4 06 f8-6a 0f e5 7b 73 a5 a4 0a   .S.2....j..{s...\n    00a0 - 4b 9f e4 07 e9 1b 48 6f-6b 13 0e 33 26 8a d2 9d   K.....Hok..3&...\n    00b0 - e2 90 a6 ca f1 c8 4d ce-6e 93 82 c6 9c b8 30 16   ......M.n.....0.\n\n    Start Time: 1771403567\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.124.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
```
---

**🔴 Verify Secure TLS 1.3 Session Resumption with PSK**
> Detailed Validation of the Container's TCP/IP Stack:  
1. Attempts to establish a raw socket connection.  
2. Bypasses DNS resolution.

**Trace:**
```text
tests/tests/test_11_network_tls.py:402: in test_secure_tls13_session_resumption
    assert initial_result.returncode == 0, f"Initial connection failed. Stderr: {initial_result.stderr}"
E   AssertionError: Initial connection failed. Stderr: Connecting to 104.16.124.96
E     depth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4
E     verify return:1
E     depth=1 C=US, O=Google Trust Services, CN=WE1
E     verify return:1
E     depth=0 CN=www.cloudflare.com
E     verify return:1
E     Error writing session file /mnt/session_data/tls_session.pem
E     read:errno=13
E     
E   assert 13 == 0
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp7jol0_3v:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQGEwJVUzEeMB...f cb 09 9a   ~...^=.w.B......\n    0030 - b7 f6 6a 09 6c 42 5f 9a-43 31 f1 64 db bf 30 2a   ..j.lB_.C1.d..0*\n    0040 - cf 2c 7b a2 5d 6b ad 88-59 b3 5e e4 a3 8d 57 87   .,{.]k..Y.^...W.\n    0050 - 7d c3 98 96 9e 40 f7 c5-8e 39 2b 3e da 3d 2c ab   }....@...9+>.=,.\n    0060 - 8b 0d 51 8a a2 bb 64 87-8c 5e a6 52 4e d1 26 06   ..Q...d..^.RN.&.\n    0070 - 9e 1c d8 a6 b8 cd 6c a4-22 cd 22 82 c2 65 12 2f   ......l."."..e./\n    0080 - 51 45 42 e0 9b 68 2e f6-b6 a0 ab 56 4d 60 ea 9e   QEB..h.....VM`..\n    0090 - 17 e9 64 52 11 3d 92 0d-fc cc 01 11 29 02 10 77   ..dR.=......)..w\n    00a0 - 5b d9 9e b1 57 58 f1 b6-d8 a5 31 d9 41 09 4c e2   [...WX....1.A.L.\n    00b0 - 03 ad 3b a1 3f 49 2b 3b-20 e8 53 df 1b 9d f6 9d   ..;.?I+; .S.....\n\n    Start Time: 1771403613\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.124.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `221ms` |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `212ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `251ms` |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `258ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `268ms` |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `270ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `390ms` |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `405ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `211ms` |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `212ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `273ms` |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `278ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `229ms` |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `237ms` |




<br>



*Automated by scripts/generate_docs_tests.py*