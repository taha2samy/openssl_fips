# :material-shield-check: Standard Image Validation Report

This high-assurance report documents the automated verification process for the **Wolfi OpenSSL FIPS (Standard)** image.

---

## :material-chart-box-outline: Execution Summary

<div class="grid cards" markdown>

-   :material-check-decagram:{ .md-typeset__success } **Passed Verifications**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-code-hl-string-color);">
      {{ standard_report_FIPS_validation.summary.passed }}
    </span>
    *All cryptographic boundaries intact*

-   :material-alert-decagram:{ .md-typeset__error } **Compliance Failures**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-code-hl-keyword-color);">
      {{ standard_report_FIPS_validation.summary.failed }}
    </span>
    *Immediate remediation required*

-   :material-clock-fast: **Total Latency**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ standard_report_FIPS_validation.duration | round(1) }}s
    </span>
    *End-to-end execution time*

</div>

---
## :material-clipboard-list: Test Details
{% for test in standard_report_FIPS_validation.tests %}
  {% set is_passed = test.outcome == "passed" %}
  {% set status_type = "success" if is_passed else "failure" %}
  {% set display_name = test.nodeid.split('::')[-1] | replace('test_', '') | replace('_', ' ') | title %}

??? {{ status_type }} "{{ display_name }} ({{ test.call.duration | round(2) if (test.call and test.call.duration) else '0' }}s)"

    **File Path:** `{{ test.nodeid.split('::')[0] }}`

    {% if not is_passed and test.call and test.call.crash %}
    ---
    **Failure Message:**
    ```python
    {{ test.call.crash.message | indent(4) }}
    ```
    {% endif %}

    {% if test.call and test.call.log %}
    ---
    ??? info "View Logs"

        ```bash
        {% for log in test.call.log -%}
        [{{ log.levelname }}] {{ log.msg }}
        {% endfor %}
        ```
    {% endif %}

{% endfor %}