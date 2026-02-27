# :material-shield-check: Wolfi OpenSSL FIPS
**Enterprise-Grade Cryptographic Foundation for High-Security Cloud Workloads**

---

<div align="center" style="margin-bottom: 25px;">
  <!-- Tier 1: Real-Time Audit Status (Forced dynamic values) -->
  <p align="center">
    <a href="validation/functional-tests/standard-image/">
      <img src="https://img.shields.io/badge/FIPS_Audit_Passed-{{ test_stats.passed }}-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Passed" />
    </a>
    <a href="validation/functional-tests/standard-image/">
      <img src="https://img.shields.io/badge/Audit_Failed-{{ test_stats.failed }}-{{ test_badge_color }}?style=for-the-badge&logo=githubactions&logoColor=white" alt="Failed" />
    </a>
    <a href="validation/compliance/standard/vulnerability/">
      {# --- Calculate if Zero CVE or not based on standard scan --- #}
      {% set ns_v = namespace(total=0) %}
      {% if standard_compliance.security_scan.Results is defined %}
        {% for res in standard_compliance.security_scan.Results %}
          {% if res.Vulnerabilities is defined %}
            {% set ns_v.total = ns_v.total + res.Vulnerabilities | length %}
          {% endif %}
        {% endfor %}
      {% endif %}
      
      {% if ns_v.total == 0 %}
        <img src="https://img.shields.io/badge/Security_Scan-Zero_CVE-brightgreen?style=for-the-badge&logo=dependabot&logoColor=white" alt="Zero CVE" />
      {% else %}
        <img src="https://img.shields.io/badge/Security_Scan-{{ ns_v.total }}_Issues-red?style=for-the-badge&logo=dependabot&logoColor=white" alt="CVEs Found" />
      {% endif %}
    </a>
  </p>

  <!-- Tier 2: Technical Specifications & Infrastructure -->
  <p align="center">
    <a href="https://github.com/wolfi-dev">
      <img src="https://img.shields.io/badge/Base_OS-Wolfi-blue?style=flat-square&logo=linux&logoColor=white" alt="Wolfi OS" />
    </a>
    <a href="https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282">
      <img src="https://img.shields.io/badge/NIST_Provider-3.1.2-orange?style=flat-square&logo=keybase" alt="NIST Provider" />
    </a>
    <a href="https://slsa.dev/">
      <img src="https://img.shields.io/badge/Supply_Chain-SLSA_L3-blueviolet?style=flat-square&logo=linuxfoundation" alt="SLSA L3" />
    </a>
    <img src="https://img.shields.io/badge/Arch-AMD64%20%7C%20ARM64-lightgrey?style=flat-square&logo=cpu" alt="Multi-Arch" />
    <img src="https://img.shields.io/badge/License-Apache--2.0-lightgrey?style=flat-square" alt="License" />
  </p>
</div>

---
## :octicons-rocket-16: Executive Overview

This repository maintains a production-hardened, **FIPS 140-3 Compliant** OpenSSL ecosystem. Built on **Wolfi OS** (the un-distro), this project is specifically engineered to eliminate legacy OS overhead and provide a **Zero-CVE** baseline for high-assurance environments (FedRAMP, DoD IL5, Financial Services).

### :material-check-decagram: Verified Compliance Baseline
Unlike generic container images, every build of this project is statically audited against:

1.  **FIPS 140-3 Logic:** Mandatory self-tests and cryptographic boundary enforcement via a NIST-validated provider.
2.  **CIS Docker Benchmark:** Hardening of the container runtime and configuration.
3.  **NSA & CISA Hardening:** Adherence to the official "Kubernetes Hardening Guidance."
4.  **K8s PSS Restricted:** Seamless scheduling in namespaces enforcing the strictest pod security standards.

!!! info "Continuous Verification Note"
    This dashboard is not static. All metrics, test results, and compliance scores are generated in real-time from our automated test suite on **{{ generation_date }}** from Commit [`{{ github.commit_sha[:7] }}`](https://github.com/{{ github.repository }}/commit/{{ github.commit_sha }}).





## :fontawesome-solid-layer-group: Core Architectural Pillars

Our implementation does not just "add a FIPS flag"; it fundamentally restructures how the cryptographic boundary is enforced in a containerized environment.

<div class="grid cards" markdown>

-   :material-lock-check: **Strict Cryptographic Boundary**
    ---
    The FIPS provider `{{ fips_version }}` is statically integrated and verified via **HMAC** upon every initialization (Power-On Self-Test). Any tampering with the binary triggers an immediate lockout.

-   :material-package-variant-closed: **Hermetic Build System**
    ---
    Built to **SLSA Level 3** standards. We eliminate supply chain risks by using pinned image digests and specific package versions. No external dependencies are pulled at runtime.

-   :material-shield-sync: **Zero-CVE Baseline**
    ---
    Leveraging the **Wolfi OS** "un-distro" philosophy. By stripping away legacy utilities and a dedicated package manager, we provide the smallest possible attack surface for production workloads.

-   :material-speedometer: **Hardware Optimization**
    ---
    High-performance assembly pathways for **AES-NI (x86)** and **NEON (ARM)** ensure that FIPS compliance incurs near-zero performance overhead compared to unvalidated engines.

</div>

---

## :material-alert-decagram: Architectural Integrity Notice

!!! failure "IMPORTANT: OpenSSL Visibility in SBOM & Scans"
    When you audit the **Software Bill of Materials (SBOM)** or perform a **Vulnerability Scan**, you will notice that `OpenSSL` is **not** listed as a standard OS package (like `apk` or `dpkg`).

    **This is the core foundation of our security model:**
    To ensure absolute cryptographic integrity, we do not trust upstream repository binaries for critical primitives. Instead, this project **builds OpenSSL Core and the FIPS Provider from validated source code** during our hermetic build process. 
    
    They are integrated as **Static/Shared Integrals**, ensuring that the binaries you deploy are identical to those verified in our [Functional Core Audit](validation/functional-tests/standard-image.md). This prevents "Repository Poisoning" and guarantees a hardened cryptographic boundary.

---



## :material-server-network: Deployment Tiers & Artifacts

We provide three specialized variants of the OpenSSL FIPS container, each attested for integrity and optimized for different stages of the Software Development Life Cycle (SDLC).

=== ":material-shield-star: Distroless (Production Target)"

    **The Hardened Baseline:** Contains zero shell, zero package managers, and zero unnecessary OS libraries. This is the **most secure** variant, intended for production microservices to minimize the attack surface.
    
    ```bash
    # Pull the production-ready, attested distroless image
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}-distroless@{{ distroless_digest }}
    ```
    
    *   **:material-file-document-check: SLSA Provenance:** [View L3 Attestation]({{ distroless_url }})
    *   **:material-barcode-scan: Software Bill of Materials:** [Download CycloneDX JSON]({{ distroless_sbom_url }})
    *   **:material-security: Compliance Status:** [:material-check-circle: View Hardening Report](validation/compliance/distroless/vulnerability.md)

=== ":material-console: Standard (CI/CD & Debug)"

    **Optimized for Observability:** Includes standard POSIX utilities and a `/bin/bash` shell. Use this variant in CI/CD pipelines or environments where interactive inspection of the cryptographic state is required.
    
    ```bash
    # Pull the standard debug and verification environment
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}@{{ standard_digest }}
    ```
    
    *   **:material-file-document-check: SLSA Provenance:** [View L3 Attestation]({{ standard_url }})
    *   **:material-barcode-scan: Software Bill of Materials:** [Download CycloneDX JSON]({{ standard_sbom_url }})
    *   **:material-security: Compliance Status:** [:material-check-circle: View Hardening Report](validation/compliance/standard/vulnerability.md)

=== ":material-hammer-wrench: Development (SDK & Multi-Stage)"

    **The Builder Foundation:** Equipped with `build-base`, `linux-headers`, and `pkgconf`. Use this image as a multi-stage builder to compile C/C++, Rust, or Go applications against the validated FIPS module.
    
    ```bash
    # Pull the development and compilation toolkit
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}-dev@{{ dev_digest }}
    ```
    
    *   **:material-file-document-check: SLSA Provenance:** [View L3 Attestation]({{ dev_url }})
    *   **:material-barcode-scan: Software Bill of Materials:** [Download CycloneDX JSON]({{ dev_sbom_url }})
    *   **:material-security: Compliance Status:** [:material-check-circle: View Hardening Report](validation/compliance/development/vulnerability.md)

---