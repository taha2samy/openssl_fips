{% set nsa_data = development_compliance['k8s_nsa'] %}
{% set all_controls = nsa_data['SummaryControls'] %}

{# --- Logic: Separate Controls using Namespace (Safe for MkDocs) --- #}
{% set ns = namespace(manual=[], auto=[]) %}
{% for ctrl in all_controls %}
  {% if "(Manual)" in ctrl['Name'] or "manual" in ctrl['Name']|lower %}
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
  {% set compliance_percent = (passed_auto / total_auto * 100) | round(0) | int %}
{% else %}
  {% set compliance_percent = 0 %}
{% endif %}

# :fontawesome-solid-building-shield: NSA Kubernetes Hardening (Development)

**Scope:** `Development SDK` &nbsp;|&nbsp; **Guidance Ver:** `1.0` &nbsp;|&nbsp; **Profile:** `Build-Time Security`

!!! abstract "Shared Responsibility Disclaimer"
    The NSA/CISA hardening guidance for the **Development Variant** focuses on ensuring that the build-time environment doesn't introduce supply chain risks. 
    *   **Image Scope:** We enforce non-root users and immutable layers where possible.
    *   **Cluster Scope:** Infrastructure controls (like NetworkPolicies) must be applied by the **Cluster Admin** during the CI/CD pipeline execution.
    *   **Reference:** [Shared Responsibility Model](https://cloud.google.com/architecture/framework/security/shared-responsibility-model)

---

## :material-finance: Build-Time Risk Profile

<div class="grid cards" markdown>

-   :material-bullseye-arrow: **Image Adherence**
    ---
    {% if compliance_percent == 100 -%}
    <span style="color: #00c853; font-size: 2.2em; font-weight: 900;">{{ compliance_percent }}%</span>
    {% elif compliance_percent >= 85 -%}
    <span style="color: #ffab00; font-size: 2.2em; font-weight: 900;">{{ compliance_percent }}%</span>
    {% else -%}
    <span style="color: #d50000; font-size: 2.2em; font-weight: 900;">{{ compliance_percent }}%</span>
    {% endif -%}
    
    *Verified SDK Configuration*

-   :material-clipboard-text-clock: **Infrastructure Dependency**
    ---
    <span style="color: #2979ff; font-size: 2.2em; font-weight: 900;">{{ ns.manual | length }}</span>
    
    *Cluster-Level Controls Required*

-   :material-alert-rhombus: **Actionable Violations**
    ---
    {% if failed_auto == 0 -%}
    <span style="color: #00c853; font-size: 2.2em; font-weight: 900;">Zero</span>
    {% else -%}
    <span style="color: #d50000; font-size: 2.2em; font-weight: 900;">{{ failed_auto }}</span>
    {% endif -%}
    
    *Direct Container Risks*

</div>

---

## :material-view-list: Control Matrix

### 1. Automated Checks (Container Image Scope)

| ID | Hardening Control | Severity | Audit Status |
| :---: | :--- | :---: | :---: |
{% for control in ns.auto -%}
{% if control['TotalFail'] == 0 -%}
| **{{ control['ID'] }}** | {{ control['Name'] }} | <span style="color: #4caf50; font-weight: bold;">{{ control['Severity'] }}</span> | :material-check-decagram:{ .md-typeset__success title="Compliant" } |
{% else -%}
| **{{ control['ID'] }}** | {{ control['Name'] }} | <span style="color: #f44336; font-weight: bold;">{{ control['Severity'] }}</span> | :material-close-octagon:{ .md-typeset__error title="Violation" } |
{% endif -%}
{% endfor %}

### 2. Manual / Cluster Scope (Out-of-Scope)

| ID | Hardening Control | Severity | Responsibility |
| :---: | :--- | :---: | :---: |
{% for control in ns.manual -%}
| **{{ control['ID'] }}** | {{ control['Name'] }} | <span style="color: #616161;">{{ contr