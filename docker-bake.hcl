variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "CORE_VERSION" {
  default = "3.5.5" 
}



variable "REGISTRY" {
  default = "ghcr.io"
}

variable "OWNER" {
  default = "taha2samy"
}

variable "REPO_NAME" {
  default = "wolfi-openssl-fips"
}

function "tag" {
  params = [tag_name]
  result = ["${REGISTRY}/${OWNER}/${REPO_NAME}:${tag_name}"]
}

group "default" {
  targets = ["standard", "distroless"]
}

target "common" {
  context    = "."
  dockerfile = "Dockerfile"
  platforms  = ["linux/amd64", "linux/arm64"]
  output = ["type=registry"]
  attest = [
  "type=sbom,generator=docker/buildkit-syft-scanner:v1.10.0,format=cyclonedx-json",
    "type=provenance,mode=max"
  ]
  args = {
    FIPS_VERSION = "${FIPS_VERSION}"
    CORE_VERSION = "${CORE_VERSION}"
        # --- Base Images ---
    BASE_IMAGE   = "${BASE_IMAGE}"
    STATIC_IMAGE = "${STATIC_IMAGE}"
    FIPS_VERSION = "${FIPS_VERSION}"
    CORE_VERSION = "${CORE_VERSION}"

    # --- Build Stage Packages (fips-builder & core-builder) ---
    BUILD_BASE_VER    = "${BUILD_BASE_VER}"
    PERL_VER          = "${PERL_VER}"
    LINUX_HEADERS_VER = "${LINUX_HEADERS_VER}"
    WGET_VER          = "${WGET_VER}"
    CA_CERTIFICATES_VER = "${CA_CERTIFICATES_VER}"

    # --- Runtime & Helper Packages (helper & openssl-standard) ---
    LIBSTDC_PLUS_PLUS_VER = "${LIBSTDC_PLUS_PLUS_VER}"
    ZLIB_VER              = "${ZLIB_VER}"
    TZDATA_VER            = "${TZDATA_VER}"
    POSIX_LIBC_UTILS_VER  = "${POSIX_LIBC_UTILS_VER}"
    

  }
}

### ---------- STANDARD IMAGE ----------
target "standard" {
  inherits = ["common"]
  target   = "openssl-standard"

  tags = concat(
    tag("${CORE_VERSION}"),
    tag("latest")
  )


  cache-from = ["type=registry,ref=${REGISTRY}/${OWNER}/${REPO_NAME}:build-cache-standard"]
  cache-to   = ["type=registry,ref=${REGISTRY}/${OWNER}/${REPO_NAME}:build-cache-standard,mode=max"]


}

### ---------- DISTROLESS IMAGE ----------
target "distroless" {
  inherits = ["common"]
  target   = "openssl-distroless"

  tags = concat(
    tag("${CORE_VERSION}-distroless"),
    tag("distroless")
  )


  cache-from = ["type=registry,ref=${REGISTRY}/${OWNER}/${REPO_NAME}:build-cache-distroless"]
  cache-to   = ["type=registry,ref=${REGISTRY}/${OWNER}/${REPO_NAME}:build-cache-distroless,mode=max"]


}
