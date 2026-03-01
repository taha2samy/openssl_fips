# Wolfi OpenSSL FIPS
### High-Assurance Cryptographic Foundation

This project provides a production-hardened, FIPS 140-3 validated OpenSSL environment built on the Wolfi ecosystem. It is engineered for Zero-Trust environments, strict cryptographic compliance, and verifiable supply chain integrity.

---

## Live Security Dashboard & Reports
All technical details, including vulnerability audits, FIPS functional test results, performance benchmarks, and compliance matrices (CIS, NSA, PSS), are available at:

👉 **[https://taha2samy.github.io/openssl_fips/](https://taha2samy.github.io/openssl_fips/)**

**Important:** Before pulling or deploying any artifacts, please review the live dashboard to verify the current security posture and cryptographic integrity of the latest build.

---

## Core Features
*   **SLSA Level 3 Compliance:** Every build includes verifiable provenance and a signed CycloneDX SBOM.
*   **FIPS 140-3 Integrity:** Automated boundary verification via KAT (Known Answer Tests) and POST (Power-On Self-Tests).
*   **Zero-CVE Policy:** Built on Wolfi to ensure a minimal attack surface and rapid security patching.
*   **Operational Parity:** Local development is synchronized with CI/CD execution using Taskfile and Docker-wrapped tooling.

---


## Operations
The project lifecycle is managed via Taskfile. Refer to the **Operational Excellence Guide** on the dashboard for instructions on setup, auditing, and local documentation rendering.



**License:** Apache-2.0  
