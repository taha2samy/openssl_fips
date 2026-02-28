---
hide:
  - navigation
  - toc
---

<style>
  [data-md-color-scheme="slate"] .openssl-logo {
    filter: brightness(0) invert(1) hue-rotate(180deg) saturate(100%) brightness(1.5);
  }

  .md-typeset h1 {
    font-weight: 900;
    letter-spacing: -1px;
  }

  .md-typeset h2 .twemoji,
  .md-typeset h2 svg {
    width: 1.3em;
    height: 1.3em;
    vertical-align: middle;
  }

  .md-typeset li .twemoji,
  .md-typeset li svg {
    width: 1.2em;
    height: 1.2em;
    vertical-align: middle;
  }

  .hero-desc {
    font-size: 1.15em;
    line-height: 1.8;
    text-align: center;
    max-width: 860px;
    margin: 20px auto 40px auto;
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 24px;
    margin: 30px 0 50px 0;
  }

  .card {
    padding: 28px;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 16px;
    background: var(--md-default-bg-color);
    transition: box-shadow 0.2s, transform 0.2s;
  }

  .card:hover {
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    transform: translateY(-2px);
  }

  .card-icon {
    font-size: 2.2em;
    margin-bottom: 12px;
    line-height: 1;
  }

  .card-title {
    font-size: 1.1em;
    font-weight: 700;
    margin: 0 0 10px 0;
    color: #326ce5;
  }

  .card-body {
    font-size: 0.95em;
    line-height: 1.7;
    opacity: 0.82;
    margin: 0;
  }

  .contribution-box {
    margin-top: 50px;
    padding: 36px 40px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(50,108,229,0.07) 0%, rgba(103,58,183,0.07) 100%);
    border: 2px solid #326ce5;
  }

  .bug-card {
    margin: 24px 0;
    padding: 20px 24px;
    background: var(--md-default-bg-color);
    border-left: 8px solid #673ab7;
    border-radius: 6px;
  }

  .bug-link {
    display: inline-block;
    margin-top: 10px;
    font-size: 1.05em;
    font-weight: 800;
    color: #673ab7 !important;
    text-decoration: none;
  }

  .bug-link:hover { text-decoration: underline; }

</style>





<div align="center">
  <img src="https://raw.githubusercontent.com/wolfi-dev/.github/main/profile/wolfi-logo-light-mode.svg#only-light" width="180" alt="Wolfi Linux">
  <img src="https://raw.githubusercontent.com/wolfi-dev/.github/main/profile/wolfi-logo-dark-mode.svg#only-dark" width="180" alt="Wolfi Linux">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://openssl-library.org/images/openssl_logo_library.svg" width="220" alt="OpenSSL" class="openssl-logo">
</div>

# :material-shield-check: Wolfi OpenSSL FIPS { align="center" }
### High-Assurance Cryptographic Infrastructure { align="center" }


<div align="center" style="margin: 14px 0 10px 0;">
  <img src="https://img.shields.io/badge/Architecture-AMD64-0078D4?style=for-the-badge&logo=intel&logoColor=white" alt="AMD64">
  &nbsp;
  <img src="https://img.shields.io/badge/Architecture-ARM64-37AD4B?style=for-the-badge&logo=arm&logoColor=white" alt="ARM64">
</div>

Welcome to the production-ready, **FIPS 140-3** validated OpenSSL environment. Built exclusively on top of the hardened, un-distro Wolfi ecosystem, this project is engineered from the ground up for Zero-Trust environments, strict cryptographic compliance boundaries, and immutable cloud-native workloads.
{: .hero-desc }

---



<div align="center" style="margin-top: 100px; margin-bottom: 50px;">
  <h1 style="font-size: 3.5em; font-weight: 900; margin: 0; color: var(--md-primary-fg-color);">DEPLOYMENT ARTIFACTS</h1>
  <p style="font-size: 1.8em; font-weight: 300; opacity: 0.8;">Verified Production Runtimes & SDKs</p>
</div>

<div class="hero-desc" markdown="1">
We compile and attest three distinct image variants, designed to cater to different stages of your Software Development Life Cycle (SDLC). Select the variant that matches your operational and security requirements.
</div>

---

## :material-package-variant: Artifact Tiers & Quick Start

=== ":material-shield-star: Production Distroless"

    !!! success "The Ultimate Hardened Target"
        **Security Profile:** Zero-entry surface. No shell (`/bin/sh` is missing), no package manager, and no unnecessary OS libraries. Intended for high-security production microservices.

    <div style="font-size: 1.2em;" markdown="1">
    ```bash
    # Pull the production-ready, attested Distroless image
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}-distroless
    ```
    </div>

    **Verifiable Metadata:**
    *   **:material-file-document-check: L3 Provenance:** [View Attestation]({{ distroless_url }})
    *   **:material-barcode-scan: CycloneDX SBOM:** [Download JSON]({{ distroless_sbom_url }})
    *   **:material-tag-outline: Additional Tags:** `distroless`

