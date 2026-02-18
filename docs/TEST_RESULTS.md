# 🛡️ FIPS Compliance Audit Report

> **Generated on:** 2026-02-18 16:34:51 UTC  
> **Status:** ![Status](https://img.shields.io/badge/tests-failed%2068-red)


## 📋 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Build Configuration](#-build-configuration)
3. [Supply Chain & Packages](#-supply-chain--packages)
4. [Test Results Detail](#-test-results-detail)


## 📊 Executive Summary

| Metric | Count | Status |
| :--- | :---: | :--- |
| **Total Tests** | `92` | 🔍 Scoped |
| **Passed** | `24` | ✅ Passing |
| **Failed** | `66` | ❌ Critical |
| **Broken** | `2` | ⚠️ Error |


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
| ❌ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `12ms` |
| ❌ | **Verify Default Provider Blocking (Isolation Check)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation</sub> | `14ms` |



#### 🔻 Failure Analysis for tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_default_provider_isolation


**🔴 Verify Default Provider Blocking (Isolation Check)**
>   
        Ensures strict isolation between the FIPS provider and the default provider.  
        By attempting to call an unapproved algorithm (MD5) without explicit property queries,  
        this test verifies that the default provider is disabled or inaccessible.   
        This prevents accidental usage of non-validated cryptographic implementations.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:239: in test_default_provider_isolation
    assert any(x in error_msg for x in ["unsupported", "fetch failed", "error", "not found"]), \
E   AssertionError: Unexpected behavior during isolation check: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestCorePolicyAndIntegrity.test_default_provider_isolation.<locals>.<genexpr> at 0x7f5064ced7d0>)
```
---

**🔴 Verify Default Provider Blocking (Isolation Check)**
>   
        Ensures strict isolation between the FIPS provider and the default provider.  
        By attempting to call an unapproved algorithm (MD5) without explicit property queries,  
        this test verifies that the default provider is disabled or inaccessible.   
        This prevents accidental usage of non-validated cryptographic implementations.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:239: in test_default_provider_isolation
    assert any(x in error_msg for x in ["unsupported", "fetch failed", "error", "not found"]), \
E   AssertionError: Unexpected behavior during isolation check: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestCorePolicyAndIntegrity.test_default_provider_isolation.<locals>.<genexpr> at 0x7f21cdeeb9f0>)
```
---



<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `1962ms` |
| ✅ | **Verify FIPS Config File Indicators (fipsmodule.cnf)**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_fips_config_file_indicators</sub> | `1557ms` |




<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `12ms` |
| ❌ | **Verify Mandatory FIPS Property Enforcement**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property</sub> | `14ms` |



#### 🔻 Failure Analysis for tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_mandatory_fips_property


**🔴 Verify Mandatory FIPS Property Enforcement**
>   
        Tests the strict enforcement of the FIPS security policy.  
        Attempts to bypass FIPS mode using '-propquery fips=no'.   
        The system MUST reject this request if 'default_properties = fips=yes'   
        is correctly configured in the OpenSSL configuration file.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:147: in test_mandatory_fips_property
    assert any(x in error_msg for x in ["unsupported", "fetch failed", "error"]), \
E   AssertionError: Unexpected error message during bypass attempt: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestCorePolicyAndIntegrity.test_mandatory_fips_property.<locals>.<genexpr> at 0x7f5064c96b50>)
```
---

**🔴 Verify Mandatory FIPS Property Enforcement**
>   
        Tests the strict enforcement of the FIPS security policy.  
        Attempts to bypass FIPS mode using '-propquery fips=no'.   
        The system MUST reject this request if 'default_properties = fips=yes'   
        is correctly configured in the OpenSSL configuration file.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:147: in test_mandatory_fips_property
    assert any(x in error_msg for x in ["unsupported", "fetch failed", "error"]), \
E   AssertionError: Unexpected error message during bypass attempt: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestCorePolicyAndIntegrity.test_mandatory_fips_property.<locals>.<genexpr> at 0x7f21cde77c60>)
```
---



<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `12ms` |
| ❌ | **Verify FIPS Module Operational State Persistence**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_operational_state_stability


**🔴 Verify FIPS Module Operational State Persistence**
>   
        Validates the operational stability of the FIPS module as required by FIPS 140-3 standards.  
        This test ensures that the cryptographic module remains in a consistent 'active' state   
        during service requests and does not transition into an undefined, uninitialized,   
        or insecure error state during standard operations.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:195: in test_operational_state_stability
    assert result.returncode == 0, "The module failed to respond to service requests, indicating operational instability."
E   AssertionError: The module failed to respond to service requests, indicating operational instability.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify FIPS Module Operational State Persistence**
>   
        Validates the operational stability of the FIPS module as required by FIPS 140-3 standards.  
        This test ensures that the cryptographic module remains in a consistent 'active' state   
        during service requests and does not transition into an undefined, uninitialized,   
        or insecure error state during standard operations.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:195: in test_operational_state_stability
    assert result.returncode == 0, "The module failed to respond to service requests, indicating operational instability."
E   AssertionError: The module failed to respond to service requests, indicating operational instability.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `12ms` |
| ❌ | **Verify FIPS Module Version & Metadata**<br><sub>tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_01_core_policy.TestCorePolicyAndIntegrity#test_provider_version_metadata


**🔴 Verify FIPS Module Version & Metadata**
>   
        Ensures the loaded FIPS provider matches the expected NIST-validated version   
        (e.g., 3.1.2) and correctly identifies itself as 'OpenSSL FIPS Provider'.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:106: in test_provider_version_metadata
    assert result.returncode == 0, "Failed to retrieve provider list."
E   AssertionError: Failed to retrieve provider list.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify FIPS Module Version & Metadata**
>   
        Ensures the loaded FIPS provider matches the expected NIST-validated version   
        (e.g., 3.1.2) and correctly identifies itself as 'OpenSSL FIPS Provider'.  
    

**Trace:**
```text
tests/tests/test_01_core_policy.py:106: in test_provider_version_metadata
    assert result.returncode == 0, "Failed to retrieve provider list."
E   AssertionError: Failed to retrieve provider list.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `12ms` |
| ✅ | **Verify MD5 Algorithm Rejection**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_md5_execution_rejection</sub> | `13ms` |




<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `12ms` |
| ❌ | **Verify SHA-256 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_02_hashing_and_digests.TestMessageDigests#test_sha256_availability


**🔴 Verify SHA-256 Algorithm Availability**
>   
        Confirms that the SHA-256 algorithm (SHA-2 Family) is fully operational.  
        This is a blocker requirement as it is the standard hashing algorithm for FIPS 140-3.  
    

**Trace:**
```text
tests/tests/test_02_hashing_and_digests.py:48: in test_sha256_availability
    assert result.returncode == 0, f"SHA-256 execution failed. Stderr: {result.stderr}"
E   AssertionError: SHA-256 execution failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify SHA-256 Algorithm Availability**
>   
        Confirms that the SHA-256 algorithm (SHA-2 Family) is fully operational.  
        This is a blocker requirement as it is the standard hashing algorithm for FIPS 140-3.  
    

**Trace:**
```text
tests/tests/test_02_hashing_and_digests.py:48: in test_sha256_availability
    assert result.returncode == 0, f"SHA-256 execution failed. Stderr: {result.stderr}"
E   AssertionError: SHA-256 execution failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `12ms` |
| ❌ | **Verify SHA-3 Algorithm Availability**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_02_hashing_and_digests.TestMessageDigests#test_sha3_availability


**🔴 Verify SHA-3 Algorithm Availability**
>   
        Validates the availability of the SHA-3 family (NIST SP 800-202).  
        Ensures that modern KMAC and SHAKE functions have the necessary underlying primitives.  
    

**Trace:**
```text
tests/tests/test_02_hashing_and_digests.py:69: in test_sha3_availability
    assert result.returncode == 0, f"SHA-3 execution failed. Stderr: {result.stderr}"
E   AssertionError: SHA-3 execution failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify SHA-3 Algorithm Availability**
>   
        Validates the availability of the SHA-3 family (NIST SP 800-202).  
        Ensures that modern KMAC and SHAKE functions have the necessary underlying primitives.  
    

**Trace:**
```text
tests/tests/test_02_hashing_and_digests.py:69: in test_sha3_availability
    assert result.returncode == 0, f"SHA-3 execution failed. Stderr: {result.stderr}"
E   AssertionError: SHA-3 execution failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `13ms` |
| ❌ | **Verify SHAKE XOF Functionality**<br><sub>tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_02_hashing_and_digests.TestMessageDigests#test_shake_xof_functionality


**🔴 Verify SHAKE XOF Functionality**
>   
        Validates the functionality of SHAKE128 (Extendable Output Function).  
        Ensures the algorithm is available and functional within the FIPS boundary.  
        Accepts both 'SHAKE128' and 'SHAKE-128' naming conventions.  
    

**Trace:**
```text
tests/tests/test_02_hashing_and_digests.py:99: in test_shake_xof_functionality
    assert result.returncode == 0, f"SHAKE128 execution failed. Stderr: {result.stderr}"
E   AssertionError: SHAKE128 execution failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify SHAKE XOF Functionality**
>   
        Validates the functionality of SHAKE128 (Extendable Output Function).  
        Ensures the algorithm is available and functional within the FIPS boundary.  
        Accepts both 'SHAKE128' and 'SHAKE-128' naming conventions.  
    

**Trace:**
```text
tests/tests/test_02_hashing_and_digests.py:99: in test_shake_xof_functionality
    assert result.returncode == 0, f"SHAKE128 execution failed. Stderr: {result.stderr}"
E   AssertionError: SHAKE128 execution failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `479ms` |
| ✅ | **Verify AES-CBC Functional Integrity (KAT)**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_cbc_known_answer</sub> | `530ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `12ms` |
| ❌ | **Verify AES-GCM Tag Length Restrictions**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_gcm_tag_length


**🔴 Verify AES-GCM Tag Length Restrictions**
>   
        Validates the precision of cryptographic boundaries for authenticated encryption (AES-GCM).  
        FIPS 140-3 mandates specific approved Tag lengths (typically 96, 104, 112, 120, or 128 bits).  
        This test ensures that the module rejects insecure, unapproved short tag lengths   
        (e.g., 32-bit / 4-byte) to prevent tag forgery and maintain security strength.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:36: in test_aes_gcm_tag_length
    assert any(x in error_msg for x in ["error", "invalid", "unsupported", "tag", "macopt"]), \
E   AssertionError: Unexpected error behavior during GCM tag length rejection: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestAESEncryption.test_aes_gcm_tag_length.<locals>.<genexpr> at 0x7f5064c0b100>)
```
---

**🔴 Verify AES-GCM Tag Length Restrictions**
>   
        Validates the precision of cryptographic boundaries for authenticated encryption (AES-GCM).  
        FIPS 140-3 mandates specific approved Tag lengths (typically 96, 104, 112, 120, or 128 bits).  
        This test ensures that the module rejects insecure, unapproved short tag lengths   
        (e.g., 32-bit / 4-byte) to prevent tag forgery and maintain security strength.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:36: in test_aes_gcm_tag_length
    assert any(x in error_msg for x in ["error", "invalid", "unsupported", "tag", "macopt"]), \
E   AssertionError: Unexpected error behavior during GCM tag length rejection: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestAESEncryption.test_aes_gcm_tag_length.<locals>.<genexpr> at 0x7f21cdef0ad0>)
```
---



