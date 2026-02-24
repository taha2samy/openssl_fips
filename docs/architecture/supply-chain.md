
# 🏛️ System Architecture & Integrity

Our build pipeline enforces a strict cryptographic boundary, ensuring that the **FIPS 140-3 module** is correctly installed, initialized, and protected from tampering.

We rely on a **Hermetic Build** philosophy. This means zero external dependencies at build time, byte-for-byte reproducibility, and SLSA Level 3 provenance.

---

## :material-lock-pattern: The Cryptographic Boundary

The following architecture diagram illustrates the flow from trusted source ingestion down to the attested deployment artifacts. 


```mermaid
graph TD
    %% Global Styles - High Contrast Palette (No White / No Black)
    classDef trusted fill:#009688,stroke:#004d40,stroke-width:2px,color:#ffffff;
    classDef boundary fill:#ff9800,stroke:#e65100,stroke-width:2px,stroke-dasharray: 6 4,color:#1a1a1a;
    classDef attest fill:#3f51b5,stroke:#1a237e,stroke-width:2px,color:#ffffff;
    classDef artifact fill:#e91e63,stroke:#880e4f,stroke-width:2px,color:#ffffff;

    subgraph Pipeline ["01. Trusted Ingestion Layer"]
        A[Wolfi Base Image<br/>'cgr.dev/chainguard']:::trusted
        B[OpenSSL Core {{ core_version }}<br/>Source Code]:::trusted
        C[FIPS Module {{ fips_version }}<br/>Validated Source]:::trusted
    end

    subgraph FIPS_Boundary ["02. FIPS 140-3 Cryptographic Boundary"]
        D[Compilation & Static Linking]
        E[fipsinstall Protocol]
        F{Integrity Self-Tests<br/>POST / KAT}

        D --> E
        E --> F
    end

    subgraph Security_Audit ["03. Attestation & Supply Chain"]
        G[SBOM Generation<br/>'CycloneDX']:::attest
        H[Cosign Keyless Signing<br/>'Sigstore/OIDC']:::attest
        I[SLSA Provenance<br/>'Level 3']:::attest
    end

    subgraph Artifacts ["04. Attested Artifacts"]
        J[Standard Image<br/>'Full Shell']:::artifact
        K[Distroless Image<br/>'Static Binary']:::artifact
    end

    %% Connections
    Pipeline -->|Integrity Check| FIPS_Boundary
    FIPS_Boundary -->|Validated MAC| Security_Audit
    Security_Audit --> J
    Security_Audit --> K

    %% Styling Labels
    F -- Passed --> Security_Audit
    F -- Failed --> L[Build Aborted]
    style L fill:#f44336,stroke:#b71c1c,color:#ffffff

    class FIPS_Boundary boundary
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

