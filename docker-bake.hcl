variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "CORE_VERSION" {
  default = "3.4.0" 
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
  platforms  = ["linux/amd64"]
  output = ["type=registry"]
  args = {
    FIPS_VERSION = FIPS_VERSION
    CORE_VERSION = CORE_VERSION
    BASE_IMAGE   = BASE_IMAGE
    STATIC_IMAGE = STATIC_IMAGE
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
  
  attest = [
    "type=provenance,mode=max",
    "type=sbom,format=cyclonedx-json"
  ]
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

  attest = [
    "type=provenance,mode=max",
    "type=sbom,format=cyclonedx-json"
  ]
}
