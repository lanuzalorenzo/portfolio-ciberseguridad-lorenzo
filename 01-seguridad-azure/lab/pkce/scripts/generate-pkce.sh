#!/usr/bin/env bash
set -euo pipefail

# Genera un code_verifier y code_challenge para PKCE.
# Uso: ./scripts/generate-pkce.sh

if ! command -v openssl >/dev/null 2>&1; then
  echo "Error: openssl no está instalado." >&2
  exit 1
fi

code_verifier=$(openssl rand -base64 96 | tr '+/' '-_' | tr -d '=')
code_challenge=$(printf '%s' "$code_verifier" | openssl dgst -sha256 -binary | openssl base64 -A | tr '+/' '-_' | tr -d '=')

printf 'code_verifier=%s\n' "$code_verifier"
printf 'code_challenge=%s\n' "$code_challenge"
printf '\nCopiar estos valores en la configuración del cliente Azure AD o en la URL de autorización.\n'