<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `13ms` |
| ❌ | **Verify AES Key Unwrapping (AES-WRAP) Availability**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed</sub> | `14ms` |



#### 🔻 Failure Analysis for tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_key_unwrapping_allowed


**🔴 Verify AES Key Unwrapping (AES-WRAP) Availability**
>   
        Validates the availability of AES Key Wrap (WRAP) and Key Wrap with Padding (WRAP-PAD).  
        As per Security Policy Table 7 (Page 17) and Table 9 (Page 28), these   
        algorithms are mandated for key unwrapping services.   
        Note: OpenSSL 3.x identifies these internally as 'AES-WRAP' rather than 'AES-KW'.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:184: in test_aes_key_unwrapping_allowed
    assert len(found_identifiers) > 0, "Compliance Failure: AES Key Wrap (WRAP/KW) algorithms not found in FIPS provider."
E   AssertionError: Compliance Failure: AES Key Wrap (WRAP/KW) algorithms not found in FIPS provider.
E   assert 0 > 0
E    +  where 0 = len([])
```
---

**🔴 Verify AES Key Unwrapping (AES-WRAP) Availability**
>   
        Validates the availability of AES Key Wrap (WRAP) and Key Wrap with Padding (WRAP-PAD).  
        As per Security Policy Table 7 (Page 17) and Table 9 (Page 28), these   
        algorithms are mandated for key unwrapping services.   
        Note: OpenSSL 3.x identifies these internally as 'AES-WRAP' rather than 'AES-KW'.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:184: in test_aes_key_unwrapping_allowed
    assert len(found_identifiers) > 0, "Compliance Failure: AES Key Wrap (WRAP/KW) algorithms not found in FIPS provider."
E   AssertionError: Compliance Failure: AES Key Wrap (WRAP/KW) algorithms not found in FIPS provider.
E   assert 0 > 0
E    +  where 0 = len([])
```
---



