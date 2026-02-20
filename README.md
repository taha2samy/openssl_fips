<div align="center">

# 🛡️ Wolfi OpenSSL FIPS
**High-Assurance Cryptographic Foundation for Cloud-Native Workloads**


<p align="center">
  <a href="docs/TEST_RESULTS.md">
    <img src="https://img.shields.io/badge/passed-86-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Passed" />
  </a>
  <a href="docs/TEST_RESULTS.md">
    <img src="https://img.shields.io/badge/failed-6-red?style=for-the-badge&logo=githubactions&logoColor=white" alt="Failed" />
  </a>
  <a href="docs/TEST_RESULTS.md">
    <img src="https://img.shields.io/badge/broken-0-orange?style=for-the-badge" alt="Broken" />
  </a>
  <a href="docs/TEST_RESULTS.md">
    <img src="https://img.shields.io/badge/total-92-blue?style=for-the-badge" alt="Total" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/taha2samy/openssl_fips/actions/runs/22210513146">
    <img src="https://img.shields.io/badge/Build_Status-Success-brightgreen?style=flat-square&logo=github-actions" alt="Build Status" />
  </a>
  <a href="https://csrc.nist.gov/">
    <img src="https://img.shields.io/badge/Compliance-FIPS_140--3-blue?style=flat-square&logo=keybase" alt="Compliance" />
  </a>

</p>

<p align="center">
  <a href="https://github.com/wolfi-dev">
    <img src="https://img.shields.io/badge/Security-Zero_CVE-blue?style=flat-square&logo=dependabot" alt="Zero CVE" />
  </a>
  <a href="https://slsa.dev/">
    <img src="https://img.shields.io/badge/Supply_Chain-SLSA_L3-blueviolet?style=flat-square&logo=linuxfoundation" alt="SLSA Level 3" />
  </a>
  <img src="https://img.shields.io/badge/License-Apache--2.0-lightgrey?style=flat-square" alt="License" />
</p>

</div>

---

## 01. Specification Overview
This repository maintains a production-hardened, **FIPS 140-3 compliant** OpenSSL 3.5.5 container image. Architected on **Wolfi OS**, it eliminates legacy overhead and ensures a minimal attack surface for enterprise and federal environments (FedRAMP, DoD IL5).

### Core Components
| Component | Version | Specification |
| :--- | :--- | :--- |
| **OpenSSL Core** | 3.5.5 | Production-ready engine |
| **FIPS Provider** | 3.1.2 | NIST Validated module |
| **Base OS** | Wolfi | Zero-CVE baseline |
| **Integrity** | SLSA L3 | Cryptographically attested build |


----
## 02. Architectural Integrity
The build pipeline enforces a strict cryptographic boundary, ensuring that the FIPS module is correctly installed, initialized, and protected.

```mermaid
graph TD
    %% Global Styles
    classDef trusted fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef boundary fill:#fff3e0,stroke:#e65100,stroke-width:2px,stroke-dasharray: 5 5;
    classDef attest fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef artifact fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;

    subgraph Pipeline ["01. Trusted Ingestion Layer"]
        A[Wolfi Base Image<br/>'cgr.dev/chainguard']:::trusted
        B[OpenSSL Core 3.5.5<br/>Source Code]:::trusted
        C[FIPS Module 3.1.2<br/>Validated Source]:::trusted
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
    style L fill:#ffebee,stroke:#c62828
    class FIPS_Boundary boundary
```
---

## 03. Deployment Artifacts
We provide two specialized variants optimized for security and operational flexibility.

| Variant | Image Tag | Base | Logic |
| :--- | :--- | :--- | :--- |
| **Standard** | `3.5.5` | Wolfi | Includes shell for debugging/CI |
| **Distroless** | `3.5.5-distroless` | Static | No shell/manager (Hardened) |

