# 🛡️ FIPS Compliance Audit Report

> **Generated on:** 2026-02-18 08:23:43 UTC  
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
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `233ms` |
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `244ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `1433ms` |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `860ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `235ms` |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `238ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `239ms` |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `240ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `240ms` |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `247ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `240ms` |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `236ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `237ms` |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `238ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `235ms` |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `239ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `233ms` |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `250ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `478ms` |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `482ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `236ms` |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `242ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `235ms` |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `239ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `243ms` |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `246ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `244ms` |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `240ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `238ms` |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `249ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `240ms` |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `256ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `242ms` |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `243ms` |



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
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `953ms` |
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `951ms` |



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
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `239ms` |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `247ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `232ms` |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `238ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `474ms` |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `469ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `239ms` |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `239ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `724ms` |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `737ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmptyfnvq0a:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpvgkw9ys2:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `483ms` |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `494ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `238ms` |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `244ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1205ms` |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1224ms` |



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
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `235ms` |
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `243ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `307ms` |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `293ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `243ms` |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `244ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `495ms` |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `455ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `534ms` |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `584ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp7w4p1vsn:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp021_doul:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `51ms` |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `58ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `234ms` |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `236ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `237ms` |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `249ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `246ms` |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `243ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `237ms` |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `238ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15263ms` |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15270ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `324ms` |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `342ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15272ms` |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15259ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption


**🔴 Verify Secure TLS 1.3 Session Resumption with PSK**
> Detailed Validation of the Container's TCP/IP Stack:  
1. Attempts to establish a raw socket connection.  
2. Bypasses DNS resolution.

**Trace:**
```text
tests/tests/test_11_network_tls.py:402: in test_secure_tls13_session_resumption
    assert initial_result.returncode == 0, f"Initial connection failed. Stderr: {initial_result.stderr}"
E   AssertionError: Initial connection failed. Stderr: Connecting to 104.16.123.96
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
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpyb1hduc1:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQG...7 1c 15 16   ...;*H...v.F....\n    0030 - 7e 8f 89 2a bb 9f 98 b2-69 50 08 1e 6a e4 36 b9   ~..*....iP..j.6.\n    0040 - b4 a0 e1 63 6e 61 40 72-e3 3d 74 6c e7 68 94 64   ...cna@r.=tl.h.d\n    0050 - fd 43 b1 62 ad fe 44 47-d0 1d 06 c1 b7 a8 8d 7b   .C.b..DG.......{\n    0060 - fb bc 66 7c f9 72 55 c2-88 4e 3e 4c 9e e5 a3 2a   ..f|.rU..N>L...*\n    0070 - 80 70 ec 97 59 90 15 e6-2d 46 8b dc c7 40 8e e3   .p..Y...-F...@..\n    0080 - 11 b0 5a 2a b8 8e d1 1b-97 14 ea 43 20 67 54 7a   ..Z*.......C gTz\n    0090 - 6f f0 38 3e e6 35 f0 4e-4c c2 2e 6a 5f e2 df 9e   o.8>.5.NL..j_...\n    00a0 - 03 00 b3 ee d0 1c 93 52-2e a4 59 e4 e9 02 af fb   .......R..Y.....\n    00b0 - 83 47 4d 8d ac c0 3a b6-57 7e ca 71 10 8a d6 3a   .GM...:.W~.q...:\n\n    Start Time: 1771402976\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.123.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
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
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpielpwct_:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQGEwJVUzEeMB... 69 28 cc   ....Z%..V....i(.\n    0030 - 79 c5 0c 66 25 bc f5 2d-d3 7e 45 79 ef ee 90 35   y..f%..-.~Ey...5\n    0040 - ad 90 f2 55 2f 83 82 9d-35 7a 80 ed 37 eb 1a a2   ...U/...5z..7...\n    0050 - 05 67 56 8e 9d 18 8b 51-94 75 e3 21 99 98 07 9e   .gV....Q.u.!....\n    0060 - 8a 1e d4 85 2d 88 11 17-0a 0b 46 82 af e9 32 da   ....-.....F...2.\n    0070 - 5c 30 eb f4 24 43 b6 e9-f5 63 24 5a 85 7c c9 fe   \\0..$C...c$Z.|..\n    0080 - ff bb 7c 0d ef da 8e 77-c3 12 ef 50 1f 03 f9 7f   ..|....w...P....\n    0090 - 96 bb 07 36 58 56 cd 53-84 8b 50 4d 8d 15 b5 35   ...6XV.S..PM...5\n    00a0 - f4 44 e5 0e aa 82 c3 0f-90 ee 22 c9 88 da 66 b4   .D........"...f.\n    00b0 - d6 b1 9f 9b 61 7f d1 51-d4 22 85 03 1c 58 b0 8f   ....a..Q."...X..\n\n    Start Time: 1771403022\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.124.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `248ms` |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `256ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `272ms` |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `267ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `272ms` |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `268ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `464ms` |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `495ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `244ms` |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `245ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `264ms` |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `257ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `269ms` |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `258ms` |




<br>



*Automated by scripts/generate_docs_tests.py*