<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `12ms` |
| ❌ | **Verify AES-XTS Rejection of Duplicate Keys**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection</sub> | `15ms` |



#### 🔻 Failure Analysis for tests.test_03_symmetric_ciphers.TestAESEncryption#test_aes_xts_duplicate_key_rejection


**🔴 Verify AES-XTS Rejection of Duplicate Keys**
>   
        Validates compliance with NIST SP 800-38E regarding XTS-AES.  
        The system must reject encryption attempts where Key_1 (Data Encryption Key)   
        is identical to Key_2 (Tweak Key).  
        Simulates an attack using a 512-bit key consisting of identical halves.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:103: in test_aes_xts_duplicate_key_rejection
    assert "error" in error_msg or "hex" in error_msg or "cipher" in error_msg, \
E   AssertionError: Operation failed but without specific key validation error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert ('error' in "unknown flag: --user\n\nusage:  docker [options] command [arg...]\n\nrun 'docker --help' for more information\n" or 'hex' in "unknown flag: --user\n\nusage:  docker [options] command [arg...]\n\nrun 'docker --help' for more information\n" or 'cipher' in "unknown flag: --user\n\nusage:  docker [options] command [arg...]\n\nrun 'docker --help' for more information\n")
```
---

**🔴 Verify AES-XTS Rejection of Duplicate Keys**
>   
        Validates compliance with NIST SP 800-38E regarding XTS-AES.  
        The system must reject encryption attempts where Key_1 (Data Encryption Key)   
        is identical to Key_2 (Tweak Key).  
        Simulates an attack using a 512-bit key consisting of identical halves.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:103: in test_aes_xts_duplicate_key_rejection
    assert "error" in error_msg or "hex" in error_msg or "cipher" in error_msg, \
E   AssertionError: Operation failed but without specific key validation error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert ('error' in "unknown flag: --user\n\nusage:  docker [options] command [arg...]\n\nrun 'docker --help' for more information\n" or 'hex' in "unknown flag: --user\n\nusage:  docker [options] command [arg...]\n\nrun 'docker --help' for more information\n" or 'cipher' in "unknown flag: --user\n\nusage:  docker [options] command [arg...]\n\nrun 'docker --help' for more information\n")
```
---



<br>

### 📁 tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `12ms` |
| ❌ | **Verify FIPS-Approved Cipher Algorithms**<br><sub>tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_03_symmetric_ciphers.TestAESEncryption#test_fips_cipher_list_integrity


**🔴 Verify FIPS-Approved Cipher Algorithms**
>   
        Queries the OpenSSL provider for algorithms strictly tagged with 'fips=yes'.  
        Validates that the mandatory AES-GCM (Galois/Counter Mode) cipher is present   
        and available for use within the cryptographic boundary.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:65: in test_fips_cipher_list_integrity
    assert result.returncode == 0, f"Failed to list ciphers. Stderr: {result.stderr}"
E   AssertionError: Failed to list ciphers. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify FIPS-Approved Cipher Algorithms**
>   
        Queries the OpenSSL provider for algorithms strictly tagged with 'fips=yes'.  
        Validates that the mandatory AES-GCM (Galois/Counter Mode) cipher is present   
        and available for use within the cryptographic boundary.  
    

**Trace:**
```text
tests/tests/test_03_symmetric_ciphers.py:65: in test_fips_cipher_list_integrity
    assert result.returncode == 0, f"Failed to list ciphers. Stderr: {result.stderr}"
E   AssertionError: Failed to list ciphers. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `230ms` |
| ✅ | **Verify 3DES Encryption Rejection**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_3des_encryption_rejection</sub> | `273ms` |




<br>

### 📁 tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `235ms` |
| ✅ | **Verify Absolute Absence of Single DES**<br><sub>tests.test_03_symmetric_ciphers.TestLegacyCipherPolicies#test_des_algorithm_absence</sub> | `261ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `22ms` |
| ❌ | **Verify Precise 112-bit Security Boundary**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary</sub> | `22ms` |



#### 🔻 Failure Analysis for tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_112bit_security_boundary


**🔴 Verify Precise 112-bit Security Boundary**
>   
        Validates the exact transition point for HMAC security strength.  
        Ensures that 104-bit keys are rejected and 112-bit keys are accepted   
        under strict FIPS property queries.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:68: in test_hmac_112bit_security_boundary
    assert result_112.returncode == 0, f"Functional Failure: 112-bit key rejected. Stderr: {result_112.stderr}"
E   AssertionError: Functional Failure: 112-bit key rejected. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify Precise 112-bit Security Boundary**
>   
        Validates the exact transition point for HMAC security strength.  
        Ensures that 104-bit keys are rejected and 112-bit keys are accepted   
        under strict FIPS property queries.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:68: in test_hmac_112bit_security_boundary
    assert result_112.returncode == 0, f"Functional Failure: 112-bit key rejected. Stderr: {result_112.stderr}"
E   AssertionError: Functional Failure: 112-bit key rejected. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `44ms` |
| ✅ | **Verify Rejection of Weak Keys across SHA-2 Family**<br><sub>tests.test_04_mac_integrity.TestHMACBoundaries#test_hmac_sha2_key_length_exhaustive</sub> | `49ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `11ms` |
| ✅ | **Verify CMAC-AES Key Strength Enforcement**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_cmac_aes_key_policy</sub> | `12ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `10ms` |
| ✅ | **Verify KMAC-SHA3 Security Strength**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_kmac_sha3_strength</sub> | `12ms` |




<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `22ms` |
| ❌ | **Verify SP 800-108 Counter Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf</sub> | `25ms` |



#### 🔻 Failure Analysis for tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_counter_kdf


**🔴 Verify SP 800-108 Counter Mode KDF Integrity**
>   
        Validates KBKDF in Counter Mode.   
        Note: KBKDF requires an explicit MAC algorithm (HMAC or CMAC).  
        This test uses HMAC-SHA256 as the underlying PRF.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:208: in test_sp800_108_counter_kdf
    assert result.returncode == 0, f"KBKDF Counter Mode failed. Stderr: {result.stderr}"
E   AssertionError: KBKDF Counter Mode failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify SP 800-108 Counter Mode KDF Integrity**
>   
        Validates KBKDF in Counter Mode.   
        Note: KBKDF requires an explicit MAC algorithm (HMAC or CMAC).  
        This test uses HMAC-SHA256 as the underlying PRF.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:208: in test_sp800_108_counter_kdf
    assert result.returncode == 0, f"KBKDF Counter Mode failed. Stderr: {result.stderr}"
E   AssertionError: KBKDF Counter Mode failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `12ms` |
| ❌ | **Verify SP 800-108 Feedback Mode KDF Integrity**<br><sub>tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_04_mac_integrity.TestModernMACs#test_sp800_108_feedback_kdf


**🔴 Verify SP 800-108 Feedback Mode KDF Integrity**
>   
        Validates KBKDF in Feedback Mode using HMAC-SHA256 as the PRF.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:235: in test_sp800_108_feedback_kdf
    assert result.returncode == 0, f"KBKDF Feedback Mode failed. Stderr: {result.stderr}"
E   AssertionError: KBKDF Feedback Mode failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify SP 800-108 Feedback Mode KDF Integrity**
>   
        Validates KBKDF in Feedback Mode using HMAC-SHA256 as the PRF.  
    

**Trace:**
```text
tests/tests/test_04_mac_integrity.py:235: in test_sp800_108_feedback_kdf
    assert result.returncode == 0, f"KBKDF Feedback Mode failed. Stderr: {result.stderr}"
