# 🛡️ FIPS Compliance Audit Report

> **Generated on:** 2026-02-18 18:49:16 UTC  
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
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `234ms` |
| ✅ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `249ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `2344ms` |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `1873ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `248ms` |
| ✅ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `234ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `237ms` |
| ✅ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `242ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `236ms` |
| ✅ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `240ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `240ms` |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `247ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `237ms` |
| ✅ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `244ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `261ms` |
| ✅ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `251ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `236ms` |
| ✅ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `240ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `480ms` |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `505ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `243ms` |
| ✅ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `257ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `240ms` |
| ✅ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `250ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `240ms` |
| ✅ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `247ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `255ms` |
| ✅ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `246ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `266ms` |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `253ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `241ms` |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `258ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `237ms` |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `264ms` |



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
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `965ms` |
| ❌ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `988ms` |



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
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `248ms` |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `242ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `250ms` |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `249ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `517ms` |
| ✅ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `503ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `275ms` |
| ✅ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `244ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `737ms` |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `753ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpcr6sla5b:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmptq3zcgk1:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `479ms` |
| ✅ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `490ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `242ms` |
| ✅ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `248ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1232ms` |
| ❌ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `1228ms` |



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
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `245ms` |
| ✅ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `254ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `327ms` |
| ✅ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `269ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `241ms` |
| ✅ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `236ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `979ms` |
| ✅ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `434ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `529ms` |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `615ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpsn2dzc_x:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp4pnu0p3d:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `52ms` |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `58ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `244ms` |
| ✅ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `241ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `245ms` |
| ✅ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `243ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `239ms` |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `251ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `241ms` |
| ✅ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `245ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15272ms` |
| ✅ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `15263ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `429ms` |
| ✅ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `403ms` |




<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15268ms` |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15280ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption


**🔴 Verify Secure TLS 1.3 Session Resumption with PSK**
> Detailed Validation of the Container's TCP/IP Stack:  
1. Attempts to establish a raw socket connection.  
2. Bypasses DNS resolution.

**Trace:**
```text
tests/tests/test_11_network_tls.py:400: in test_secure_tls13_session_resumption
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
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpf1xlcu1n:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQG...d6 b4 8e   S...2C..Oz.\'....\n    0030 - 35 a1 63 35 50 c6 dd f2-58 b3 31 16 35 7a 38 69   5.c5P...X.1.5z8i\n    0040 - 8c 8b 47 8a f8 df ab 8d-89 43 6f 34 0f a1 e0 03   ..G......Co4....\n    0050 - ec 14 4a d7 02 1c 39 fc-d7 2f b9 9a 7b ae 26 18   ..J...9../..{.&.\n    0060 - 14 e4 2b db 17 7c 58 4d-00 21 22 70 b8 41 d4 f1   ..+..|XM.!"p.A..\n    0070 - e2 28 2f ac e3 ff 87 db-47 04 df 5e 71 5c a7 31   .(/.....G..^q\\.1\n    0080 - 62 22 ed 08 d8 ec af d4-d0 6c 51 fd 60 33 a9 29   b".......lQ.`3.)\n    0090 - 93 4b b2 fe 57 d2 85 fc-d1 9e 41 17 2d 60 82 08   .K..W.....A.-`..\n    00a0 - be 3b 41 e1 d9 76 1c 19-74 f6 6b 91 66 93 4d 78   .;A..v..t.k.f.Mx\n    00b0 - fc a9 ea 19 fd 3e 69 fb-ba 10 2e f3 47 b6 48 d9   .....>i.....G.H.\n\n    Start Time: 1771440507\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.123.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
```
---

**🔴 Verify Secure TLS 1.3 Session Resumption with PSK**
> Detailed Validation of the Container's TCP/IP Stack:  
1. Attempts to establish a raw socket connection.  
2. Bypasses DNS resolution.

**Trace:**
```text
tests/tests/test_11_network_tls.py:400: in test_secure_tls13_session_resumption
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
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp8kb2noz2:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQGEwJVUzEeMB... 7c 0d 9a   Z.=7.....B...|..\n    0030 - f9 6d 1c 08 c6 98 b4 44-e8 ba 8c 7e fc 1e 8d 2c   .m.....D...~...,\n    0040 - 69 61 43 b3 0e 14 b2 9f-4e 46 5c 8d e4 13 15 c4   iaC.....NF\\.....\n    0050 - b6 7e 53 e1 c0 38 83 da-da 9b 3d 66 4a e2 c6 92   .~S..8....=fJ...\n    0060 - 04 2d f4 73 00 86 18 01-18 8d 5d 72 7e dc 45 48   .-.s......]r~.EH\n    0070 - 47 31 bb a0 55 14 37 bb-ac 2d 99 5e 15 b3 47 69   G1..U.7..-.^..Gi\n    0080 - 91 ef ec f9 22 94 0d cd-48 52 e5 16 38 a0 e8 43   ...."...HR..8..C\n    0090 - 89 b3 b2 46 cc 85 ba ad-b0 65 ef 4e fd 4e 9d 3f   ...F.....e.N.N.?\n    00a0 - 4e eb d5 d4 bd 4f 99 81-76 d7 dd 40 f9 89 68 8f   N....O..v..@..h.\n    00b0 - d5 89 e7 85 40 14 2d 9d-d8 ff 45 26 63 4b 6a 32   ....@.-...E&cKj2\n\n    Start Time: 1771440555\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.124.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `240ms` |
| ✅ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `251ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `286ms` |
| ✅ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `279ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `289ms` |
| ✅ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `306ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `485ms` |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `484ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `240ms` |
| ✅ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `238ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `272ms` |
| ✅ | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `263ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `255ms` |
| ✅ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `255ms` |




<br>



*Automated by scripts/generate_docs_tests.py*