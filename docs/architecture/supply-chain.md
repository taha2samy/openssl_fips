
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
        K1[":material-magnify-scan: KICS Security Audit<br/>'IaC & Dockerfile Static Analysis'"]:::kics
    end

    subgraph Ingestion ["01. Trusted Ingestion Layer"]
        A[":material-linux: Wolfi Base Image<br/>'Pinned Digest'"]:::trusted
        B[":material-code-braces: OpenSSL Core<br/>Source Code"]:::trusted
        C[":material-shield-lock: FIPS Module<br/>Validated Source"]:::trusted
    end

    subgraph FIPS_Boundary ["02. Cryptographic Construction"]
        D[":material-cog: Compilation &<br/>Static Linking"]
        E[":material-protocol: FIPS Install<br/>Integrity Protocol"]
        F{":material-microscope: KAT & POST<br/>Integrity Check"}
        D --> E --> F
    end

    subgraph Supply_Chain ["03. Supply Chain Security"]
        G[":material-file-document-check: SBOM Generation<br/>'CycloneDX JSON'"]:::attest
        N[":material-github: Dependency Graph<br/>'GitHub Submission'"]:::attest
        H[":material-fingerprint: Sigstore Signing<br/>'Keyless OIDC'"]:::attest
        I[":material-certificate: SLSA Provenance<br/>'Level 3 Verified'"]:::attest
        G --> N
    end

    subgraph Compliance ["04. Compliance Gates (4 Tests per Variant)"]
        direction TB
        subgraph Gates ["Trivy Security & Policy Engine"]
            T1[":material-shield-bug: 1. Vulnerability Scan"]
            T2[":material-docker: 2. CIS Benchmark"]
            T3[":material-kubernetes: 3. NSA/CISA Guide"]
            T4[":material-gavel: 4. K8s PSS Restricted"]
        end
    end

    subgraph Artifacts ["05. Attested Artifacts"]
        J[":material-console: Standard Image"]:::artifact
        K[":material-package-variant-closed: Distroless Image"]:::artifact
        M[":material-hammer-wrench: Development Image"]:::artifact
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
    F -- Failed --> L[Build Aborted]
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

