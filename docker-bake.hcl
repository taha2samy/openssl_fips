variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "CORE_VERSION" {
  default = "3.5.5"
}

variable "CORE_SHA256" {
  default = ""
}

variable "REGISTRY" {
  default = "ghcr.io"
}

variable "REPO" {
  default = "taha2samy/wolfi_os"
}

group "default" {
  targets = ["standard", "distroless"]
}

target "common" {
  context    = "."
  dockerfile = "Dockerfile"
  platforms  = ["linux/amd64", "linux/arm64"]
  args = {
    FIPS_VERSION = "${FIPS_VERSION}"
    CORE_VERSION = "${CORE_VERSION}"
    BASE_IMAGE   = "${BASE_IMAGE}"
    STATIC_IMAGE = "${STATIC_IMAGE}"
  }
}

target "standard" {
  inherits   = ["common"]
  target     = "openssl-standard"
  tags       = ["${REGISTRY}/${REPO}-base:latest", "${REGISTRY}/${REPO}:${CORE_VERSION}"]
  cache-from = ["type=registry,ref=${REGISTRY}/${REPO}-base:cache"]
  cache-to   = ["type=gha,mode=max,ref=${REGISTRY}/${REPO}-distroless:cache"]
  attest = [
    "type=provenance,mode=max",
    "type=sbom,format=cyclonedx-json"
  ]
}

target "distroless" {
  inherits   = ["common"]
  target     = "openssl-distroless"
  tags       = ["${REGISTRY}/${REPO}-distroless:latest", "${REGISTRY}/${REPO}:${CORE_VERSION}-distroless"]
  cache-from = ["type=registry,ref=${REGISTRY}/${REPO}-distroless:cache"]
  cache-to   = ["type=gha,mode=max,ref=${REGISTRY}/${REPO}-distroless:cache"]
  attest = [
    "type=provenance,mode=max",
    "type=sbom,format=cyclonedx-json"
  ]
}
