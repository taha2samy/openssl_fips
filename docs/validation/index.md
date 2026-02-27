# :material-shield-check: Automated Validation Overview


This section documents the continuous security and functional verification process. Our validation strategy ensures that the cryptographic boundary remains intact across all distributed variants.

---

## :material-chart-areaspline: Real-Time Validation Status

<div class="grid cards" markdown>

-   :material-magnify-scan: **Static Analysis (SAST)**
    ---
    **KICS Security Scan**
    {% if kics_report.total_counter == 0 %}
    [:material-check-circle:{ .md-typeset__success } **Clean**](../validation/static-analysis/kics-report.md)
    {% else %}
    [:material-alert-circle:{ .md-typeset__error } **{{ kics_report.total_counter }} Issues Found**](../validation/static-analysis/kics-report.md)
    {% endif %}
    *Dockerfile, HCL, & CI/CD Security*

-   :material-test-tube: **Standard & Development**
    ---
    **Shared Cryptographic Core**
    {% if standard_report_FIPS_validation.summary.failed == 0 %}
    [:material-check-circle:{ .md-typeset__success } **Passed**](../validation/functional-tests/standard-image.md)
    {% else %}
    [:material-close-circle:{ .md-typeset__error } **{{ standard_report_FIPS_validation.summary.failed }} Failed**](../validation/functional-tests/standard-image.md)
    {% endif %}
    *Validated FIPS Provider & SDK Integrity*

-   :material-package-variant-closed: **Distroless Image**
    ---
    **Production-Hardened**
    {% if distroless_report_FIPS_validation.summary.failed == 0 %}
    [:material-check-circle:{ .md-typeset__success } **Passed**](../validation/functional-tests/distroless-image.md)
    {% else %}
    [:material-close-circle:{ .md-typeset__error } **{{ distroless_report_FIPS_validation.summary.failed }} Failed**](../validation/functional-tests/distroless-image.md)
    {% endif %}
    *Attack surface reduction validation*

</div>

---

## :material-layers-outline: Validation Methodology

### 1. Static Infrastructure Analysis
We use **KICS** to analyze our multi-stage Dockerfile and HCL configurations. This ensures that every layer—from the initial FIPS builder to the final runtime stages—follows strict security headers and best practices.

### 2. Functional & Compliance Strategy
Our testing is designed around the **Shared Core** architecture:

*   **Standard Image Validation:** This serves as the primary verification for both `Standard` and `Development` variants. Since the `openssl-dev` stage inherits the exact same FIPS binaries and configuration from the `fips-integrator` as the `Standard` image, the cryptographic integrity of the Development SDK is guaranteed by the Standard Image test suite.
*   **Distroless Validation:** A secondary, more stringent check. It verifies that stripping the OS down to the bare minimum does not interfere with OpenSSL's ability to locate its modules or perform its Power-Up Self-Tests (POST).

---

## :material-file-tree: Detailed Reports

- :material-file-search: [Detailed Static Analysis (KICS)](../validation/static-analysis/kics-report.md)
- :material-file-document: [Standard & Dev Core Functional Report](../validation/functional-tests/standard-image.md)
- :material-file-document: [Distroless Image Functional Report](../validation/functional-tests/distroless-image.md)