=== ":material-console: Standard Image"

    !!! info "Optimized for Observability"
        **Security Profile:** Balanced hardening. Includes standard POSIX utilities and a `/bin/bash` shell. Intended for CI/CD pipeline execution and environments requiring interactive inspection.

    <div style="font-size: 1.2em;" markdown="1">
    ```bash
    # Pull the standard runtime and debugging environment
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}
    ```
    </div>

    **Verifiable Metadata:**
    *   **:material-file-document-check: L3 Provenance:** [View Attestation]({{ standard_url }})
    *   **:material-barcode-scan: CycloneDX SBOM:** [Download JSON]({{ standard_sbom_url }})
    *   **:material-tag-outline: Additional Tags:** `latest`

=== ":material-hammer-wrench: Development SDK"

    !!! warning "The Builder's Foundation"
        **Security Profile:** Functional parity with Standard. Includes `build-base`, `headers`, and `pkgconf`. Designed to be used as a multi-stage builder to compile apps against the FIPS boundary.

    <div style="font-size: 1.2em;" markdown="1">
    ```bash
    # Pull the development toolchain and compilation toolkit
    docker pull {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}-dev
    ```
    </div>

    **Verifiable Metadata:**
    *   **:material-file-document-check: L3 Provenance:** [View Attestation]({{ dev_url }})
    *   **:material-barcode-scan: CycloneDX SBOM:** [Download JSON]({{ dev_sbom_url }})
    *   **:material-tag-outline: Additional Tags:** `dev`

---

## :material-identifier: Image Tagging Reference

The following tags are maintained and updated automatically by our **SLSA L3 pipeline** for every release of OpenSSL `{{ core_version }}`.

| Artifact Variant | Version-Specific Tag | Alias / Floating Tag |
| :--- | :--- | :--- |
| **Standard Image** | `{{ core_version }}` | `latest` |
| **Distroless Runtime** | `{{ core_version }}-distroless` | `distroless` |
| **Development SDK** | `{{ core_version }}-dev` | `dev` |

---





## <img src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/trivy.png" width="55" align="top"> Continuous Compliance Engine (Trivy)

Our verification engine leverages **Trivy** to enforce a Zero-CVE posture and strict operational hardening across all image variants. Every build is cross-referenced against global security benchmarks.

<div class="card-grid" markdown="1">

<!-- Card 1: Vulnerability -->
<div class="card" markdown="1">
### :material-shield-bug: Vulnerability & SBOM Audit
<div class="card-body" markdown="1">
{% set std_results = standard_compliance.get('security_scan', {}).get('Results', [{}]) -%}
{% set std_vulns = std_results[0].get('Vulnerabilities', []) | length -%}
{% if std_vulns == 0 -%}
[:material-check-decagram:{ .md-typeset__success } **Zero-CVE Verified**](validation/compliance/standard/vulnerability.md)
{% else -%}
[:material-alert-rhombus:{ .md-typeset__error } **{{ std_vulns }} CVEs Detected**](validation/compliance/standard/vulnerability.md)
{% endif %}

*   [:material-arrow-right: **Distroless Report**](validation/compliance/distroless/vulnerability.md)
*   [:material-arrow-right: **Standard Report**](validation/compliance/standard/vulnerability.md)
*   [:material-arrow-right: **Development Report**](validation/compliance/development/vulnerability.md)

</div>
</div>

<!-- Card 2: CIS Docker -->
<div class="card" markdown="1">
### :material-docker: CIS Docker Benchmarks
<div class="card-body" markdown="1">
Static analysis of Docker runtime security and host-level best practices.

*   [:material-arrow-right: **Standard**](validation/compliance/standard/docker-cis.md)
*   [:material-arrow-right: **Distroless**](validation/compliance/distroless/docker-cis.md)
*   [:material-arrow-right: **Development**](validation/compliance/development/docker-cis.md)
</div>
</div>

<!-- Card 3: NSA/CISA -->
<div class="card" markdown="1">
### :material-kubernetes: NSA/CISA Hardening
<div class="card-body" markdown="1">
Validating infrastructure isolation and Kubernetes threat mitigation.

*   [:material-arrow-right: **Standard**](validation/compliance/standard/k8s-nsa.md)
*   [:material-arrow-right: **Distroless**](validation/compliance/distroless/k8s-nsa.md)
*   [:material-arrow-right: **Development**](validation/compliance/development/k8s-nsa.md)
</div>
</div>

<!-- Card 4: K8s PSS -->
<div class="card" markdown="1">
### :material-gavel: K8s PSS Restricted
<div class="card-body" markdown="1">
Verification of the highest cluster-level workload isolation standards.

