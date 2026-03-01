{% set nsa_data = distroless_compliance['k8s_nsa'] %}
{% set all_controls = nsa_data['SummaryControls'] %}

{# --- Logic: Separate Controls (Container vs Cluster) --- #}
{% set ns = namespace(manual=[], auto=[]) %}

{% for ctrl in all_controls %}
  {% if "(Manual)" in ctrl['Name'] or "manual" in ctrl['Name']|lower %}
    {% set ns.manual = ns.manual + [ctrl] %}
  {% else %}
    {% set ns.auto = ns.auto + [ctrl] %}
  {% endif %}
{% endfor %}

{% set total_auto = ns.auto | length %}
{% set passed_auto = ns.auto | selectattr("TotalFail", "defined") | selectattr("TotalFail", "equalto", 0) | list | length %}
{% set failed_auto = total_auto - passed_auto %}

{% if total_auto > 0 %}
  {% set compliance_percent = (passed_auto / total_auto * 100) | round(0) | int %}
{% else %}
  {% set compliance_percent = 0 %}
{% endif %}

# :fontawesome-solid-building-shield: NSA Kubernetes Hardening (Distroless)

**Scope:** `Distroless Image` &nbsp;|&nbsp; **Guidance Ver:** `1.0` &nbsp;|&nbsp; **Profile:** `Hardened Workload`

!!! abstract "Shared Responsibility: Infrastructure Scoping"
    The NSA/CISA Kubernetes guidance requires hardening at both the container and cluster levels. 
    *   **In-Scope (Container):** The Distroless image satisfies all static requirements by eliminating the shell, reducing binaries, and enforcing non-root execution.
    *   **Out-of-Scope (Cluster):** Network isolation policies and API server configurations must be verified by the **Cluster Admin**.
    *   **Reference:** [Shared Responsibility Model](https://cloud.google.com/architecture/framework/security/shared-responsibility-model)

---

## :material-finance: Production Risk Profile

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
    
    *Automated Container Audit*

-   :material-clipboard-text-clock: **Runtime Dependency**
    ---
    <span style="color: #2979ff; font-size: 2.2em; font-weight: 900;">{{ ns.manual | length }}</span>
    
    *Cluster-Level Verifications*

-   :material-alert-rhombus: **Actionable Violations**
    ---
    {% if failed_auto == 0 -%}
    <span style="color: #00c853; font-size: 2.2em; font-weight: 900;">Zero</span>
    {% else -%}
    <span style="color: #d50000; font-size: 2.2em; font-weight: 900;">{{ failed_auto }}</span>
    {% endif -%}
    
    *Immediate Remediation*

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
| **{{ control['ID'] }}** | {{ control['Name'] }} | <span style="color: #616161;">{{ control['Severity'] }}</span> | :material-kubernetes:{ style="color: #326ce5" title="Cluster Admin" } |
{% endfor %}

---

## :fontawesome-solid-layer-group: Key Hardening Principles (Distroless)

By utilizing a Distroless base image, we natively address several NSA hardening requirements:

1.  **Attack Surface Reduction:** By removing shells (`/bin/sh`, `/bin/bash`) and package managers (`apk`), the lateral movement capability of an attacker is significantly restricted.
2.  **Binary Integrity:** Only the minimal required OpenSSL FIPS binaries are present, reducing the risk of unauthorized binary execution.
3.  **Read-Only Compatibility:** The image is optimized for `readOnlyRootFilesystem: true`, a core NSA recommendation for immutable workloads.

---
[:material-arrow-up: Back to Top](#nsa-kubernetes-hardening-distroless)