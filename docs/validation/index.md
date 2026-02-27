# :material-certificate-outline: Automated Validation Overview

This section documents our comprehensive multi-tier security verification process. Our strategy ensures that the FIPS cryptographic boundary and container hardening remain intact across all distributed variants.

---

## :material-chart-timeline-variant: Real-Time Validation Status

<div class="grid cards" markdown>

-   :material-magnify-scan: **Static Analysis (SAST)**
    ---
    **KICS Security Scan**
    {% if kics_report.total_counter == 0 -%}
    [:material-check-circle:{ .md-typeset__success } **Clean Audit**](./static-analysis/kics-report.md)
    {% else -%}
    [:material-alert-circle:{ .md-typeset__error } **{{ kics_report.total_counter }} Issues Found**](./static-analysis/kics-report.md)
    {% endif -%}
    *Dockerfile & IaC Security*

-   :material-test-tube: **Functional Core**
    ---
    **Standard & Development**
    {% if standard_report_FIPS_validation.summary.failed == 0 -%}
    [:material-check-circle:{ .md-typeset__success } **Boundary Intact**](./functional-tests/standard-image.md)
    {% else -%}
    [:material-close-circle:{ .md-typeset__error } **{{ standard_report_FIPS_validation.summary.failed }} Failed**](./functional-tests/standard-image.md)
    {% endif -%}
    *FIPS Provider & Logic Integrity*

-   :material-package-variant-closed: **Distroless Runtime**
    ---
    **Production Hardened**
    {% if distroless_report_FIPS_validation.summary.failed == 0 -%}
    [:material-check-circle:{ .md-typeset__success } **Validated**](./functional-tests/distroless-image.md)
    {% else -%}
    [:material-close-circle:{ .md-typeset__error } **{{ distroless_report_FIPS_validation.summary.failed }} Failed**](./functional-tests/distroless-image.md)
    {% endif -%}
    *Attack Surface Reduction*

-   :material-shield-check: **Enterprise Compliance**
    ---
    **Standard Image Metrics**
    {% set standard_vulns = standard_compliance.security_scan.Results[0].Vulnerabilities | default([]) | length %}
    {% if standard_vulns == 0 -%}
    [:material-shield-check:{ .md-typeset__success } **Compliant**](./compliance/standard/vulnerability.md)
    {% else -%}
    [:material-shield-alert:{ .md-typeset__error } **Action Required**](./compliance/standard/vulnerability.md)
    {% endif -%}
    *Trivy / CIS / NSA / PSS*

</div>

---

!!! failure "IMPORTANT: OpenSSL SBOM Visibility & Integrity"
    **Architectural Notice:** When auditing the **Software Bill of Materials (SBOM)** or **Vulnerability Scans**, the `OpenSSL` package will **not** appear as a standard OS package (e.g., via `apk`). 
    
    **The Core Principle:** To ensure absolute cryptographic integrity and FIPS 140-3 boundary enforcement, this project **builds OpenSSL Core and the FIPS Provider from validated source code** during the build process. They are integrated as static/shared integrals rather than ephemeral system packages. This prevents upstream repository tampering and is the primary reason this project exists.

---

## :material-file-tree: Detailed Audit Reports

### :material-gavel: 1. Functional Logic Audits
Verifying the internal cryptographic logic and FIPS provider state machine.

- :material-file-document: [Standard & Development Core Functional Audit](./functional-tests/standard-image.md)
- :material-file-document: [Distroless Production Functional Audit](./functional-tests/distroless-image.md)

### :material-shield-check: 2. Enterprise Compliance Hub
Detailed reports covering Vulnerabilities, Docker CIS, NSA Hardening, and K8s PSS Restricted.

=== ":material-monitor-dashboard: Standard Image"
    - :material-shield-sync: [Security & Vulnerability Scan](./compliance/standard/vulnerability.md)
    - :material-docker: [CIS Docker Benchmark](./compliance/standard/docker-cis.md)
    - :material-kubernetes: [NSA Kubernetes Hardening](./compliance/standard/k8s-nsa.md)
    - :material-gavel: [K8s PSS Restricted Compliance](./compliance/standard/k8s-pss.md)

=== ":material-shield-star: Distroless Image"
    - :material-shield-sync: [Security & Vulnerability Scan](./compliance/distroless/vulnerability.md)
    - :material-docker: [CIS Docker Benchmark](./compliance/distroless/docker-cis.md)
    - :material-kubernetes: [NSA Kubernetes Hardening](./compliance/distroless/k8s-nsa.md)
    - :material-gavel: [K8s PSS Restricted Compliance](./compliance/distroless/k8s-pss.md)

=== ":material-hammer-wrench: Development SDK"
    - :material-shield-sync: [Security & Vulnerability Scan](./compliance/development/vulnerability.md)
    - :material-docker: [CIS Docker Benchmark](./compliance/development/docker-cis.md)
    - :material-kubernetes: [NSA Kubernetes Hardening](./compliance/development/k8s-nsa.md)
    - :material-gavel: [K8s PSS Restricted Compliance](./compliance/development/k8s-pss.md)

### :material-magnify-scan: 3. Infrastructure SAST
- :material-file-search: [IaC Static Analysis (KICS)](./static-analysis/kics-report.md)

---
[:material-arrow-up: Back to Top](#automated-validation-overview)