E   AssertionError: KBKDF Feedback Mode failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `733ms` |
| ❌ | **Verify ECDH Raw Key Derivation (NIST P-384)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdh_key_derivation_raw</sub> | `750ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp54aaamys:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp4pfd50kr:/mnt/ecdh', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkey', '-in', '/mnt/ecdh/bob_priv.pem', '-pubout', '-out', '/mnt/ecdh/bob_pub.pem'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key of key from /mnt/ecdh/bob_priv.pem: Permission denied\n').returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `11ms` |
| ❌ | **Verify ECDSA P-384 Functional Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_ecdsa_p384_signing_flow


**🔴 Verify ECDSA P-384 Functional Integrity**
>   
        Validates the generation and structural integrity of Elliptic Curve keys   
        using the NIST P-384 curve. Confirms that the FIPS provider supports   
        approved curves. Note: P-384 is technically referred to as secp384r1.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:263: in test_ecdsa_p384_signing_flow
    assert gen_result.returncode == 0, f"EC Key generation failed. Stderr: {gen_result.stderr}"
E   AssertionError: EC Key generation failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify ECDSA P-384 Functional Integrity**
>   
        Validates the generation and structural integrity of Elliptic Curve keys   
        using the NIST P-384 curve. Confirms that the FIPS provider supports   
        approved curves. Note: P-384 is technically referred to as secp384r1.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:263: in test_ecdsa_p384_signing_flow
    assert gen_result.returncode == 0, f"EC Key generation failed. Stderr: {gen_result.stderr}"
E   AssertionError: EC Key generation failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `12ms` |
| ❌ | **Verify Rejection of MD5 for Digital Signatures**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_md5_signature_verification_rejection


**🔴 Verify Rejection of MD5 for Digital Signatures**
>   
        Validates the mandatory rejection of MD5 when used for digital signatures.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:297: in test_md5_signature_verification_rejection
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Operation failed but not with a clear policy rejection. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestECCAndSignatures.test_md5_signature_verification_rejection.<locals>.<genexpr> at 0x7f5064cedbe0>)
```
---

**🔴 Verify Rejection of MD5 for Digital Signatures**
>   
        Validates the mandatory rejection of MD5 when used for digital signatures.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:297: in test_md5_signature_verification_rejection
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Operation failed but not with a clear policy rejection. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestECCAndSignatures.test_md5_signature_verification_rejection.<locals>.<genexpr> at 0x7f21cdef05f0>)
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `55ms` |
| ✅ | **Verify Rejection of Non-Approved Curves (Ed25519/X25519/Ed448)**<br><sub>tests.test_05_asymmetric_and_pqc.TestECCAndSignatures#test_strict_block_legacy_curves_and_algos</sub> | `59ms` |




<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `10ms` |
| ❌ | **Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**<br><sub>tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestPostQuantumIsolation#test_ml_kem_isolation_in_fips


**🔴 Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**
>   
        Validates that modern Post-Quantum Cryptography (PQC) algorithms, specifically ML-KEM (Kyber),  
        are strictly unavailable when the FIPS property query is enforced.   
        As these algorithms are not yet part of the certified FIPS 140-3 provider   
        (e.g., OpenSSL FIPS provider 3.0.x/3.1.x), they must be rejected to ensure   
        only approved algorithms are used within the cryptographic boundary.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:417: in test_ml_kem_isolation_in_fips
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: The command failed, but not with an expected PQC algorithm rejection error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestPostQuantumIsolation.test_ml_kem_isolation_in_fips.<locals>.<genexpr> at 0x7f5064c4f9f0>)
```
---

**🔴 Verify Isolation of ML-KEM (Kyber) from FIPS Boundary**
>   
        Validates that modern Post-Quantum Cryptography (PQC) algorithms, specifically ML-KEM (Kyber),  
        are strictly unavailable when the FIPS property query is enforced.   
        As these algorithms are not yet part of the certified FIPS 140-3 provider   
        (e.g., OpenSSL FIPS provider 3.0.x/3.1.x), they must be rejected to ensure   
        only approved algorithms are used within the cryptographic boundary.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:417: in test_ml_kem_isolation_in_fips
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: The command failed, but not with an expected PQC algorithm rejection error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestPostQuantumIsolation.test_ml_kem_isolation_in_fips.<locals>.<genexpr> at 0x7f21cdeeb030>)
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `11ms` |
| ❌ | **Verify RSA 2048-bit Compliance**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_2048_compliance


**🔴 Verify RSA 2048-bit Compliance**
>   
        Validates the generation of RSA keys with a 2048-bit modulus.  
        As per FIPS 140-3 and NIST SP 800-131A, 2048-bit is the minimum accepted   
        security strength for RSA key generation in a compliant environment.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:62: in test_rsa_keygen_2048_compliance
    assert result.returncode == 0, f"RSA 2048-bit generation failed. Stderr: {result.stderr}"
E   AssertionError: RSA 2048-bit generation failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify RSA 2048-bit Compliance**
>   
        Validates the generation of RSA keys with a 2048-bit modulus.  
        As per FIPS 140-3 and NIST SP 800-131A, 2048-bit is the minimum accepted   
        security strength for RSA key generation in a compliant environment.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:62: in test_rsa_keygen_2048_compliance
    assert result.returncode == 0, f"RSA 2048-bit generation failed. Stderr: {result.stderr}"
E   AssertionError: RSA 2048-bit generation failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `12ms` |
| ❌ | **Verify Rejection of Weak RSA 1024-bit Keys**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection</sub> | `11ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_keygen_weak_rejection


