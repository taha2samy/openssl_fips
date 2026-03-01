
# 🏛️ System Architecture & Integrity

Our build pipeline enforces a strict cryptographic boundary, ensuring that the **FIPS 140-3 module** is correctly installed, initialized, and protected from tampering.

We rely on a **Hermetic Build** philosophy. This means zero external dependencies at build time, byte-for-byte reproducibility, and SLSA Level 3 provenance.

---

## :material-lock-pattern: The Cryptographic Boundary

The following architecture diagram illustrates the flow from trusted source ingestion down to the attested deployment artifacts. 

```mermaid
graph TD
    %% Global Styles
    classDef trusted fill:#009688,stroke:#004d40,stroke-width:2px,color:#ffffff;
    classDef boundary fill:#ff9800,stroke:#e65100,stroke-width:2px,stroke-dasharray: 6 4,color:#1a1a1a;
    classDef attest fill:#3f51b5,stroke:#1a237e,stroke-width:2px,color:#ffffff;
    classDef audit fill:#673ab7,stroke:#311b92,stroke-width:2px,color:#ffffff;
    classDef artifact fill:#e91e63,stroke:#880e4f,stroke-width:2px,color:#ffffff;
    classDef kics fill:#00b0ff,stroke:#01579b,stroke-width:2px,color:#ffffff;

    subgraph SAST ["00. Infrastructure SAST"]
        K1["KICS Security Audit<br/>'IaC & Dockerfile Static Analysis'"]:::kics
    end

    subgraph Ingestion ["01. Trusted Ingestion Layer"]
        A["Wolfi Base Image<br/>'Pinned Digest'"]:::trusted
        B["OpenSSL Core<br/>Source Code"]:::trusted
        C["FIPS Module<br/>Validated Source"]:::trusted
    end

    subgraph FIPS_Boundary ["02. Cryptographic Construction"]
        D["Compilation &<br/>Static Linking"]
        E["FIPS Install<br/>Integrity Protocol"]
        F{"KAT & POST<br/>Integrity Check"}
        D --> E --> F
    end

    subgraph Supply_Chain ["03. Supply Chain Security"]
        G["SBOM Generation<br/>'CycloneDX JSON'"]:::attest
        N["Dependency Graph<br/>'GitHub Submission'"]:::attest
        H["Sigstore Signing<br/>'Keyless OIDC'"]:::attest
        I["SLSA Provenance<br/>'Level 3 Verified'"]:::attest
        G --> N
    end

    subgraph Compliance ["04. Compliance Gates (4 Tests per Variant)"]
        direction TB
        subgraph Gates ["Trivy Security & Policy Engine"]
            T1["1. Vulnerability Scan"]
            T2["2. CIS Benchmark"]
            T3["3. NSA/CISA Guide"]
            T4["4. K8s PSS Restricted"]
        end
    end

    subgraph Artifacts ["05. Attested Artifacts"]
        J["Standard Image"]:::artifact
        K["Distroless Image"]:::artifact
        M["Development Image"]:::artifact
    end

    %% Flow Connections
    K1 -->|Audit Blueprints| Ingestion
    Ingestion -->|Verify & Build| FIPS_Boundary
    FIPS_Boundary -->|Passed Self-Tests| Supply_Chain
    Supply_Chain -->|Validate Runtimes| Gates

    %% Output to Final Artifacts
    Gates --> J
    Gates --> K
    Gates --> M

    %% Failure Path
    F -- Failed --> L["Build Aborted"]
    style L fill:#f44336,stroke:#b71c1c,color:#ffffff

    class FIPS_Boundary boundary
    class Gates audit
```

!!! info "Runtime Integrity Check (FIPS POST)"
    The FIPS POST (Power-On Self-Test) happens automatically on startup. If the `.so` binary is tampered with, the MAC verification fails and the container halts immediately.

---

## :material-shield-check: Deployment Variants

We provide specialized variants optimized for security and operational flexibility.

| Variant | Image Tag | Base OS | Intended Use Case |
| :--- | :--- | :--- | :--- |
| **Standard** | `{{ core_version }}` | Wolfi | Includes shell (`/bin/bash`) for debugging and CI pipelines. |
| **Distroless** | `{{ core_version }}-distroless` | Static | No shell/manager. Pure cryptographic engine for production. |
| **Development** | `{{ core_version }}-dev` | Wolfi (Dev) | Includes build tools (`gcc`, `make`) for compiling apps. |



!!! info "[:material-github: 360° Dependency Visibility]"
    Our security posture extends beyond the container itself. Every component in our software supply chain is tracked and monitored, including:

    *   All **OS Packages** within the `Standard`, `Distroless`, and `Development` images.
    *   The **Python (Pipenv) dependencies** used for our testing and automation scripts.
    *   The **GitHub Actions** (`user/action@vX`) that orchestrate our CI/CD pipeline.

    Every single one of these components is continuously monitored by the **GitHub Dependency Graph** and its integrated security advisory database. This provides real-time alerts for any newly discovered vulnerabilities across the entire stack.

    [**Explore the Live Dependency Graph for a Complete Inventory**](https://github.com/taha2samy/openssl_fips/network/dependencies)