*   [:material-arrow-right: **Standard**](validation/compliance/standard/k8s-pss.md)
*   [:material-arrow-right: **Distroless**](validation/compliance/distroless/k8s-pss.md)
*   [:material-arrow-right: **Development**](validation/compliance/development/k8s-pss.md)
</div>
</div>

</div>

---


## <img src="https://www.kics.io/wp-content/uploads/2022/11/icon.svg" width="70" align="top"> Infrastructure SAST (KICS)

<div class="hero-desc" markdown="1">
Security begins at the architecture level. We employ **KICS (Keeping Infrastructure as Code Secure)** to perform deep static analysis on our `Dockerfile` and HCL files CI/CD pipelines, ensuring zero misconfigurations are injected into the build environment.
</div>

<div class="contribution-box" style="text-align: center; margin-bottom: 50px;" markdown="1">

{% set kics_total = kics_report.get('total_counter', 0) -%}
{% if kics_total == 0 -%}
### :material-check-decagram:{ .md-typeset__success } **STATUS: PRISTINE INFRASTRUCTURE**
Infrastructure code adheres to 100% of the defined security best practices.
{% else -%}
### :material-alert-circle:{ .md-typeset__error } **STATUS: {{ kics_total }} SECURITY RISKS IDENTIFIED**
Static analysis has flagged configuration anomalies in the build layers.
{% endif %}

<br>

[:material-text-box-search-outline: **OPEN FULL KICS AUDIT REPORT**](validation/static-analysis/kics-report.md){ .md-button .md-button--primary style="font-size: 1.2em; font-weight: 700; border-radius: 50px; padding: 10px 30px;" }

</div>

---





# :material-link-lock: Supply Chain Integrity { align="center" }
### SLSA Level 3 Compliant & Verified { align="center" }

<div align="center" style="margin-top: 60px;">
  <img src="https://icon.icepanel.io/Technology/svg/GitHub-Actions.svg" width="80" alt="GitHub Actions">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://slsa.dev/images/badge-exploded.svg" width="130" alt="SLSA Level 3">
</div>


<div class="hero-desc" markdown="1">
We enforce absolute cryptographic provenance. Every build is governed by strict dependency pinning, signed via **Sigstore/OIDC**, and accompanied by a verifiable **CycloneDX SBOM** (Software Bill of Materials).
</div>

<div class="card-grid" markdown="1">

<div class="card" markdown="1">
### :material-pin-outline: Immutable Dependencies
<div class="card-body">
Every base image and package is pinned by <b>SHA256 digest</b> in <code>versions.hcl</code>. This ensures byte-for-byte reproducibility and prevents "upstream poisoning" attacks.
</div>
</div>

<!-- Pillar 2: Provenance -->
<div class="card" markdown="1">
### :material-fingerprint: Verified Provenance
<div class="card-body">
Cryptographically signed build logs that prove exactly which Git Commit produced the specific image digest you are running.
</div>
</div>

<!-- Pillar 3: SBOM -->
<div class="card" markdown="1">
### :material-file-document-check: CycloneDX SBOM
<div class="card-body">
A complete inventory listing every library, header, and compiler version used to construct the FIPS cryptographic boundary.
</div>
</div>

</div>

---

### :material-certificate: Cryptographic Attestations
*Publicly verifiable trust bundles for every artifact variant.*

| Artifact Variant | L3 Provenance Link | SBOM Download |
| :--- | :--- | :--- |
| **Distroless Runtime** | [:material-link: View Attestation]({{ distroless_url }}) | [:material-download: CycloneDX JSON]({{ distroless_sbom_url }}) |
| **Standard Image** | [:material-link: View Attestation]({{ standard_url }}) | [:material-download: CycloneDX JSON]({{ standard_sbom_url }}) |
| **Development SDK** | [:material-link: View Attestation]({{ dev_url }}) | [:material-download: CycloneDX JSON]({{ dev_sbom_url }}) |

---









<div align="center" style="margin-top: 100px; margin-bottom: 30px;">
  <div style="display: flex; justify-content: center; align-items: center; gap: 30px; margin-bottom: 20px;">
    <img src="https://raw.githubusercontent.com/wolfi-dev/.github/main/profile/wolfi-logo-light-mode.svg#only-light" width="80" alt="Wolfi">
    <img src="https://raw.githubusercontent.com/wolfi-dev/.github/main/profile/wolfi-logo-dark-mode.svg#only-dark" width="80" alt="Wolfi">
    <span style="font-size: 2.5em; color: var(--md-default-fg-color--light); font-weight: 300;">VS</span>
    <img src="https://icon.icepanel.io/Technology/svg/Ubuntu.svg" width="60" title="Ubuntu">
    <img src="https://icon.icepanel.io/Technology/svg/Debian.svg" width="60" title="Debian">
    <img src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/alpine-linux.svg" width="60" title="Alpine">
  </div>