**🔴 Verify Rejection of Weak RSA 1024-bit Keys**
>   
        Validates the enforcement of minimum RSA key lengths.  
        FIPS 140-3 strictly prohibits the generation of RSA keys smaller than 2048 bits.  
        The system must intercept and reject any attempt to generate a 1024-bit RSA key.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:93: in test_rsa_keygen_weak_rejection
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Generation failed but without a specific policy error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestRSAOperations.test_rsa_keygen_weak_rejection.<locals>.<genexpr> at 0x7f5064b20a00>)
```
---

**🔴 Verify Rejection of Weak RSA 1024-bit Keys**
>   
        Validates the enforcement of minimum RSA key lengths.  
        FIPS 140-3 strictly prohibits the generation of RSA keys smaller than 2048 bits.  
        The system must intercept and reject any attempt to generate a 1024-bit RSA key.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:93: in test_rsa_keygen_weak_rejection
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Generation failed but without a specific policy error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestRSAOperations.test_rsa_keygen_weak_rejection.<locals>.<genexpr> at 0x7f21cdcacad0>)
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `13ms` |
| ❌ | **Verify Support for Large RSA Modulus (4096-bit)**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support</sub> | `11ms` |



#### 🔻 Failure Analysis for tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_large_modulus_support


**🔴 Verify Support for Large RSA Modulus (4096-bit)**
>   
        Validates that the FIPS provider supports RSA modulus sizes beyond the 2048-bit minimum.  
        According to Security Policy Page 36 (Section 2.7.g), the module supports modulus   
        lengths up to 16384 bits. This test performs a functional generation of a 4096-bit   
        RSA key to confirm support for large moduli while maintaining efficient test execution time.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:36: in test_rsa_large_modulus_support
    assert result.returncode == 0, f"FIPS provider failed to generate a {target_bits}-bit RSA key."
E   AssertionError: FIPS provider failed to generate a 4096-bit RSA key.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify Support for Large RSA Modulus (4096-bit)**
>   
        Validates that the FIPS provider supports RSA modulus sizes beyond the 2048-bit minimum.  
        According to Security Policy Page 36 (Section 2.7.g), the module supports modulus   
        lengths up to 16384 bits. This test performs a functional generation of a 4096-bit   
        RSA key to confirm support for large moduli while maintaining efficient test execution time.  
    

**Trace:**
```text
tests/tests/test_05_asymmetric_and_pqc.py:36: in test_rsa_large_modulus_support
    assert result.returncode == 0, f"FIPS provider failed to generate a {target_bits}-bit RSA key."
E   AssertionError: FIPS provider failed to generate a 4096-bit RSA key.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `551ms` |
| ❌ | **Verify RSA-PSS Signature and Verification Integrity**<br><sub>tests.test_05_asymmetric_and_pqc.TestRSAOperations#test_rsa_pss_padding_signature</sub> | `555ms` |



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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmp85n594wu:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
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
E    +  where 1 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpjb4u6sc4:/mnt/crypto', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 'pkeyutl', '-sign', '-propquery', 'fips=yes', '-inkey', '/mnt/crypto/key.pem', '-digest', 'sha256', '-pkeyopt', 'rsa_padding_mode:pss', '-pkeyopt', 'rsa_pss_saltlen:32', '-in', '/mnt/crypto/data.txt', '-out', '/mnt/crypto/signature.bin'], returncode=1, stdout='', stderr='Could not open file or uri for loading private key from /mnt/crypto/key.pem: Permission denied\npkeyutl: Error loading key\n').returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `54ms` |
| ✅ | **Verify Non-Root User Execution Enforcement**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_container_user_security</sub> | `60ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `13ms` |
| ❌ | **Verify FIPS DRBG Functional Integrity**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_06_architecture_compliance.TestSystemIntegrity#test_drbg_functionality


**🔴 Verify FIPS DRBG Functional Integrity**
>   
        Validates the functionality of the Deterministic Random Bit Generator (DRBG).  
        Ensures that the system can generate cryptographically strong random data   
        using the FIPS-approved provider. The test verifies that the 'rand'   
        utility successfully honors the FIPS property query.  
    

**Trace:**
```text
tests/tests/test_06_architecture_compliance.py:89: in test_drbg_functionality
    assert result.returncode == 0, f"Random data generation failed. Stderr: {result.stderr}"
E   AssertionError: Random data generation failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify FIPS DRBG Functional Integrity**
>   
        Validates the functionality of the Deterministic Random Bit Generator (DRBG).  
        Ensures that the system can generate cryptographically strong random data   
        using the FIPS-approved provider. The test verifies that the 'rand'   
        utility successfully honors the FIPS property query.  
    

**Trace:**
```text
tests/tests/test_06_architecture_compliance.py:89: in test_drbg_functionality
    assert result.returncode == 0, f"Random data generation failed. Stderr: {result.stderr}"
E   AssertionError: Random data generation failed. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `12ms` |
| ❌ | **Verify Entropy Source Authority & FIPS Provider Priority**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_06_architecture_compliance.TestSystemIntegrity#test_entropy_source_validation


**🔴 Verify Entropy Source Authority & FIPS Provider Priority**
>   
        Validates that the cryptographic module utilizes a FIPS-approved entropy source.  
        This test ensures that the Deterministic Random Bit Generator (DRBG) is   
        specifically provided by the 'fips' provider (e.g., CTR-DRBG @ fips),   
        overriding any legacy or default system entropy sources.  
    

**Trace:**
```text
tests/tests/test_06_architecture_compliance.py:120: in test_entropy_source_validation
    assert result.returncode == 0, "Failed to retrieve the list of random generators."
E   AssertionError: Failed to retrieve the list of random generators.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify Entropy Source Authority & FIPS Provider Priority**
>   
        Validates that the cryptographic module utilizes a FIPS-approved entropy source.  
        This test ensures that the Deterministic Random Bit Generator (DRBG) is   
        specifically provided by the 'fips' provider (e.g., CTR-DRBG @ fips),   
        overriding any legacy or default system entropy sources.  
    

**Trace:**
```text
tests/tests/test_06_architecture_compliance.py:120: in test_entropy_source_validation
    assert result.returncode == 0, "Failed to retrieve the list of random generators."
E   AssertionError: Failed to retrieve the list of random generators.
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `12ms` |
| ✅ | **Verify Absence of Legacy Cryptographic Engines**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_legacy_engines_absence</sub> | `12ms` |




<br>

### 📁 tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `12ms` |
| ❌ | **Verify PBKDF2 Derivation with FIPS Approved Digest**<br><sub>tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_06_architecture_compliance.TestSystemIntegrity#test_pbkdf2_derivation


**🔴 Verify PBKDF2 Derivation with FIPS Approved Digest**
>   
        Validates the PBKDF2 integrity.   
        Note: FIPS 140-3 (via NIST SP 800-132) mandates a minimum salt length   
        of 128 bits (16 bytes). This test uses a 128-bit hex salt to comply.  
    

**Trace:**
```text
tests/tests/test_06_architecture_compliance.py:182: in test_pbkdf2_derivation
    assert result.returncode == 0, f"PBKDF2 failed even with 128-bit salt. Stderr: {result.stderr}"
