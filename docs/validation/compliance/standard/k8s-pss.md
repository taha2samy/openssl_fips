{% set pss_data = standard_compliance.k8s_pss_restricted %}
{% set total_rules = pss_data.SummaryControls | length %}
{% set passed_rules = pss_data.SummaryControls | selectattr("TotalFail", "equalto", 0) | list | length %}
{% set failed_rules = total_rules - passed_rules %}
{% set compliance_color = "#00c853" if failed_rules == 0 else "#d50000" %}

# :fontawesome-brands-linux: Kubernetes PSS (Restricted Profile)

**Enforcement Level:** `Restricted` &nbsp;|&nbsp; **Scope:** `Workload Isolation` &nbsp;|&nbsp; **K8s Ver:** `v1.24+`

!!! abstract "Scope of Responsibility (Image vs. Runtime)"
    The Kubernetes Pod Security Standards (PSS) evaluate workload isolation. 
    This audit verifies the **static posture of the container image** (e.g., verifying it does not require root, lacks `setuid` binaries, and drops capabilities natively). However, full PSS enforcement occurs at the Kubernetes Admission Controller. Operators must still explicitly declare the required `securityContext` parameters (like `allowPrivilegeEscalation: false` and `runAsNonRoot: true`) in their deployment manifests to successfully schedule this image.

---

## :material-gavel: Admission Controller Readiness

<div class="grid cards" markdown>

-   :material-police-badge: **Policy Status**
    ---
    {% if failed_rules == 0 %}
    <span style="color: {{ compliance_color }}; font-size: 2.2em; font-weight: 900;">READY</span>
    <br><span style="font-size: 0.8em;">*Image is Restricted-Capable*</span>
    {% else %}
    <span style="color: {{ compliance_color }}; font-size: 2.2em; font-weight: 900;">BLOCKED</span>
    <br><span style="font-size: 0.8em;">*Fails Static Validation*</span>
    {% endif %}

-   :material-lock-check: **Rules Satisfied**
    ---
    <span style="font-size: 2.2em; font-weight: 900;">{{ passed_rules }}</span>
    <span style="color: #9e9e9e;"> / {{ total_rules }}</span>
    
    *Baseline + Restricted Policies*

-   :material-skull-crossbones: **Blocking Violations**
    ---
    {% if failed_rules == 0 %}
    <span style="color: #00c853; font-size: 2.2em; font-weight: 900;">0</span>
    {% else %}
    <span style="color: #d50000; font-size: 2.2em; font-weight: 900;">{{ failed_rules }}</span>
    {% endif %}
    
    *Requires Image Rebuild*

</div>

{% if failed_rules > 0 %}
!!! critical "Deployment Blocker"
    This image **CANNOT** run in a `Restricted` namespace. It violates core isolation principles natively within its layers (e.g., hardcoded root user, or required host namespaces).
{% else %}
!!! tip "Deployment Greenlight"
    This image is architecturally designed to satisfy the **Kubernetes Restricted Pod Security Standard**. It can be safely scheduled in highly regulated, multi-tenant environments without requesting PSP/PSA exceptions.
{% endif %}

---

## :material-clipboard-list-outline: Policy Enforcement Matrix

| ID | Restriction Rule | Impact Level | Static Enforcement |
| :---: | :--- | :---: | :---: |
{% for rule in pss_data.SummaryControls -%}
{% if rule.TotalFail == 0 -%}
| `{{ rule.ID }}` | **{{ rule.Name }}** | <span style="color: #616161;">{{ rule.Severity }}</span> | :material-check-all:{ .md-typeset__success title="Satisfied" } |
{% else -%}
| `{{ rule.ID }}` | **{{ rule.Name }}** | <span style="color: #d50000; font-weight: bold;">{{ rule.Severity }}</span> | :material-cancel:{ .md-typeset__error title="Violated" } |
{% endif -%}
{% endfor %}

---

## :material-lightbulb-outline: Why This Matters?

The **Restricted Profile** is the most stringent level of Kubernetes Pod security. Achieving image-level compliance here guarantees that your container:

1.  **Is Invisible to the Host:** Does not demand Host PID, IPC, or Network namespaces to function.
2.  **Operates with Zero Privilege:** Runs efficiently as a non-root user (`USER openssl`) and functions with all default Linux Capabilities dropped (`ALL`).
3.  **Is Sandbox-Ready:** Fully compatible with the `RuntimeDefault` seccomp profile to restrict the syscall attack surface.

> *For details on how operational duties are divided between Image Builders and Cluster Administrators, see the [Cloud Native Shared Responsibility Model]({{ "https://cloud.google.com/architecture/framework/security/shared-responsibility-model" }}).*