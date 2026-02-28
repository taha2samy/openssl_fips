# :material-shield-search: KICS Static Analysis Report

This report provides an automated security analysis for the project's Infrastructure as Code (IaC).

---

## :material-chart-box-outline: Scan Summary

<div class="grid cards" markdown>

-   :material-file-document-multiple-outline: **Files Scanned**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ kics_report.files_scanned }}
    </span>

-   :material-code-tags-check: **Lines Scanned**
    ---
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ kics_report.lines_scanned }}
    </span>

-   :material-timer-sand: **Scan Duration**
    ---
    {% set start_time = kics_report.start | to_datetime %}
    {% set end_time = kics_report.end | to_datetime %}
    {% set duration = (end_time - start_time).total_seconds() %}
    <span style="font-size: 2.2em; font-weight: 900; color: var(--md-default-fg-color--light);">
      {{ duration | round(1) }}s
    </span>

</div>

---

## :material-security: Vulnerability Overview

{% if kics_report.total_counter == 0 %}
!!! success "All Clear: No Vulnerabilities Found"
    The infrastructure code adheres to the defined security best practices.
{% else %}
!!! failure "Action Required: {{ kics_report.total_counter }} Issues Found"
    The scan identified security misconfigurations. Please review the breakdown:

<div class="grid cards" markdown>

- :material-alert-decagram:{ .md-typeset__error } **Critical/High**
    ---
    <span style="font-size: 1.5em; font-weight: 700;">
    {{ (kics_report.severity_counters.CRITICAL or 0) + (kics_report.severity_counters.HIGH or 0) }}
    </span>

- :material-alert-circle:{ .md-typeset__warning } **Medium**
    ---
    <span style="font-size: 1.5em; font-weight: 700;">
    {{ kics_report.severity_counters.MEDIUM or 0 }}
    </span>

- :material-information-outline:{ .md-typeset__info } **Low**
    ---
    <span style="font-size: 1.5em; font-weight: 700;">
    {{ kics_report.severity_counters.LOW or 0 }}
    </span>

- :material-note-text-outline: **Info**
    ---
    <span style="font-size: 1.5em; font-weight: 700;">
    {{ kics_report.severity_counters.INFO or 0 }}
    </span>

</div>
{% endif %}

---

## :material-magnify-scan: Detailed Findings

{% if kics_report.queries %}
{% for query in kics_report.queries %}
  {% set severity = query.severity | lower %}
  {% if severity in ['high', 'critical'] %}{% set status_type = "failure" %}
  {% elif severity == 'medium' %}{% set status_type = "warning" %}
  {% else %}{% set status_type = "info" %}{% endif %}

??? {{ status_type }} "**{{ query.severity }}:** {{ query.query_name | replace('_', ' ') | title }}"
    
    **Description:**  
    {{ query.description }}

    ---
    **Evidence:**
    | File | Line | Category |
    | :--- | :--- | :--- |
    | `{{ query.files[0].file_name }}` | `{{ query.files[0].line }}` | `{{ query.category }}` |

    [:octicons-link-external-16: Learn More]({{ query.query_url }})

{% endfor %}
{% else %}
*No detailed findings to display.*
{% endif %}