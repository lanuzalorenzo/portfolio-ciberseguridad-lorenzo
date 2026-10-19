#!/usr/bin/env bash
set -euo pipefail

# Intercambia un authorization code por access_token usando PKCE.
# Requiere:
#   AZURE_TENANT_ID, AZURE_CLIENT_ID, REDIRECT_URI, CODE_VERIFIER, AUTHORIZATION_CODE
# Uso:
#   export AZURE_TENANT_ID=... \
#          AZURE_CLIENT_ID=... \
#          REDIRECT_URI=http://localhost:8080/callback \
#          CODE_VERIFIER=... \
#          AUTHORIZATION_CODE=...
#   ./scripts/exchange-token.sh

if [[ -z "${AZURE_TENANT_ID:-}" ]]; then
  echo "Error: AZURE_TENANT_ID no está definido." >&2
  exit 1
fi

if [[ -z "${AZURE_CLIENT_ID:-}" ]]; then
  echo "Error: AZURE_CLIENT_ID no está definido." >&2
  exit 1
fi

if [[ -z "${REDIRECT_URI:-}" ]]; then
  echo "Error: REDIRECT_URI no está definido." >&2
  exit 1
fi

if [[ -z "${CODE_VERIFIER:-}" ]]; then
  echo "Error: CODE_VERIFIER no está definido." >&2
  exit 1
fi

if [[ -z "${AUTHORIZATION_CODE:-}" ]]; then
  echo "Error: AUTHORIZATION_CODE no está definido." >&2
  exit 1
fi

if [[ -z "${REQUESTED_SCOPE:-}" ]]; then
  echo "Error: REQUESTED_SCOPE no está definido (por ejemplo, api://<api-client-id>/access_as_user)." >&2
  exit 1
fi

curl -sS -X POST "https://login.microsoftonline.com/${AZURE_TENANT_ID}/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "client_id=${AZURE_CLIENT_ID}" \
  --data-urlencode "scope=${REQUESTED_SCOPE}" \
  --data-urlencode "code=${AUTHORIZATION_CODE}" \
  --data-urlencode "redirect_uri=${REDIRECT_URI}" \
  --data-urlencode "grant_type=authorization_code" \
  --data-urlencode "code_verifier=${CODE_VERIFIER}" \
  -o /tmp/azure-pkce-token-response.json

cat /tmp/azure-pkce-token-response.json
printf '\n'
