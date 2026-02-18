# 🛡️ FIPS Compliance Audit Report

> **Generated on:** 2026-02-18 19:25:49 UTC  
> **Status:** ![Status](https://img.shields.io/badge/tests-failed%2010-red)


## 📋 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Build Configuration](#-build-configuration)
3. [Supply Chain & Packages](#-supply-chain--packages)
4. [Test Results Detail](#-test-results-detail)


## 📊 Executive Summary

| Metric | Count | Status |
| :--- | :---: | :--- |
| **Total Tests** | `92` | 🔍 Scoped |
| **Passed** | `82` | ✅ Passing |
| **Failed** | `10` | ❌ Critical |
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
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `260ms` |
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `258ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `1191ms` |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `650ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `259ms` |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `260ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `254ms` |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `267ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `242ms` |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `256ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `257ms` |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `256ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `253ms` |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `266ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `253ms` |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `266ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `241ms` |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `263ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `502ms` |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `507ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `250ms` |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `251ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `259ms` |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `245ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `245ms` |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `244ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `254ms` |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `252ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `249ms` |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `250ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `249ms` |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `253ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `249ms` |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `253ms` |



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
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `1001ms` |
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `1028ms` |



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
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `254ms` |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `247ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `256ms` |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `242ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `491ms` |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `499ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `253ms` |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `253ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `758ms` |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `765ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp7x66n12t:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmptk6xg72o:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `495ms` |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `526ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `249ms` |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `252ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1256ms` |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1247ms` |



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
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `244ms` |
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `254ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `300ms` |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `301ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `247ms` |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `258ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `468ms` |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `746ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `569ms` |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `608ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp3bcchgtv:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp4l2z19bd:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `53ms` |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `60ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `253ms` |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `269ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `255ms` |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `258ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `251ms` |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `256ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `244ms` |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `250ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15276ms` |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15273ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `413ms` |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `467ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `30555ms` |
| ✅ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `30831ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `269ms` |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `269ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `278ms` |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `283ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `284ms` |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `279ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `499ms` |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `506ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `244ms` |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `250ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `281ms` |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `294ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `279ms` |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `283ms` |




<br>



*Automated by scripts/generate_docs_tests.py*