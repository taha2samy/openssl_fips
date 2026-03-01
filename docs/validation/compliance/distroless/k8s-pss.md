{% set pss_data = distroless_compliance['k8s_pss_restricted'] %}
{% set total_rules = pss_data['SummaryControls'] | length %}
{% set passed_rules = pss_data['SummaryControls'] | selectattr("TotalFail", "defined") | selectattr("TotalFail", "equalto", 0) | list | length %}
{% set failed_rules = total_rules - passed_rules %}
{% set compliance_color = "#00c853" if failed_rules == 0 else "#d50000" %}

# :fontawesome-brands-linux: Kubernetes PSS (Restricted Profile) - Distroless

**Enforcement Level:** `Restricted` &nbsp;|&nbsp; **Scope:** `Production Hardening` &nbsp;|&nbsp; **K8s Ver:** `v1.24+`

!!! abstract "The Distroless Advantage"
    The **Distroless variant** is engineered for the highest level of Kubernetes security. By removing the shell and all unnecessary OS utilities, it natively satisfies many PSS "Restricted" requirements that typical images struggle with.
    **[:material-link-variant: Review the Shared Responsibility Model](https://cloud.google.com/architecture/framework/security/shared-responsibility-model)**

---

## :material-gavel: Admission Controller Readiness

<div class="grid cards" markdown>

-   :material-police-badge: **Policy Status**
    ---
    {% if failed_rules == 0 -%}
    <span style="color: {{ compliance_color }}; font-size: 2.2em; font-weight: 900;">READY</span>
    <br><span style="font-size: 0.8em;">*Seamless Production Scheduling*</span>
    {% else -%}
    <span style="color: {{ compliance_color }}; font-size: 2.2em; font-weight: 900;">BLOCKED</span>
    <br><span style="font-size: 0.8em;">*Hardening Exceptions Needed*</span>
    {% endif -%}

-   :material-lock-check: **Rules Verified**
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
    
    *Policy Violations Found*

</div>

{% if failed_rules > 0 %}
!!! critical "Security Violation"
    The Distroless image has failed specific PSS-Restricted rules. This is highly unusual for a distroless build and requires immediate investigation of the build layers.
{% else %}
!!! success "Zero-Exception Deployment"
    This image is **100% compliant** with the Kubernetes Restricted Pod Security Standard. It can be deployed into hardened namespaces with the strictest admission webhooks enabled.
{% endif %}

---

## :material-clipboard-list-outline: Policy Enforcement Matrix

| ID | Restriction Rule | Severity | Static Audit |
| :---: | :--- | :---: | :---: |
{% for rule in pss_data['SummaryControls'] -%}
{% if rule['TotalFail'] == 0 -%}
| `{{ rule['ID'] }}` | **{{ rule['Name'] }}** | <span style="color: #616161;">{{ rule['Severity'] }}</span> | :material-shield-check:{ .md-typeset__success title="Compliant" } |
{% else -%}
| `{{ rule['ID'] }}` | **{{ rule['Name'] }}** | <span style="color: #d50000; font-weight: bold;">{{ rule['Severity'] }}</span> | :material-shield-off:{ .md-typeset__error title="Non-Compliant" } |
{% endif -%}
{% endfor %}

---

## :material-security: Why Distroless + Restricted PSS?

Combining **Distroless** with the **Restricted PSS Profile** provides the "Gold Standard" of cloud security:

1.  **No Shell/Utilities:** Automatically complies with the rule against unnecessary binaries that could aid in container escape.
2.  **Explicit Non-Root:** The image is built to run as a non-privileged user, ensuring compatibility with `runAsNonRoot: true`.
3.  **Minimal Attack Surface:** Reduces the number of syscalls an attacker can attempt, perfectly complementing the `RuntimeDefault` seccomp policy.

---
[:material-arrow-up: Back to Top](#kubernetes-pss-restricted-profile-distroless)