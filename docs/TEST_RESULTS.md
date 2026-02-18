# 🛡️ FIPS Compliance Audit Report

> **Generated on:** 2026-02-18 19:33:17 UTC  
> **Status:** ![Status](https://img.shields.io/badge/tests-passed%200-brightgreen)


## 📋 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Build Configuration](#-build-configuration)
3. [Supply Chain & Packages](#-supply-chain--packages)
4. [Test Results Detail](#-test-results-detail)


## 📊 Executive Summary

| Metric | Count | Status |
| :--- | :---: | :--- |
| **Total Tests** | `0` | 🔍 Scoped |
| **Passed** | `0` | ✅ Passing |
| **Failed** | `0` | ❌ Critical |
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











*Automated by scripts/generate_docs_tests.py*