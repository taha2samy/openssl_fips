# :material-shield-lock-outline: Security Validation Dashboard

This dashboard provides a high-fidelity overview of our automated verification pipeline. We employ a multi-layered defense-in-depth strategy to ensure that the **FIPS 140-3** cryptographic boundary and container hardening remain uncompromised across all distributed artifacts.

---

## :material-pulse: Real-Time Pipeline Status

<div class="grid cards" markdown>

-   :material-magnify-scan:{ .md-typeset__primary } **Infrastructure SAST**
    ---
    **KICS Security Audit**
    {% set kics_total = kics_report.get('total_counter', 0) %}
    {% if kics_total == 0 -%}
    [:material-check-circle:{ .md-typeset__success } **Pristine State**](./static-analysis/kics-report.md)
    {% else -%}
    [:material-alert-decagram:{ .md-typeset__error } **{{ kics_total }} Security Risks**](./static-analysis/kics-report.md)
    {% endif -%}
    *Static Analysis of IaC & Dockerfile*

-   :material-shield-check:{ .md-typeset__primary } **Cryptographic Boundary**
    ---
    **FIPS Logic Integrity**
    {% set std_failed = standard_report_FIPS_validation.get('summary', {}).get('failed', 'N/A') %}
    {% if std_failed == 0 -%}
    [:material-shield-lock:{ .md-typeset__success } **Boundary Validated**](./functional-tests/standard-image.md)
    {% else -%}
    [:material-shield-off:{ .md-typeset__error } **{{ std_failed }} Logic Violations**](./functional-tests/standard-image.md)
    {% endif -%}
    *Provider State Machine Verification*

-   :material-package-variant-closed:{ .md-typeset__primary } **Runtime Hardening**
    ---
    **Attack Surface Audit**
    {% set dist_failed = distroless_report_FIPS_validation.get('summary', {}).get('failed', 'N/A') %}
    {% if dist_failed == 0 -%}
    [:material-robot-confused-outline:{ .md-typeset__success } **Zero-Entry Hardened**](./functional-tests/distroless-image.md)
    {% else -%}
    [:material-robot-dead-outline:{ .md-typeset__error } **{{ dist_failed }} Policy Failures**](./functional-tests/distroless-image.md)
    {% endif -%}
    *Distroless Compliance & Binary Parity*

-   :material-gavel:{ .md-typeset__primary } **Enterprise Adherence**
    ---
    **Supply Chain Metrics**
    {% set std_results = standard_compliance.get('security_scan', {}).get('Results', [{}]) %}
    {% set std_vulns = std_results[0].get('Vulnerabilities', []) | length %}
    {% if std_vulns == 0 -%}
    [:material-certificate:{ .md-typeset__success } **Standard Compliant**](./compliance/standard/vulnerability.md)
    {% else -%}
    [:material-alert-rhombus:{ .md-typeset__error } **{{ std_vulns }} CVEs Pending**](./compliance/standard/vulnerability.md)
    {% endif -%}
    *Trivy / CIS / NSA / PSS Benchmarks*

</div>

---

## :material-layers-triple-outline: Architectural Integrity Notice

!!! tip "Development vs Standard Parity"
    The **Development SDK** variant contains an extended suite of packages (compilers, debuggers, and headers) compared to the **Standard** variant. However, it is vital to note that the **cryptographic core and FIPS boundary remain identical** across both profiles. The functional behavior of the OpenSSL provider is mirrored to ensure that applications developed in the SDK environment behave with absolute parity when moved to the Standard production runtime.

!!! info "Cryptographic Provenance & SBOM Transparency"
    To ensure absolute compliance with **FIPS 140-3** standards, the OpenSSL core and FIPS provider are compiled directly from validated sources. This bypasses upstream package manager vulnerabilities. Consequently, OpenSSL will be listed in the **CycloneDX SBOM** as a compiled integral rather than an ephemeral OS package.

---

## :material-file-tree: Deep-Dive Audit Repository

### :material-text-box-search-outline: 1. Functional Integrity Reports
Detailed audit logs for cryptographic state-machine and provider validation.

| Audit Target | Environment | Status |
| :--- | :--- | :--- |
| **Standard Image** | [Full Technical Report](./functional-tests/standard-image.md) | :material-file-find-outline: |
| **Distroless Runtime** | [Full Technical Report](./functional-tests/distroless-image.md) | :material-file-find-outline: |

---
[:material-arrow-up-circle: Back to top](#security-validation-dashboard)


### :material-shield-crown-outline: 2. Compliance & Hardening Matrix
*Multi-benchmark verification hub across production-ready and development-integrated variants.*

=== ":material-monitor-dashboard: Production Standard"

    !!! example "Standard Profile"
        The **Standard Variant** is engineered for general-purpose high-security workloads. It provides a balanced attack surface while maintaining essential system utilities.

    <div class="grid cards" markdown>

    -   [:material-shield-sync: **Vulnerability Scan**](./compliance/standard/vulnerability.md)
        ---
        *Trivy-backed SBOM & CVE analysis.*

    -   [:material-docker: **CIS Docker Benchmark**](./compliance/standard/docker-cis.md)
        ---
        *Host and container configuration audit.*

    -   [:material-kubernetes: **NSA Hardening**](./compliance/standard/k8s-nsa.md)
        ---
        *NSA/CISA Kubernetes infrastructure mapping.*

    -   [:material-gavel: **PSS Restricted**](./compliance/standard/k8s-pss.md)
        ---
        *Pod Security Standards validation.*

    </div>

=== ":material-shield-star: Hardened Distroless"

    !!! success "Distroless Profile"
        The **Distroless Variant** represents the absolute "Zero-Entry" hardening tier. With no shell or package manager, it natively satisfies the most stringent compliance requirements.

    <div class="grid cards" markdown>

    -   [:material-shield-sync: **Vulnerability Scan**](./compliance/distroless/vulnerability.md)
        ---
        *Minimalist binary footprint audit.*

    -   [:material-docker: **CIS Docker Benchmark**](./compliance/distroless/docker-cis.md)
        ---
        *Optimized for immutable deployments.*

    -   [:material-kubernetes: **NSA Hardening**](./compliance/distroless/k8s-nsa.md)
        ---
        *Advanced cluster-level isolation checks.*

    -   [:material-gavel: **PSS Restricted**](./compliance/distroless/k8s-pss.md)
        ---
        *Strict admission controller compatibility.*

    </div>

=== ":material-hammer-wrench: Development SDK"

    !!! warning "SDK & Build Parity"
        The **Development Variant** includes comprehensive build tooling (GCC, Perl, PCRE) necessary for FIPS-linked compilation. While the package count is higher than the Standard variant, the **OpenSSL FIPS logic remains identical** to production.

    <div class="grid cards" markdown>

    -   [:material-shield-sync: **Vulnerability Scan**](./compliance/development/vulnerability.md)
        ---
        *Supply-chain audit of dev toolchains.*

    -   [:material-docker: **CIS Docker Benchmark**](./compliance/development/docker-cis.md)
        ---
        *Build-time security posture assessment.*

    -   [:material-kubernetes: **NSA Hardening**](./compliance/development/k8s-nsa.md)
        ---
        *Dev-environment infrastructure guidance.*

    -   [:material-gavel: **PSS Restricted**](./compliance/development/k8s-pss.md)
        ---
        *Validation of high-privilege dev containers.*

    </div>

---
[:material-arrow-up-circle: Back to top](#security-validation-dashboard)