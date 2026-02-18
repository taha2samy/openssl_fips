import json 
with open("all-metadata/distroless_attestation_details.json", "r") as f:
    distroless = json.load(f)

print(summary)
