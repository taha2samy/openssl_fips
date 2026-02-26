# :material-shield-check: Wolfi OpenSSL FIPS Dashboard

**A High-Assurance, Cryptographically Hardened Foundation for Cloud-Native Workloads**

---

<div align="center" style="margin-bottom: 20px;">
  <!-- Dynamic Test Badges -->
  <a href="compliance/fips-audit/"><img src="https://img.shields.io/badge/FIPS_Audit_Passed-{{ test_stats.passed }}-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Passed" /></a>
  <a href="compliance/fips-audit/"><img src="https://img.shields.io/badge/FIPS_Audit_Failed-{{ test_stats.failed }}-{{ test_badge_color }}?style=for-the-badge&logo=githubactions&logoColor=white" alt="Failed" /></a>
  <a href="compliance/fips-audit/"><img src="https://img.shields.io/badge/Total_Vectors-{{ test_stats.total }}-blue?style=for-the-badge" alt="Total" /></a>
</div>

<div align="center">
  <!-- Dynamic Build & Security Badges -->
  <a href="{{ registry }}/{{ owner }}/{{ repo_name }}"><img src="https://img.shields.io/badge/OpenSSL-{{ core_version }}-blueviolet?style=flat-square&logo=openssl" alt="OpenSSL Version" /></a>
  <a href="https://csrc.nist.gov/"><img src="https://img.shields.io/badge/NIST_Provider-{{ fips_version }}-blue?style=flat-square&logo=keybase" alt="FIPS Version" /></a>
  <a href="https://github.com/wolfi-dev"><img src="https://img.shields.io/badge/Security-Zero_CVE-blue?style=flat-square&logo=dependabot" alt="Zero CVE" /></a>
  <a href="https://slsa.dev/"><img src="https://img.shields.io/badge/Supply_Chain-SLSA_L3-blueviolet?style=flat-square&logo=linuxfoundation" alt="SLSA Level 3" /></a>
</div>

---

## :octicons-rocket-16: Executive Overview

Welcome to the **Wolfi OpenSSL FIPS** portal. This repository maintains a production-hardened, **FIPS 140-3 compliant** OpenSSL `{{ core_version }}` container ecosystem. Architected exclusively on **[Wolfi OS](https://github.com/wolfi-dev)** (the undisdistro), this project eliminates legacy OS overhead, completely eradicates scanner noise, and ensures a microscopically small attack surface. 

This image is specifically engineered for **Enterprise, FedRAMP, and DoD IL5/IL6** environments where regulatory compliance and absolute cryptographic integrity are non-negotiable.

!!! tip "Continuous Compliance State"
    The metrics and attestations displayed on this portal are not static. They are dynamically generated from our automated test suites. This documentation reflects the state of the codebase as of **{{ generation_date }}** from Commit [`{{ github.commit_sha[:7] }}`](https://github.com/{{ github.repository }}/commit/{{ github.commit_sha }}).

---

## :fontawesome-solid-layer-group: Core Architectural Pillars

Our implementation does not just "add a FIPS flag"; it fundamentally restructures how the cryptographic boundary is enforced.

- **:material-lock-check: Strict Cryptographic Boundaries:** The FIPS provider `{{ fips_version }}` is statically linked and verified via MAC (Message Authentication Code) upon every initialization (Power-On Self-Test).
- **:material-package-variant-closed: Zero-CVE Baseline:** Built entirely from source on Wolfi OS. We use a custom, hermetic Python engine (`wolfi-pkg-updater`) to track upstream GLIBC and ZLIB vulnerabilities autonomously.
- **:material-certificate: SLSA Level 3 Provenance:** Every deployment artifact is cryptographically signed using Sigstore/Cosign. Attackers cannot inject malicious binaries into this supply chain.
- **:material-speedometer: Negligible Performance Tax:** Optimized assembly pathways ensure that utilizing the FIPS provider incurs near-zero latency overhead compared to the standard OpenSSL engine.

---

## :material-server-network: Deployment Artifacts & Quick Start

We compile and attest three distinct image variants, designed to cater to different stages of your Software Development Life Cycle (SDLC). 

Choose the variant that best fits your operational requirements:

=== ":material-shield-star: Distroless (Production)"

    **The Ultimate Hardened Target:** Contains no shell (`/bin/sh` is missing), no package manager, and no unnecessary OS libraries. This is the pure cryptographic engine intended for production microservices.
    
    ```bash
    # Pull the production-ready, attested distroless image
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}-distroless@{{ distroless_digest }}
    ```
    
    * **:material-file-document-check: Provenance:** [View SLSA L3 Attestation]({{ distroless_url }})
    * **:material-barcode-scan: SBOM:** [Download CycloneDX JSON]({{ distroless_sbom_url }})

=== ":material-console: Standard (CI/CD Debug)"

    **Optimized for Observability:** Includes standard POSIX utilities and a `/bin/bash` shell. Intended for local debugging, pipeline execution, or environments where interactive inspection of the cryptographic state is required.
    
    ```bash
    # Pull the standard debug environment
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}@{{ standard_digest }}
    ```
    
    * **:material-file-document-check: Provenance:** [View SLSA L3 Attestation]({{ standard_url }})
    * **:material-barcode-scan: SBOM:** [Download CycloneDX JSON]({{ standard_sbom_url }})

=== ":material-hammer-wrench: Development (SDK)"

    **The Builder's Foundation:** Shipped with `build-base`, `linux-headers`, and `pkgconf`. Use this image as a multi-stage builder to compile your C/C++ or Rust applications against the validated FIPS module.
    
    ```bash
    # Pull the development and compilation toolkit
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}-dev@{{ dev_digest }}
    ```
    
    * **:material-file-document-check: Provenance:** [View SLSA L3 Attestation]({{ dev_url }})
    * **:material-barcode-scan: SBOM:** [Download CycloneDX JSON]({{ dev_sbom_url }})

---

## :material-check-decagram: Cryptographic Verification Protocol

Trust is good, but mathematical verification is better. Before deploying these images to your infrastructure, we strongly recommend verifying the OIDC identity and cryptographic signature of the artifact using **Cosign**.

```bash
# Verify the integrity and source identity of the FIPS image
cosign verify \
  --certificate-identity-regexp "^https://github.com/{{ owner }}/.*" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}
```
# :material-test-tube: Distroless Image Validation Report

This report contains the automated security and functional testing results for the **Wolfi OpenSSL FIPS (Distroless)** image. The tests are executed automatically in an isolated CI/CD environment.

---

<span style="font-size: 2.5em; font-weight: 900; color: var(--md-code-hl-keyword-color);">
</span>
