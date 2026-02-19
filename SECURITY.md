
# Security Policy: Wolfi OpenSSL FIPS

This project is not just a container image; it is a **fully automated, high-assurance cryptographic supply chain**. Our security posture is engineered from the ground up to meet **SLSA Level 3** standards, ensuring every artifact is verifiable, reproducible, and secure by design.

## 01. The Hermetic Build System (SLSA Level 3)
Our core security guarantee comes from our **Hermetic Build** philosophy. We eliminate supply chain risks by design:
*   **Zero External Dependencies at Build Time:** The CI/CD pipeline does **not** pull "latest" tags or un-versioned dependencies. The repository is the **Single Source of Truth**, containing pinned image digests and package versions in `versions.hcl`.
*   **Byte-for-Byte Reproducibility:** Any build triggered from a specific commit is guaranteed to produce an identical artifact. This prevents build-time injection attacks and ensures that what you audit is what you run.
*   **SLSA Provenance:** Every build generates a non-falsifiable SLSA Level 3 attestation. This allows you to cryptographically verify the entire build lifecycle—from the source code commit to the final container image digest.

## 02. The Autonomous Security Lifecycle
Human intervention is a liability. We have engineered an autonomous system to maintain a **Zero-CVE** state:
*   **Autonomous Upstream Ingestion:** Our engine (`wolfi-pkg-updater.py`) continuously monitors Chainguard's Wolfi repositories for security patches and new base image digests.
*   **Automated Version Pinning:** Upon detecting an upstream security update (e.g., in `libc` or `zlib`), the engine automatically commits the new, secure version to `versions.hcl`. This action creates a new, auditable "snapshot of truth".
*   **Continuous Verification Pipeline:** This commit triggers our full 200+ point Pytest compliance suite. An image is only released if it passes every FIPS boundary and integrity test. This is a **zero-touch, zero-trust** workflow.

## 03. Runtime Integrity & FIPS Enforcement
The security guarantees are not just at build time; they are enforced at runtime:
*   **FIPS Self-Tests (POST/KAT):** The FIPS provider is configured with `security-checks = 1`. On startup, it performs mandatory Power-On Self-Tests. Any failure (e.g., a corrupted binary) causes the module to enter a "Fatal Error" state, blocking all cryptographic operations.
*   **Tamper Resistance:** The `fipsmodule.cnf` contains a cryptographic MAC of the `fips.so` provider. If the binary is tampered with, the MAC verification will fail, and the FIPS module will refuse to load.

## 04. Reporting a Vulnerability
Given the automated and transparent nature of this project, we are most interested in vulnerabilities that represent a bypass of our core security principles:
*   A flaw in the FIPS provider configuration that allows a non-approved algorithm.
*   A way to break the hermetic build environment.
*   A bypass of our automated compliance test suite.

Please report any findings privately via [GitHub Security Advisories](https://github.com/taha2samy/openssl_fips/security/advisories/new).


