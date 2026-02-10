#!/bin/bash
set -e
OUTFILE="versions.hcl"
echo "" > "$OUTFILE"

declare -A IMAGES
IMAGES=(
  ["STATIC_IMAGE"]="cgr.dev/chainguard/static"
  ["BASE_IMAGE"]="cgr.dev/chainguard/wolfi-base"
)

for var in "${!IMAGES[@]}"; do
  image="${IMAGES[$var]}"
  
  digest=$(docker manifest inspect "$image:latest" -v | jq -r 'if type=="array" then .[0].Descriptor.digest else .Descriptor.digest end' 2>/dev/null || \
           docker pull "$image:latest" >/dev/null && docker inspect --format='{{index .RepoDigests 0}}' "$image:latest" | cut -d'@' -f2)

  if [ -z "$digest" ] || [ "$digest" == "null" ]; then
    echo "Error: Could not find digest for $image"
    exit 1
  fi

  cat >> "$OUTFILE" <<EOL
variable "$var" {
  default = "$image@$digest"
}

EOL
done
