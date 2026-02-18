# Security Policy: Wolfi OpenSSL FIPS

This project is a high-assurance cryptographic foundation. Security is not just a feature; it is the core objective. As a FIPS 140-3 compliant containerized solution, we adhere to a strict disclosure and remediation process.

## 01. Security Model & Philosophy
Our security posture is built on three pillars:
1.  **Minimal Attack Surface:** Built on Wolfi (Distroless-first), removing shell-access and non-essential binaries.
2.  **Cryptographic Integrity:** Strict enforcement of FIPS 140-3 boundaries; non-compliant algorithms are blocked at the provider level.
3.  **Supply Chain Transparency:** Every build is signed via Sigstore/Cosign and includes a Level 3 SLSA provenance.

## 02. Reporting a Vulnerability
We take every report seriously. If you discover a security vulnerability, please do **not** open a public issue. 

### Reporting Channels:
*   **GitHub Security Advisory:** Please use the [GitHub Advisories](https://github.com/taha2samy/openssl_fips/security/advisories/new) feature to report privately.
*   **Encrypted Email:** For highly sensitive disclosures, contact **[Your Email]**.

## 03. Vulnerability Triage & Response
Once a report is received, the following timeline is initiated:
- **Triage (24-48 hours):** Initial assessment and confirmation of the vulnerability.
- **Remediation (3-7 days):** Development of a fix and internal audit against FIPS 140-3 compliance (to ensure the fix doesn't break the cryptographic boundary).
- **Disclosure:** Public advisory and updated image release with a new SLSA attestation.

## 04. Scope
| Component | Status |
| :--- | :--- |
| **OpenSSL FIPS Provider** | In Scope |
| **Container Configuration (`openssl.cnf`)** | In Scope |
| **Build Pipeline (GitHub Actions)** | In Scope |
| **Wolfi Base Packages** | Out of Scope (Managed by Chainguard/Wolfi) |

## 05. Security Hardening Measures
*   **Zero-CVE Goal:** We rebuild daily to ingest the latest security patches from Wolfi.
-   **Static Analysis:** Every PR undergoes static analysis (SAST) to prevent insecure configuration drifts.
-   **Integrity Self-Tests:** The image will fail to start if the FIPS `module-mac` or `install-status` is compromised.

## 06. Cryptographic Boundary Notice
Any vulnerability reported that involves a "bypass" of the FIPS provider (e.g., successfully running MD5 when FIPS mode is active) is treated as a **Critical** severity (P1) and will trigger an immediate emergency release.

---