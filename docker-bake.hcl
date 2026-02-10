variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "CORE_VERSION" {
  default = "3.5.5"
}

variable "REGISTRY" {
  default = "ghcr.io"
}

variable "REPO" {
  default = "taha2samy/wolfi_os"
}

group "default" {
  targets = ["base", "distroless"]
}

target "common" {
  context    = "."
  dockerfile = "Dockerfile"
  platforms  = ["linux/amd64", "linux/arm64"]

  args = {
    FIPS_VERSION = FIPS_VERSION
    CORE_VERSION = CORE_VERSION
  }
}

### ---------- BASE ----------
target "base" {
  inherits = ["common"]
  target   = "openssl-standard"

  tags = [
    "${REGISTRY}/${REPO}:latest"
  ]

  cache-from = [
    "type=registry,ref=${REGISTRY}/${REPO}:cache-base"
  ]

  cache-to = [
    "type=registry,ref=${REGISTRY}/${REPO}:cache-base,mode=max"
  ]

  attest = [
    "type=provenance,mode=max",
    "type=sbom,format=cyclonedx-json"
  ]
}

### ---------- DISTROLESS ----------
target "distroless" {
  inherits = ["common"]
  target   = "openssl-distroless"

  tags = [
    "${REGISTRY}/${REPO}-distroless:latest"
  ]

  cache-from = [
    "type=registry,ref=${REGISTRY}/${REPO}:cache-distroless"
  ]

  cache-to = [
    "type=registry,ref=${REGISTRY}/${REPO}:cache-distroless,mode=max"
  ]

  attest = [
    "type=provenance,mode=max",
    "type=sbom,format=cyclonedx-json"
  ]
}