E   AssertionError: PBKDF2 failed even with 128-bit salt. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify PBKDF2 Derivation with FIPS Approved Digest**
>   
        Validates the PBKDF2 integrity.   
        Note: FIPS 140-3 (via NIST SP 800-132) mandates a minimum salt length   
        of 128 bits (16 bytes). This test uses a 128-bit hex salt to comply.  
    

**Trace:**
```text
tests/tests/test_06_architecture_compliance.py:182: in test_pbkdf2_derivation
    assert result.returncode == 0, f"PBKDF2 failed even with 128-bit salt. Stderr: {result.stderr}"
E   AssertionError: PBKDF2 failed even with 128-bit salt. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `11ms` |
| ❌ | **Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_fips_approved_key_exchange_negotiation


**🔴 Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**
> 

**Trace:**
```text
tests/tests/test_11_network_tls.py:321: in test_fips_approved_key_exchange_negotiation
    assert result.returncode == 0, f"Handshake failed when restricted to a FIPS-approved curve. Stderr: {result.stderr}"
E   AssertionError: Handshake failed when restricted to a FIPS-approved curve. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify Exclusive Use of FIPS-Approved Elliptic Curves for Key Exchange**
> 

**Trace:**
```text
tests/tests/test_11_network_tls.py:321: in test_fips_approved_key_exchange_negotiation
    assert result.returncode == 0, f"Handshake failed when restricted to a FIPS-approved curve. Stderr: {result.stderr}"
E   AssertionError: Handshake failed when restricted to a FIPS-approved curve. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `12ms` |
| ❌ | **Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_rejection_of_sha1_certificate_signature


**🔴 Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**
>   
        FIPS 140-3 strictly forbids the use of SHA-1 for digital signature verification. This test  
        validates that the TLS client will reject a server's certificate chain if it is signed with  
        a deprecated hash algorithm.  
        1. Attempts to connect to a public server known to use a SHA-1 certificate for testing purposes (sha1-2017.badssl.com).  
        2. Verifies that the handshake fails as expected.  
        3. Examines the error message to confirm the failure reason is specifically a certificate verification or signature algorithm error.  
        4. A successful connection would represent a critical failure to enforce FIPS signature algorithm policies.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:368: in test_rejection_of_sha1_certificate_signature
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Connection failed, but not with an expected signature validation error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestAdvancedFIPSNetworkCompliance.test_rejection_of_sha1_certificate_signature.<locals>.<genexpr> at 0x7f5064b212f0>)
```
---

