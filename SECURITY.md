
# Security Policy: Wolfi OpenSSL FIPS

This project is a high-assurance, community-driven cryptographic foundation. Our security posture is defined by **Apache 2.0 transparency**, an **Autonomous Security Lifecycle**, and strict **Hermetic Build Integrity**.

## 01. Open-Source Transparency (Apache 2.0)
As a community-focused project licensed under **Apache 2.0**, we believe that security through obscurity is a flaw. 
*   **Audit-Ready Code:** Every build script, test vector, and configuration is open for public audit.
*   **Community Trust:** By making our compliance suite public, we allow the community to verify that our FIPS 140-3 boundaries are as robust as we claim.

## 02. The Autonomous Security Lifecycle
The core of this project is its **Full Automation**. We have eliminated human error from the critical security path:
*   **Autonomous Ingestion:** Our engine (`wolfi-pkg-updater.py`) automatically tracks upstream Chainguard/Wolfi updates.
*   **Automated Verification:** No image is released without passing our 200+ point Pytest compliance suite. If a single test fails (e.g., a non-FIPS algorithm is accidentally enabled), the entire pipeline halts.
*   **Continuous Patching:** The project lives in a state of continuous improvement, where security patches are ingested, tested, and released through a zero-touch automated workflow.

## 03. Hermetic Build Philosophy (SLSA L3)
To ensure absolute supply chain integrity, we implement a **Hermetic Build** model:
*   **Deterministic Snapshots:** We do not use "latest" tags. All dependencies are pinned via image digests and package versions in `versions.hcl`.
*   **Self-Contained Logic:** The repository is the **Single Source of Truth**. Any build triggered from a specific commit will yield an identical, byte-for-byte reproducible artifact.
*   **Cryptographic Attestation:** Every automated release includes a SLSA Level 3 provenance and a signed SBOM (Software Bill of Materials).

## 04. Reporting a Vulnerability
In a community project, security is a shared responsibility. If you find a way to bypass our cryptographic boundaries, please report it via our private channels.

**How to report:**
*   **Private Disclosure:** Use [GitHub Security Advisories](https://github.com/taha2samy/openssl_fips/security/advisories/new).
*   **Response Time:** Initial triage within 48 hours.

## 05. Runtime Integrity & Enforcement
*   **FIPS Self-Tests:** The module performs mandatory self-integrity checks (POST/KAT) on startup.
*   **Tamper Resistance:** The engine detects unauthorized modifications to `fipsmodule.cnf` via MAC verification and will block all cryptographic services if tampering is detected.

---
*Powered by Open Source | Secured by Automation | Verified by FIPS 140-3 Compliance Suite.*
