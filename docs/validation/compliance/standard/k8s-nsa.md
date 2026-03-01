{% set nsa_data = standard_compliance.k8s_nsa %}
{% set all_controls = nsa_data.SummaryControls %}

{# --- Logic: Separate Controls (Container vs Cluster) --- #}
{% set ns = namespace(manual=[], auto=[]) %}

{% for ctrl in all_controls %}
  {% if "(Manual)" in ctrl.Name or "manual" in ctrl.Name|lower %}
    {% set ns.manual = ns.manual + [ctrl] %}
  {% else %}
    {% set ns.auto = ns.auto + [ctrl] %}
  {% endif %}
{% endfor %}

{% set total_auto = ns.auto | length %}
{% set passed_auto = ns.auto | selectattr("TotalFail", "equalto", 0) | list | length %}
{% set failed_auto = total_auto - passed_auto %}

{% if total_auto > 0 %}
  {% set compliance_percent = (passed_auto / total_auto * 100) | round(0) | int %}
{% else %}
  {% set compliance_percent = 0 %}
{% endif %}

# :fontawesome-solid-building-shield: NSA Kubernetes Hardening

**Scope:** `Standard Image` &nbsp;|&nbsp; **Guidance Ver:** `1.0` &nbsp;|&nbsp; **Profile:** `Pod Security & Network Hardening`

!!! abstract "Scope of Responsibility (Shared Responsibility Model)"
    The NSA/CISA Kubernetes Hardening Guidance covers the entire infrastructure lifecycle. 
    *   **In-Scope (Container Level):** Image configurations like non-root execution, dropped capabilities, and filesystem immutability are handled directly by this OpenSSL FIPS image.
    *   **Out-of-Scope (Cluster Level):** Controls related to `etcd` encryption, NetworkPolicies, and API server configurations are **Runtime/Infrastructure responsibilities**. They appear in this report for completeness but must be enforced via your Kubernetes manifests (e.g., `Deployment` / `PodSecurityContext`) and Cluster configuration.

---

## :material-finance: Risk Mitigation Profile

<div class="grid cards" markdown>

-   :material-bullseye-arrow: **Image Adherence**
    ---
    {% if compliance_percent == 100 %}
    <span style="color: #00c853; font-size: 2.2em; font-weight: 900;">{{ compliance_percent }}%</span>
    {% elif compliance_percent >= 85 %}
    <span style="color: #ffab00; font-size: 2.2em; font-weight: 900;">{{ compliance_percent }}%</span>
    {% else %}
    <span style="color: #d50000; font-size: 2.2em; font-weight: 900;">{{ compliance_percent }}%</span>
    {% endif %}
    
    *Container-Level Controls*

-   :material-shield-lock: **Passed Controls**
    ---
    <span style="font-size: 2.2em; font-weight: 900;">{{ passed_auto }}</span>
    <span style="color: #bdbdbd; font-size: 0.8em;"> / {{ total_auto }}</span>
    
    *Static Configurations Verified*

-   :material-transit-connection-variant: **Runtime Dependency**
    ---
    <span style="color: #2979ff; font-size: 2.2em; font-weight: 900;">{{ ns.manual | length }}</span>
    
    *Cluster & Deployment Dependent*

</div>

{% if failed_auto > 0 %}
!!! danger "Non-Compliant Hardening Factors"
    This image violates specific NSA hardening guidelines at the container level.
{% endif %}

---

## :material-view-list: Control Matrix

### 1. Automated Checks (Container Image Scope)
These controls are statically verified against the Docker image layers.

| ID | Hardening Control | Severity | Audit Status |
| :---: | :--- | :---: | :---: |
{% for control in ns.auto -%}
{% if control.TotalFail == 0 -%}
| **{{ control.ID }}** | {{ control.Name }} | <span style="color: #4caf50; font-weight: bold;">{{ control.Severity }}</span> | :material-check-decagram:{ .md-typeset__success title="Compliant" } |
{% else -%}
| **{{ control.ID }}** | {{ control.Name }} | <span style="color: #f44336; font-weight: bold;">{{ control.Severity }}</span> | :material-close-octagon:{ .md-typeset__error title="Violation" } |
{% endif -%}
{% endfor %}

### 2. Manual / Infrastructure Checks (Cluster Scope) (1)
These controls cannot be satisfied by the container image alone. They require proper `securityContext` settings in your Kubernetes YAML and secure cluster administration.

| ID | Hardening Control | Severity | Responsibility |
| :---: | :--- | :---: | :---: |
{% for control in ns.manual -%}
| **{{ control.ID }}** | {{ control.Name }} | <span style="color: #616161; font-weight: bold;">{{ control.Severity }}</span> | :material-kubernetes:{ style="color: #326ce5" title="Cluster Admin" } |
{% endfor %}

---

## :fontawesome-solid-layer-group: Policy Categories

The controls above map to the following NSA threat models:

1.  **Non-Root Execution:** Ensures containers do not run with UID 0 (Configured via Dockerfile `USER`).
2.  **Immutable Filesystems:** Prevents runtime modification of binaries (Must be enforced via `readOnlyRootFilesystem: true` in K8s).
3.  **Network Isolation:** Ensures CNI plugins support NetworkPolicies (Cluster Architecture).

*(1) Refer to the [Shared Responsibility Model](https://cloud.google.com/architecture/framework/security/shared-responsibility-model) for Cloud Native workloads.*