**🔴 Verify Rejection of Certificates with Non-Approved Signature Hashes (SHA-1)**
>   
        FIPS 140-3 strictly forbids the use of SHA-1 for digital signature verification. This test  
        validates that the TLS client will reject a server's certificate chain if it is signed with  
        a deprecated hash algorithm.  
        1. Attempts to connect to a public server known to use a SHA-1 certificate for testing purposes (sha1-2017.badssl.com).  
        2. Verifies that the handshake fails as expected.  
        3. Examines the error message to confirm the failure reason is specifically a certificate verification or signature algorithm error.  
        4. A successful connection would represent a critical failure to enforce FIPS signature algorithm policies.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:368: in test_rejection_of_sha1_certificate_signature
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Connection failed, but not with an expected signature validation error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestAdvancedFIPSNetworkCompliance.test_rejection_of_sha1_certificate_signature.<locals>.<genexpr> at 0x7f21cde73b90>)
```
---



<br>

### 📁 tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15314ms` |
| ❌ | **Verify Secure TLS 1.3 Session Resumption with PSK**<br><sub>tests.test_11_network_tls.TestAdvancedFIPSNetworkCompliance#test_secure_tls13_session_resumption</sub> | `15312ms` |



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
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmpj565kv5t:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQG...e 6e 77 83   ._Z..8CL-!U..nw.\n    0030 - 76 46 62 4e fd be f1 7e-bf da 11 28 4a 7a ed 91   vFbN...~...(Jz..\n    0040 - cd 8d 15 f4 8b e2 9f 33-2f 51 c7 57 37 3f 76 78   .......3/Q.W7?vx\n    0050 - 0d c3 58 8d fb 62 0b c9-7d 71 40 32 8e be fe b4   ..X..b..}q@2....\n    0060 - 7f e4 09 74 b5 87 8a 59-76 f4 46 ef fc 88 5d ee   ...t...Yv.F...].\n    0070 - 61 b7 69 91 8f 48 b3 99-ea 18 a7 4c 43 ae 77 ad   a.i..H.....LC.w.\n    0080 - 86 65 3a 4d 7b f2 b2 c3-f5 61 58 1d e7 f6 08 3f   .e:M{....aX....?\n    0090 - 1f b9 9d 02 98 07 df 0d-60 5f c3 f6 cf 4d 37 77   ........`_...M7w\n    00a0 - 82 57 c1 a9 9c 9f a5 c9-e3 28 0b 8c 61 aa 6b ba   .W.......(..a.k.\n    00b0 - 93 0c 3a 20 a4 3d 6b 4c-15 9b 36 54 87 b5 28 0c   ..: .=kL..6T..(.\n\n    Start Time: 1771432469\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.123.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
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
E    +  where 13 = CompletedProcess(args=['docker', 'run', '--rm', '-v', '/home/runner/work/openssl_fips/openssl_fips/tmptomzlkmx:/mnt/session_data', 'ghcr.io/taha2samy/wolfi-openssl-fips:latest', 's_client', '-connect', 'www.cloudflare.com:443', '-sess_out', '/mnt/session_data/tls_session.pem', '-ign_eof'], returncode=13, stdout='CONNECTED(00000003)\n---\nCertificate chain\n 0 s:CN=www.cloudflare.com\n   i:C=US, O=Google Trust Services, CN=WE1\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA256\n   v:NotBefore: Jan 23 11:54:06 2026 GMT; NotAfter: Apr 23 12:54:03 2026 GMT\n 1 s:C=US, O=Google Trust Services, CN=WE1\n   i:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   a:PKEY: EC, (prime256v1); sigalg: ecdsa-with-SHA384\n   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT\n 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R4\n   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA\n   a:PKEY: EC, (secp384r1); sigalg: sha256WithRSAEncryption\n   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT\n---\nServer certificate\n-----BEGIN CERTIFICATE-----\nMIIDvzCCA2agAwIBAgIQar3iVpIg6BkOSD0dAV0oRjAKBggqhkjOPQQDAjA7MQsw\nCQYDVQQGEwJVUzEeMB... 31 99 13   y%A..I..i..?.1..\n    0030 - d8 e4 74 a1 34 de 79 f8-42 c6 13 f5 51 d0 bf 2f   ..t.4.y.B...Q../\n    0040 - 13 82 ce f1 3c f5 5c ee-5b f1 a4 bb 4f 53 8e a4   ....<.\\.[...OS..\n    0050 - 15 69 73 72 3a 70 88 94-8b f8 4b 9b c0 ff d9 fe   .isr:p....K.....\n    0060 - 37 8a 77 e2 a0 5d c6 87-85 ca 40 cb 18 bf 0d a2   7.w..]....@.....\n    0070 - c6 ac cc 80 14 f5 0b 7c-33 bf 8b 20 3b fb a1 f1   .......|3.. ;...\n    0080 - 02 2a 2e 7d e4 98 a2 7f-0e 38 d5 79 33 67 43 ec   .*.}.....8.y3gC.\n    0090 - a5 d5 26 21 c7 97 ee d6-63 c3 a6 ef fc b6 48 a7   ..&!....c.....H.\n    00a0 - a3 f8 a6 21 ec 1b 69 b4-ff b9 9c 74 01 5d 72 4a   ...!..i....t.]rJ\n    00b0 - e2 7e c3 58 93 85 71 e6-6a cb 7e a7 8e 0a 34 8f   .~.X..q.j.~...4.\n\n    Start Time: 1771432490\n    Timeout   : 7200 (sec)\n    Verify return code: 0 (ok)\n    Extended master secret: no\n    Max Early Data: 0\n---\n', stderr='Connecting to 104.16.124.96\ndepth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R4\nverify return:1\ndepth=1 C=US, O=Google Trust Services, CN=WE1\nverify return:1\ndepth=0 CN=www.cloudflare.com\nverify return:1\nError writing session file /mnt/session_data/tls_session.pem\nread:errno=13\n').returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `11ms` |
| ❌ | **Verify X.509 Certificate Parsing & Structural Integrity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestNetworkAndTLS#test_certificate_parsing


**🔴 Verify X.509 Certificate Parsing & Structural Integrity**
>   
        Comprehensive Validation of Certificate Parsing Capabilities:  
        1. Accesses the system's root CA bundle located at /etc/ssl/certs/ca-certificates.crt.  
        2. Utilizes the 'x509' utility to parse and decode the certificate structure without outputting the body.  
        3. Verifies that the FIPS provider can successfully identify and extract mandatory fields (Subject, Issuer, Public Key).  
        4. Ensures that the module's ASN.1 parser is fully operational and compatible with standard trust stores.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:104: in test_certificate_parsing
    assert result.returncode == 0, f"Certificate parsing failed. Path might be missing or corrupted. Stderr: {result.stderr}"
E   AssertionError: Certificate parsing failed. Path might be missing or corrupted. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify X.509 Certificate Parsing & Structural Integrity**
>   
        Comprehensive Validation of Certificate Parsing Capabilities:  
        1. Accesses the system's root CA bundle located at /etc/ssl/certs/ca-certificates.crt.  
        2. Utilizes the 'x509' utility to parse and decode the certificate structure without outputting the body.  
        3. Verifies that the FIPS provider can successfully identify and extract mandatory fields (Subject, Issuer, Public Key).  
        4. Ensures that the module's ASN.1 parser is fully operational and compatible with standard trust stores.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:104: in test_certificate_parsing
    assert result.returncode == 0, f"Certificate parsing failed. Path might be missing or corrupted. Stderr: {result.stderr}"
E   AssertionError: Certificate parsing failed. Path might be missing or corrupted. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert 125 == 0
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `12ms` |
| ❌ | **Verify Mandatory FIPS-Approved Cipher Suite Enforcement**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestNetworkAndTLS#test_cipher_suite_enforcement


**🔴 Verify Mandatory FIPS-Approved Cipher Suite Enforcement**
>   
        Strict Validation of TLS Negotiation and Cipher Availability:  
        1. Attempts to establish a TLS 1.3 connection to a secure endpoint (google.com).  
        2. Forces the use of the high-strength FIPS-approved cipher: TLS_AES_256_GCM_SHA384.  
        3. Validates that the TLS stack correctly selects and applies the requested cipher suite.  
        4. Ensures that no fallback to non-approved or weaker ciphers occurs during the handshake.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:145: in test_cipher_suite_enforcement
    assert result.returncode == 0 and cipher_confirmed, \
E   AssertionError: Failed to establish connection using enforced cipher TLS_AES_256_GCM_SHA384. Check TLS stack integration.
E   assert (125 == 0)
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---

**🔴 Verify Mandatory FIPS-Approved Cipher Suite Enforcement**
>   
        Strict Validation of TLS Negotiation and Cipher Availability:  
        1. Attempts to establish a TLS 1.3 connection to a secure endpoint (google.com).  
        2. Forces the use of the high-strength FIPS-approved cipher: TLS_AES_256_GCM_SHA384.  
        3. Validates that the TLS stack correctly selects and applies the requested cipher suite.  
        4. Ensures that no fallback to non-approved or weaker ciphers occurs during the handshake.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:145: in test_cipher_suite_enforcement
    assert result.returncode == 0 and cipher_confirmed, \
E   AssertionError: Failed to establish connection using enforced cipher TLS_AES_256_GCM_SHA384. Check TLS stack integration.
E   assert (125 == 0)
E    +  where 125 = CleanResult(returncode=125, stdout='', stderr="unknown flag: --user\n\nUsage:  docker [OPTIONS] COMMAND [ARG...]\n\nRun 'docker --help' for more information\n").returncode
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `11ms` |
| ❌ | **Verify DNS Resolution and Libc Integration**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestNetworkAndTLS#test_dns_resolution


**🔴 Verify DNS Resolution and Libc Integration**
>   
        Validates the integration between the Cryptographic Module and the System Name Resolver:  
        1. Executes a hostname lookup for 'google.com' via the OpenSSL s_client utility.  
        2. Ensures that the container's 'libc' (glibc or musl) correctly interfaces with /etc/resolv.conf.  
        3. Confirms that the Name Service Switch (NSS) can resolve external domains into routable IP addresses.  
        4. Validates that the FIPS provider can successfully wrap the resolved socket in a TLS session.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:74: in test_dns_resolution
    assert dns_success, f"DNS resolution succeeded but the handshake failed. Exit code: {result.returncode}"
E   AssertionError: DNS resolution succeeded but the handshake failed. Exit code: 125
E   assert False
```
---

**🔴 Verify DNS Resolution and Libc Integration**
>   
        Validates the integration between the Cryptographic Module and the System Name Resolver:  
        1. Executes a hostname lookup for 'google.com' via the OpenSSL s_client utility.  
        2. Ensures that the container's 'libc' (glibc or musl) correctly interfaces with /etc/resolv.conf.  
        3. Confirms that the Name Service Switch (NSS) can resolve external domains into routable IP addresses.  
        4. Validates that the FIPS provider can successfully wrap the resolved socket in a TLS session.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:74: in test_dns_resolution
    assert dns_success, f"DNS resolution succeeded but the handshake failed. Exit code: {result.returncode}"
E   AssertionError: DNS resolution succeeded but the handshake failed. Exit code: 125
E   assert False
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `455ms` |
| ✅ | **Verify FIPS Provider Rejection on Configuration Tampering**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_integrity_check_tampering</sub> | `487ms` |




<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `11ms` |
| ❌ | **Verify Rejection of Non-FIPS Ciphers in TLS Handshake**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestNetworkAndTLS#test_non_fips_cipher_rejection_over_network


**🔴 Verify Rejection of Non-FIPS Ciphers in TLS Handshake**
>   
        Validates that the FIPS security policy is strictly enforced at the network socket level.  
        1. Attempts to establish a TLS connection while forcing the use of a legacy, non-FIPS cipher (RC4-MD5).  
        2. Verifies that the FIPS provider intercepts the handshake and rejects the insecure cipher suite.  
        3. Confirms that the connection fails with a clear protocol error, preventing any data exchange over an unapproved channel.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:276: in test_non_fips_cipher_rejection_over_network
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: The connection failed, but not with an expected FIPS-related cipher rejection error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestNetworkAndTLS.test_non_fips_cipher_rejection_over_network.<locals>.<genexpr> at 0x7f5064c95d80>)
```
---

**🔴 Verify Rejection of Non-FIPS Ciphers in TLS Handshake**
>   
        Validates that the FIPS security policy is strictly enforced at the network socket level.  
        1. Attempts to establish a TLS connection while forcing the use of a legacy, non-FIPS cipher (RC4-MD5).  
        2. Verifies that the FIPS provider intercepts the handshake and rejects the insecure cipher suite.  
        3. Confirms that the connection fails with a clear protocol error, preventing any data exchange over an unapproved channel.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:276: in test_non_fips_cipher_rejection_over_network
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: The connection failed, but not with an expected FIPS-related cipher rejection error. Stderr: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestNetworkAndTLS.test_non_fips_cipher_rejection_over_network.<locals>.<genexpr> at 0x7f21cdeea260>)
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| 💥 | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `11ms` |
| 💥 | **Verify Raw TCP/IP Socket Connectivity**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity</sub> | `12ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestNetworkAndTLS#test_tcp_connectivity


