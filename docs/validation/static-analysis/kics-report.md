# :material-shield-search: KICS Static Analysis Report

This report provides an automated security and misconfiguration analysis for the project's Infrastructure as Code (IaC) files, including **Dockerfile** and **GitHub Actions workflows**.

---

## :material-chart-box-outline: Scan Summary

<div class="grid cards" markdown>

-   :material-file-document-multiple-outline: **Files Scanned**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ kics_report.files_scanned }}
    </span>
    *Total files processed by the scanner*

-   :material-code-tags-check: **Lines Scanned**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ kics_report.lines_scanned }}
    </span>
    *Total lines of code analyzed*

-   :material-timer-sand: **Scan Duration**
    ---
    {% set start_time = kics_report.start | to_datetime %}
    {% set end_time = kics_report.end | to_datetime %}
    {% set duration = (end_time - start_time).total_seconds() %}
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ duration | round(1) }}s
    </span>
    *End-to-end analysis time*

</div>

---

## :material-security: Vulnerability Overview

{% if kics_report.total_counter == 0 %}
!!! success "All Clear: No Vulnerabilities Found"
    **Congratulations!** The KICS scan completed successfully and found **zero** security vulnerabilities or misconfigurations in the scanned files. The infrastructure code adheres to the defined security best practices.

    - **KICS Version:** `{{ kics_report.kics_version }}`
    - **Total Queries Executed:** `{{ kics_report.queries_total }}`

{% else %}
!!! failure "Action Required: {{ kics_report.total_counter }} Vulnerabilities Found"
    The scan identified one or more security issues that require attention. Please review the detailed findings below.

    <div class="grid cards" markdown>
    - **Critical: {{ kics_report.severity_counters.CRITICAL or 0 }}**
    - **High: {{ kics_report.severity_counters.HIGH or 0 }}**
    - **Medium: {{ kics_report.severity_counters.MEDIUM or 0 }}**
    - **Low: {{ kics_report.severity_counters.LOW or 0 }}**
    </div>
{% endif %}

---

## :material-magnify-scan: Detailed Findings

{% if kics_report.queries %}
{% for query in kics_report.queries %}
  {% set severity = query.severity | lower %}
  {% set status_type = "failure" if severity in ['high', 'critical'] else "warning" if severity == 'medium' else "info" %}

??? {{ status_type }} "**{{ query.severity }}:** {{ query.query_name | replace('_', ' ') | title }}"
    
    **Description:**  
    {{ query.description }}

    ---

    **File:** `{{ query.files[0].file_name }}` (Line: `{{ query.files[0].line }}`)

    **Category:** `{{ query.category }}`

    [:octicons-link-external-16: Learn More]({{ query.query_url }})

{% endfor %}
{% else %}
*No detailed findings to display.*
{% endif %}