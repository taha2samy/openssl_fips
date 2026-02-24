# :material-link-lock: Supply Chain Security (SLSA L3)

In the era of software supply chain attacks (like SolarWinds), trusting a binary is no longer enough. You must verify its provenance. 

This project implements a **SLSA Level 3 (Supply-chain Levels for Software Artifacts)** compliant build pipeline. This guarantees that the artifact you deploy was built from the source code you see, by the builder you trust, in a tamper-evident environment.

---

## :material-shield-check: The Hermetic Build Pipeline

Our build process is **hermetic**, meaning it runs in an isolated environment with no network access during the compilation phase (except for explicitly defined inputs).

- **:material-source-commit: Pinned Dependencies:** All base images and packages are pinned by SHA256 digest in `versions.hcl`. We do not use mutable tags like `:latest` in production builds.
- **:material-server-off: Ephemeral Environments:** Every build runs on a fresh, ephemeral GitHub Actions runner that is destroyed immediately after use.
- **:material-fingerprint: OIDC Identity:** The builder authenticates itself using OpenID Connect (OIDC) to Sigstore, binding the artifact to the specific workflow run and git commit.

---

## :material-file-document-check: Attestation & Verification

Every image pushed to the registry is accompanied by a cryptographic attestation bundle.

### 1. Provenance (How it was built)
The provenance attestation describes the builder, the source code repository, the commit SHA, and the build instructions.

- **Builder ID:** `https://github.com/slsa-framework/slsa-github-generator`
- **Build Type:** `https://github.com/slsa-framework/slsa-github-generator/container@v1`

### 2. SBOM (What is inside)
We generate a **Software Bill of Materials (SBOM)** in CycloneDX format for every image. This lists every package, library, and file inside the container, allowing for automated vulnerability scanning.

| Artifact Variant | Provenance Link | SBOM Link |
| :--- | :--- | :--- |
| **Distroless** | [:material-link: View Attestation]({{ distroless_url }}) | [:material-download: Download CycloneDX]({{ distroless_sbom_url }}) |
| **Standard** | [:material-link: View Attestation]({{ standard_url }}) | [:material-download: Download CycloneDX]({{ standard_sbom_url }}) |
| **Development** | [:material-link: View Attestation]({{ dev_url }}) | [:material-download: Download CycloneDX]({{ dev_sbom_url }}) |

---

## :material-console: Verifying Artifacts

You can verify the integrity and provenance of our images using `cosign`. This ensures the image has not been tampered with since it left our CI pipeline.

```bash
# verify the image signature and identity
cosign verify \
  --certificate-identity-regexp "^https://github.com/{{ owner }}/.*" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  {{ registry }}/{{ owner }}/{{ repo_name }}:{{ core_version }}
```



!!! success "Verification Guarantee"
    A successful verification proves that:

    1. The image was built by **GitHub Actions**.
    2. The source code came from **{{ repo_url }}**.
    3. The build was triggered by a trusted workflow.

