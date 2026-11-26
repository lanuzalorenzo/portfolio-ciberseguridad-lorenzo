# Comandos ejecutados

Sustituye `<tenant-id>`, `<client-id>` y `<api-client-id>` por los valores del laboratorio. No se guardan los valores reales, ni el `code_verifier`, ni el `code`, ni los tokens.

## 1. API local

```bash
cd 01-seguridad-azure/lab/pkce
npm install
cp .env.example .env
# editar .env con tenant, clientes, audiencia y scope
npm start
curl -fsS http://localhost:4010/health
```

Salida: `{"ok":true,"status":"healthy",...}`.

## 2. PKCE

```bash
./scripts/generate-pkce.sh
```

Salida: `code_verifier` de 128 caracteres y `code_challenge` de 43; se comprobó que `BASE64URL(SHA256(verifier))` coincide con el challenge.

## 3. Autorización

```text
https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize
  ?client_id=<client-id>
  &response_type=code
  &redirect_uri=http%3A%2F%2Flocalhost%2Fcallback
  &response_mode=query
  &scope=api%3A%2F%2F<api-id>%2F<scope>
  &state=<state>
  &code_challenge=<code_challenge>
  &code_challenge_method=S256
```

El navegador redirigió a `http://localhost/callback?code=...&state=<state>`. La página no carga porque no hay servidor en el puerto 80; el `code` se copia de la barra de direcciones.

## 4. Canje

```bash
export AZURE_TENANT_ID='<tenant-id>'
export AZURE_CLIENT_ID='<client-id>'
export REDIRECT_URI='http://localhost/callback'
export REQUESTED_SCOPE='api://<api-id>/<scope>'
export CODE_VERIFIER='<code_verifier>'
export AUTHORIZATION_CODE='<authorization_code>'
./scripts/exchange-token.sh
```

Salida redactada: `token_type`, `scope` y `expires_in`.

## 5. Pruebas

```bash
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" http://localhost:4010/api/products
curl -i http://localhost:4010/api/products
curl -i -H "Authorization: Bearer ${ACCESS_TOKEN}x" http://localhost:4010/api/products
```

Resultados: `200` con cuatro productos, `401` sin token y `401` con la firma manipulada.

## 6. Limpieza

```bash
kill "$(lsof -ti tcp:4010)"
rm .env
rm /tmp/azure-pkce-token-response.json /tmp/pkce.txt /tmp/redirect-url.txt
az account clear
docker rm -f pn-az-login
docker volume rm pn-az-cli
```
