{% set pss_data = development_compliance['k8s_pss_restricted'] %}
{% set total_rules = pss_data['SummaryControls'] | length %}
{% set passed_rules = pss_data['SummaryControls'] | selectattr("TotalFail", "defined") | selectattr("TotalFail", "equalto", 0) | list | length %}
{% set failed_rules = total_rules - passed_rules %}
{% set compliance_color = "#00c853" if failed_rules == 0 else "#d50000" %}

# :fontawesome-brands-linux: Kubernetes PSS (Restricted Profile) - Development

**Enforcement Level:** `Restricted` &nbsp;|&nbsp; **Scope:** `Build Environment Isolation` &nbsp;|&nbsp; **K8s Ver:** `v1.24+`

!!! abstract "Shared Responsibility: Developer & Operator"
    This report confirms that the **Development SDK Image** is architected to run within a `Restricted` Kubernetes Namespace. 
    While the image is natively non-root and lacks privileged binaries, the final compliance is a shared effort. 
    **[:material-link-variant: Learn more about the Shared Responsibility Model](https://cloud.google.com/architecture/framework/security/shared-responsibility-model)**

---

## :material-gavel: Admission Controller Readiness

<div class="grid cards" markdown>

-   :material-police-badge: **Policy Status**
    ---
    {% if failed_rules == 0 -%}
    <span style="color: {{ compliance_color }}; font-size: 2.2em; font-weight: 900;">READY</span>
    <br><span style="font-size: 0.8em;">*SDK is Restricted-Capable*</span>
    {% else -%}
    <span style="color: {{ compliance_color }}; font-size: 2.2em; font-weight: 900;">BLOCKED</span>
    <br><span style="font-size: 0.8em;">*Static Validation Failed*</span>
    {% endif -%}

-   :material-lock-check: **Rules Satisfied**
    ---
    <span style="font-size: 2.2em; font-weight: 900;">{{ passed_rules }}</span>
    <span style="color: #9e9e9e;"> / {{ total_rules }}</span>
    
    *Baseline + Restricted Policies*

-   :material-skull-crossbones: **Blocking Violations**
    ---
    {% if failed_rules == 0 -%}
    <span style="color: #00c853; font-size: 2.2em; font-weight: 900;">0</span>
    {% else -%}
    <span style="color: #d50000; font-size: 2.2em; font-weight: 900;">{{ failed_rules }}</span>
    {% endif -%}
    
    *Must Resolve in Dockerfile*

</div>

{% if failed_rules > 0 %}
!!! critical "Compliance Gap Detected"
    The Development image contains configurations that will trigger a rejection from the Kubernetes Admission Controller in restricted environments.
{% else %}
!!! success "Secure Pipeline Ready"
    The Development SDK satisfies all **Static PSS Checks**. It is safe to use as a CI/CD build agent in hardened, multi-tenant Kubernetes clusters.
{% endif %}

---

## :material-clipboard-list-outline: Policy Enforcement Matrix

| ID | Restriction Rule | Impact Level | Static Audit |
| :---: | :--- | :---: | :---: |
{% for rule in pss_data['SummaryControls'] -%}
{% if rule['TotalFail'] == 0 -%}
| `{{ rule['ID'] }}` | **{{ rule['Name'] }}** | <span style="color: #616161;">{{ rule['Severity'] }}</span> | :material-check-all:{ .md-typeset__success title="Satisfied" } |
{% else -%}
| `{{ rule['ID'] }}` | **{{ rule['Name'] }}** | <span style="color: #d50000; font-weight: bold;">{{ rule['Severity'] }}</span> | :material-cancel:{ .md-typeset__error title="Violated" } |
{% endif -%}
{% endfor %}

---

## :material-lightbulb-outline: Why This Matters for Development?

Running build tools (Compilers, Linkers) in a **Restricted PSS** environment ensures that the development phase doesn't become the "weakest link":

1.  **Isolation:** Even if a compiler is compromised, it cannot access the host network or sensitive kernel namespaces.
2.  **Least Privilege:** Ensuring build agents run as `openssl` (non-root) prevents "Escape-to-Host" attacks from within the CI pipeline.
3.  **Governance:** Matches the security posture of the production `Distroless` image, creating a consistent security baseline across the SDLC.

---
[:material-arrow-up: Back to Top](#kubernetes-pss-restricted-profile-development)