variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "FIPS_SHA256" {
  default = "a0ce69b8b97ea6a35b96875235aa453b966ba3cba8af2de23657d8b6767d6539"
}

variable "CORE_VERSION" {
  default = "3.5.5"
}

variable "CORE_SHA256" {
  default = "b28c91532a8b65a1f983b4c28b7488174e4a01008e29ce8e69bd789f28bc2a89"
}

target "default" {
  context = "."
  dockerfile = "Dockerfile"
  platforms = ["linux/amd64"]
  args = {
    FIPS_VERSION = "${FIPS_VERSION}"
    FIPS_SHA256 = "${FIPS_SHA256}"
    CORE_VERSION = "${CORE_VERSION}"
    CORE_SHA256 = "${CORE_SHA256}"
  }
  tags = ["openssl-fips:wolfi-${CORE_VERSION}"]
}