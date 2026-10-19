#!/usr/bin/env bash
set -euo pipefail

# Llama a la API local protegida con un token OAuth2.
# Uso:
#   export ACCESS_TOKEN=... \
#   ./scripts/call-api.sh

if [[ -z "${ACCESS_TOKEN:-}" ]]; then
  echo "Error: ACCESS_TOKEN no está definido." >&2
  exit 1
fi

API_URL="${API_URL:-http://localhost:4010/api/products}"

curl -sS -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Accept: application/json" \
  -D - \
  "${API_URL}"
