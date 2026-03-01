{% set cis_data = standard_compliance.docker_cis %}
{% set all_controls = cis_data.SummaryControls %}

{# --- Logic: Separate Controls using Native List Concatenation (No 'do') --- #}
{% set ns = namespace(manual=[], auto=[]) %}

{% for ctrl in all_controls %}
  {% if "(Manual)" in ctrl.Name %}
    {% set ns.manual = ns.manual + [ctrl] %}
  {% else %}
    {% set ns.auto = ns.auto + [ctrl] %}
  {% endif %}
{% endfor %}

{# --- Stats Calculation on AUTOMATED Only --- #}
{% set total_auto = ns.auto | length %}
{% set passed_auto = ns.auto | selectattr("TotalFail", "defined") | selectattr("TotalFail", "equalto", 0) | list | length %}
{% set failed_auto = total_auto - passed_auto %}

{% if total_auto > 0 %}
  {% set success_rate = (passed_auto / total_auto * 100) | round(0) | int %}
{% else %}
  {% set success_rate = 0 %}
{% endif %}

# :fontawesome-brands-docker: CIS Docker Benchmark Report

**Target:** `Standard Image` &nbsp;|&nbsp; **Profile:** Level 1 - Container &nbsp;|&nbsp; **Benchmark Ver:** `{{ cis_data.ID }}`

---

## :material-chart-box-outline: Compliance Scorecard

<div class="grid cards" markdown>

-   :material-shield-check: **Automated Score**
    ---
    {% if success_rate == 100 %}
    <span style="color: #00e676; font-size: 2em; font-weight: bold;">{{ success_rate }}%</span> :material-check-decagram:{ .md-typeset__success }
    {% elif success_rate >= 80 %}
    <span style="color: #ff9100; font-size: 2em; font-weight: bold;">{{ success_rate }}%</span> :material-alert-decagram:{ .md-typeset__warning }
    {% else %}
    <span style="color: #ff1744; font-size: 2em; font-weight: bold;">{{ success_rate }}%</span> :material-close-octagon:{ .md-typeset__error }
    {% endif %}
    
    *Based on {{ total_auto }} Automated Checks*

-   :material-clipboard-text-clock: **Manual Review**
    ---
    <span style="color: #2979ff; font-size: 2em; font-weight: bold;">{{ ns.manual | length }}</span>
    
    *Items Require Operational Audit*

-   :material-alert-circle-outline: **Blocking Failures**
    ---
    {% if failed_auto == 0 %}
    <span style="color: #00e676; font-size: 2em; font-weight: bold;">0</span>
    {% else %}
    <span style="color: #ff1744; font-size: 2em; font-weight: bold;">{{ failed_auto }}</span>
    {% endif %}
    
    *Critical Config Errors*

</div>

{% if failed_auto > 0 %}
!!! failure "Critical Compliance Gaps"
    Some automated controls failed. These must be fixed in the `Dockerfile`.
{% elif ns.manual | length > 0 %}
!!! info "Operational Verification Required"
    The image passed all automated checks. Ensure the **Host Environment** satisfies the `Manual` controls listed below to achieve full certification.
{% endif %}

---

## :material-table-search: Detailed Audit Log

### 1. Automated Controls

| Status | ID | Control Description | Severity |
| :---: | :---: | :--- | :---: |
{%- for control in ns.auto %}
{%- if control.TotalFail == 0 %}
| :material-check-circle:{ .md-typeset__success title="Passed" } | **{{ control.ID }}** | {{ control.Name }} | <span style="color: green; font-weight: bold;">{{ control.Severity }}</span> |
{%- else %}
| :material-close-circle:{ .md-typeset__error title="Failed" } | **{{ control.ID }}** | {{ control.Name }} | <span style="color: red; font-weight: bold;">{{ control.Severity }}</span> |
{%- endif %}
{%- endfor %}

### 2. Manual / Host-Level Controls

| Status | ID | Control Description | Severity |
| :---: | :---: | :--- | :---: |
{%- for control in ns.manual %}
{%- if control.TotalFail == 0 %}
| :material-check-circle:{ .md-typeset__success title="Passed" } | **{{ control.ID }}** | {{ control.Name }} | <span style="color: green; font-weight: bold;">{{ control.Severity }}</span> |
{%- else %}
| :material-close-circle:{ .md-typeset__error title="Failed" } | **{{ control.ID }}** | {{ control.Name }} | <span style="color: red; font-weight: bold;">{{ control.Severity }}</span> |
{%- endif %}
{%- endfor %}

---

### :material-book-open-page-variant: Audit Legend

*   :material-check-circle:{ .md-typeset__success } **Passed:** Configuration is hardcoded correctly in the image.
*   :material-close-circle:{ .md-typeset__error } **Failed:** Violation detected (e.g., Image runs as Root).
*   :material-clipboard-alert:{ style="color: #2979ff" } **Manual:** Cannot be checked inside the build pipeline (Host-dependent or Runtime-dependent).