</div>

# :material-speedometer: Performance Velocity { align="center" }
### High-Speed Cryptography & Ecosystem Benchmarks { align="center" }


<div class="hero-desc" style="text-align: center;" markdown="1">
High-assurance security does not require a performance penalty. By utilizing **Wolfi's rolling-release architecture** and **OpenSSL {{ core_version }}**, our FIPS-validated module consistently achieves parity with, or outperforms, unhardened packages in legacy LTS distributions.
</div>

<br>

<div class="card-grid" markdown="1">

<!-- Optimization Insight -->
<div class="card" markdown="1">
### :material-lightning-bolt: Zero FIPS Penalty
<div class="card-body">
The Wolfi-FIPS module proves that rigorous integrity checks do not slow down your data. By leveraging <b>AVX/AVX2</b> instruction sets, we maintain peak velocity for bulk encryption and hashing.
</div>
</div>

<!-- Architecture Insight -->
<div class="card" markdown="1">
### :material-trending-up: Ecosystem Optimization
| Unlike legacy distros that pin older OpenSSL branches, Wolfi tracks modern upstream optimizations, providing immediate access to hardware acceleration features (AES-NI) for production workloads.
</div>

</div>

[:material-chart-areaspline: **VIEW FULL COMPARATIVE PERFORMANCE AUDIT**](performance/benchmarks.md){ .md-button .md-button--primary }


---


<br><br>



<div align="center" style="margin-top: 100px; margin-bottom: 40px;">
  <img src="https://www.safelogic.com/hs-fs/hubfs/FIPS-140-3-Validated-Badge%20426x500.png?width=318&height=373" width="180" alt="FIPS 140-3 Validated">
</div>`

# :material-shield-lock: FIPS Functional Integrity { align="center" }
### Boundary Verification & State Machine Logic { align="center" }

<div class="hero-desc" markdown="1">
To ensure the cryptographic state-machine operates within strict **FIPS 140-3** parameters, we execute automated **Known Answer Tests (KAT)** and **Power-On Self-Tests (POST)** directly against the verified production binaries.
</div>

<div class="card-grid" markdown="1">

<!-- Standard Variant Audit -->
<div class="card" markdown="1">
## :material-console: Standard Image Audit
<div class="card-body" markdown="1">
{% set std_f = standard_report_FIPS_validation.get('summary', {}).get('failed', 'N/A') -%}
{% if std_f == 0 -%}
<span style="color:#00c853; font-weight:900; font-size: 1.2em;">:material-check-decagram: LOGIC VALIDATED</span>
{% else -%}
<span style="color:#d50000; font-weight:900; font-size: 1.2em;">:material-alert-circle: {{ std_f }} VIOLATIONS</span>
{% endif %}

[View Forensic Functional Report](validation/functional-tests/standard-image.md)
</div>
</div>

<!-- Distroless Variant Audit -->
<div class="card" markdown="1">
## :material-package-variant-closed: Distroless Image Audit
<div class="card-body" markdown="1">
{% set dist_f = distroless_report_FIPS_validation.get('summary', {}).get('failed', 'N/A') -%}
{% if dist_f == 0 -%}
<span style="color:#00c853; font-weight:900; font-size: 1.2em;">:material-check-decagram: BOUNDARY VERIFIED</span>
{% else -%}
<span style="color:#d50000; font-weight:900; font-size: 1.2em;">:material-alert-circle: {{ dist_f }} VIOLATIONS</span>
{% endif %}

[View Forensic Functional Report](validation/functional-tests/distroless-image.md)
</div>
</div>

</div>

<div class="contribution-box" markdown="1">

## :material-bug-check: Security Contribution

Our rigorous testing methodology goes beyond basic compliance. During the development of this high-assurance infrastructure using **OpenSSL 3.1.2**, we identified and documented a **Critical Logic Flaw** within the official upstream FIPS provider.

!!! info "Technical Distinction"
    This finding represents a **technical logic bug** in the provider's internal state handling. While not classified as a security vulnerability (CVE), its discovery ensures significantly higher reliability for the global OpenSSL ecosystem.

<div class="bug-card" markdown="1">
**Confirmed Upstream Bug Report:**  
*OpenSSL FIPS Provider — Incorrect Boundary Integrity Logic*

[:material-github: **VIEW VERIFIED ISSUE #30012 ON GITHUB**](https://github.com/openssl/openssl/issues/30012){ .bug-link }
</div>


</div>

<br><br><br>

[:material-arrow-up-circle: **Return to Top of Dashboard**](#wolfi-openssl-fips)



