**🔴 Verify Raw TCP/IP Socket Connectivity**
>   
        Detailed Validation of the Container's TCP/IP Stack:  
        1. Attempts to establish a raw socket connection to a known public IP (1.1.1.1).  
        2. Bypasses DNS resolution to isolate the network stack's ability to create and manage TCP sessions.  
        3. Verifies that the FIPS-enabled OpenSSL client can correctly initialize a handshake over raw IP sockets.  
        4. Monitors for 'Network is unreachable' or 'Connection refused' errors at the kernel interface level.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:40: in test_tcp_connectivity
    allure.dynamic.description(message="Network Failure: Unable to establish raw TCP connection to 1.1.1.1")
E   TypeError: Dynamic.description() got an unexpected keyword argument 'message'
```
---

**🔴 Verify Raw TCP/IP Socket Connectivity**
>   
        Detailed Validation of the Container's TCP/IP Stack:  
        1. Attempts to establish a raw socket connection to a known public IP (1.1.1.1).  
        2. Bypasses DNS resolution to isolate the network stack's ability to create and manage TCP sessions.  
        3. Verifies that the FIPS-enabled OpenSSL client can correctly initialize a handshake over raw IP sockets.  
        4. Monitors for 'Network is unreachable' or 'Connection refused' errors at the kernel interface level.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:40: in test_tcp_connectivity
    allure.dynamic.description(message="Network Failure: Unable to establish raw TCP connection to 1.1.1.1")
E   TypeError: Dynamic.description() got an unexpected keyword argument 'message'
```
---



<br>

### 📁 tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking

| Status | Test Case | Duration |
| :---: | :--- | :---: |
| ❌ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `12ms` |
| ❌ | **Verify Blocking of Insecure TLS 1.0/1.1 Protocols**<br><sub>tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking</sub> | `13ms` |



#### 🔻 Failure Analysis for tests.test_11_network_tls.TestNetworkAndTLS#test_tls_legacy_protocol_blocking


**🔴 Verify Blocking of Insecure TLS 1.0/1.1 Protocols**
>   
        Validates the mandatory retirement of legacy cryptographic protocols:  
        1. Attempts to initiate a TLS 1.0 handshake with an external endpoint (google.com).  
        2. Confirms that the FIPS-enabled TLS stack strictly prohibits the use of TLS 1.0/1.1.  
        3. Ensures that the system returns a protocol-level error instead of falling back to insecure versions.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:235: in test_tls_legacy_protocol_blocking
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Unexpected error message during TLS 1.0 rejection: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestNetworkAndTLS.test_tls_legacy_protocol_blocking.<locals>.<genexpr> at 0x7f5064ced700>)
```
---

**🔴 Verify Blocking of Insecure TLS 1.0/1.1 Protocols**
>   
        Validates the mandatory retirement of legacy cryptographic protocols:  
        1. Attempts to initiate a TLS 1.0 handshake with an external endpoint (google.com).  
        2. Confirms that the FIPS-enabled TLS stack strictly prohibits the use of TLS 1.0/1.1.  
        3. Ensures that the system returns a protocol-level error instead of falling back to insecure versions.  
    

**Trace:**
```text
tests/tests/test_11_network_tls.py:235: in test_tls_legacy_protocol_blocking
    assert any(indicator in error_msg for indicator in rejection_indicators), \
E   AssertionError: Unexpected error message during TLS 1.0 rejection: unknown flag: --user
E     
E     Usage:  docker [OPTIONS] COMMAND [ARG...]
E     
E     Run 'docker --help' for more information
E     
E   assert False
E    +  where False = any(<generator object TestNetworkAndTLS.test_tls_legacy_protocol_blocking.<locals>.<genexpr> at 0x7f21cde3a0c0>)
```
---



<br>



*Automated by scripts/generate_docs_tests.py*