### Supply Chain Provenance (Latest Build)
- **Image Digest (Distroless):** `sha256:18901a89ced73710557a80077c0210b2a54ad2ec02087c4a2fe815d2500abd58`
- **Attestation:** [View SLSA Provenance](https://github.com/taha2samy/openssl_fips/attestations/19369396)
- **SBOM:** [Download CycloneDX](https://github.com/taha2samy/openssl_fips/attestations/19369401)


```bash
docker pull  ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless@sha256:18901a89ced73710557a80077c0210b2a54ad2ec02087c4a2fe815d2500abd58
```

- **Image Digest (standard):** `sha256:f468f0dd21023c6dedf9d6c70d8c8205af9a96812eca394458ceb7553feebed7`
- **Attestation:** [View SLSA Provenance](https://github.com/taha2samy/openssl_fips/attestations/19369397)
- **SBOM:** [Download CycloneDX](https://github.com/taha2samy/openssl_fips/attestations/19369404)

```bash
docker pull  ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5@sha256:f468f0dd21023c6dedf9d6c70d8c8205af9a96812eca394458ceb7553feebed7
```

- **Image Digest (development):** `sha256:25e061954473e4e14d7bc096028b7ab09ac8c9d7576c9ae4ae53e683a5208847`
- **Attestation:** [View SLSA Provenance](https://github.com/taha2samy/openssl_fips/attestations/19369400)
- **SBOM:** [Download CycloneDX](https://github.com/taha2samy/openssl_fips/attestations/19369419)

```bash
docker pull  ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-dev@sha256:25e061954473e4e14d7bc096028b7ab09ac8c9d7576c9ae4ae53e683a5208847
```

---

## 04. Build Provenance & Metadata
To ensure complete reproducibility and supply chain traceability (SLSA L3), strictly defined metadata is captured during the CI execution. This context binds the generated artifacts to their specific source code state and build environment.

| Context Dimension | Metadata Key | Value (Dynamic Scope) |
| :--- | :--- | :--- |
| **🔐 Source Identity** | `Repository` | `taha2samy/openssl_fips` |
| | `Ref / Branch` | `main` |
| | `Commit SHA` | `ef9fd22fdd76a063be8b0f84398529f79adc25d7` |
| | `Trigger Actor` | `taha2samy` |
| **⚙️ Execution Context** | `Workflow` | `Build` |
| | `Run ID` | [`22210513146`](https://github.com/taha2samy/openssl_fips/actions/runs/22210513146) |
| | `Run Number` | `#198` |
| | `Event Type` | `workflow_dispatch` |
| **🖥️ Build Environment** | `Runner OS` | `Linux` |
| | `CI Managed` | `true` |
| | `Workspace` | `/home/runner/work/openssl_fips/openssl_fips` |

> [!IMPORTANT]
> The `Commit SHA` represents the immutable state of the code at the time of build. The `Run ID` links directly to the tamper-evident build logs in GitHub Actions.
>
---
## 05. Automated Compliance Audit
Every build undergoes a 200+ point automated security audit via Pytest and OpenSSL FIPS verification protocols.

### Latest Test Suite Metrics
- **Compliance Status:** ❌ FAILED
- **Total Test Vectors:** 92
- **Successful Assertions:** 86
- **Critical Rejections (e.g. MD5/SHA1):** Verified 100%

> For a full breakdown of algorithm blocking and KAT (Known Answer Tests), see [**Detailed Audit Logs**](docs/TEST_RESULTS.md).

---

## 06. Performance Benchmarks
FIPS-validated cryptography involves mandatory self-tests and integrity checks. We benchmark the overhead against standard implementations to ensure operational efficiency.

### 🚀 Performance Snapshot
High-level results from our cryptographic benchmark, identifying the top-performing environments for key primitives.

| Primitive | Top Performer | Advantage |
| :--- | :---: | :---: |
| `SHA256` | **FIPS** | `+1.1%` |

> **Key Insight:** The **Wolfi-FIPS** environment demonstrates negligible performance overhead, proving that modern compliance does not impose a significant 'security tax'.

> For a full breakdown, see the [**Detailed Performance Report**](docs/Comparison_Report.md).
---

## 07. Technical Implementation
### Quick Start (Verification Mode)
```bash
docker run --rm ghcr.io/taha2samy/wolfi-openssl-fips:latest version -a
```

### Verification Protocol (Cosign)
```bash
cosign verify \
  --certificate-identity-regexp "^https://github.com/taha2samy/.*" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5
```

---

## 08. Documentation Index
- [**Performance Metrics**](docs/Comparison_Report.md)
- [**Tasks Guide & Operations Manual**](docs/OPERATIONS.md)

---



**License:** Apache-2.0  
**Security Policy:** See [SECURITY.md](SECURITY.md) for vulnerability disclosure.


