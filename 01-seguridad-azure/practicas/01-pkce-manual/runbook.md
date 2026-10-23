# Runbook — PKCE manual con cliente público

> **Estado:** Runbook preparado. Ejecución estandarizada pendiente; existe una ejecución histórica documentada en la [bitácora del módulo](../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md).
>
> **Última revisión:** 2026-10-19.
>
> **Objetivo:** ejecutar a mano el flujo OAuth2 Authorization Code + PKCE contra Microsoft Entra ID, canjear el código por un token y validar el JWT en una API local mediante JWKS.

> Este documento explica cómo pedir un token a Microsoft Entra ID a mano, sin guardar ninguna contraseña de aplicación, y cómo comprobar que la API solo acepta tokens legítimos. Se ejecuta en local y no despliega nada en Azure.

## 1. Prerrequisitos y permisos

- Node.js 18 o superior y npm.
- `curl`, `openssl`, `bash` y, opcionalmente, `jq`.
- Un tenant de Microsoft Entra ID con permisos para registrar aplicaciones.
- Dos registros de aplicación:
  - **Cliente público:** permite flujo Authorization Code + PKCE, sin secreto, con redirect URI `http://localhost/callback`.
  - **API protegida:** expone el scope `access_as_user` y tiene el cliente público autorizado con consentimiento delegado.
- No se despliegan recursos de Azure. Los registros de aplicación viven en el tenant.

> Si no tienes tenant, este runbook queda en estado **Runbook preparado**. No lo marques como validado sin ejecutarlo.

## 2. Variables y nombres

Sustituye los placeholders por los valores de tu laboratorio:

| Variable | Valor de ejemplo | Uso |
|---|---|---|
| `AZURE_TENANT_ID` | `<tenant-id>` | Autoridad y JWKS |
| `AZURE_CLIENT_ID` | `<client-id>` | Cliente público que solicita el token |
| `AZURE_API_CLIENT_ID` | `<api-client-id>` | API que expone `access_as_user` |
| `REDIRECT_URI` | `http://localhost/callback` | Redirección del cliente público |
| `REQUESTED_SCOPE` | `api://<api-client-id>/access_as_user` | Scope solicitado |

No publiques estos identificadores en capturas, logs ni evidencia. Redáctalos siempre.

## 3. Comandos copiables

### 3.1 Preparar la API

Terminal 1:

```bash
cd 01-seguridad-azure/lab/pkce
npm install
cp .env.example .env
# edita .env con los valores del tenant; no lo subas a Git
npm start
```

**Punto de control:** `http://localhost:4010/health` responde `{"ok":true,...}`.

### 3.2 Generar PKCE

Terminal 2:

```bash
cd 01-seguridad-azure/lab/pkce
./scripts/generate-pkce.sh | tee /tmp/pkce.txt
```

**Resultado esperado:** dos líneas con `code_verifier=...` y `code_challenge=...`.

Guarda el `code_verifier`; lo necesitarás en el canje. El `code_challenge` es `BASE64URL(SHA256(code_verifier))`.

### 3.3 Construir la URL de autorización

Sustituye los placeholders y abre la URL en el navegador:

```text
https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize
  ?client_id=<client-id>
  &response_type=code
  &redirect_uri=http%3A%2F%2Flocalhost%2Fcallback
  &response_mode=query
  &scope=api%3A%2F%2F<api-client-id>%2Faccess_as_user
  &state=123456
  &code_challenge=<code_challenge>
  &code_challenge_method=S256
```

Inicia sesión y acepta el consentimiento.

**Punto de control:** el navegador redirige a `http://localhost/callback?code=...&state=123456`. La página no cargará (no hay servidor en ese puerto), pero la barra de direcciones contiene el `authorization_code`. Cópialo.

### 3.4 Canjear el código por token

```bash
export AZURE_TENANT_ID='<tenant-id>'
export AZURE_CLIENT_ID='<client-id>'
export REDIRECT_URI='http://localhost/callback'
export CODE_VERIFIER='<code_verifier>'
export AUTHORIZATION_CODE='<authorization_code>'
export REQUESTED_SCOPE='api://<api-client-id>/access_as_user'

./scripts/exchange-token.sh | tee /tmp/azure-pkce-token-response.json
```

**Resultado esperado:** JSON con `token_type`, `scope`, `expires_in` y `access_token`. El script también guarda la respuesta completa en `/tmp/azure-pkce-token-response.json`.

Extrae el `access_token` y guárdalo en una variable de entorno. No lo publiques.

### 3.5 Llamar a la API protegida

```bash
export ACCESS_TOKEN='<access_token>'
./scripts/call-api.sh | tee /tmp/call-api-200.txt
```

**Resultado esperado:** `HTTP/1.1 200 OK` y un JSON con `ok`, el usuario y la lista de productos.

### 3.6 Pruebas negativas

Sin token:

```bash
curl -i http://localhost:4010/api/products | tee /tmp/call-api-401.txt
```

**Resultado esperado:** `HTTP/1.1 401 Unauthorized`.

Con token manipulado (cambia un carácter de la firma antes del último punto):

```bash
export TAMPERED_TOKEN="${ACCESS_TOKEN%?}X"
curl -i -H "Authorization: Bearer ${TAMPERED_TOKEN}" \
  http://localhost:4010/api/products | tee /tmp/call-api-tampered-401.txt
```

**Resultado esperado:** `HTTP/1.1 401 Unauthorized` con un mensaje de firma o claims no válidos.

## 4. Resultado esperado

- La API arranca y expone `/health` y `/api/products`.
- El flujo PKCE devuelve un `access_token` JWT.
- La API valida el token con JWKS y responde `200` con los productos.
- Sin token o con token manipulado responde `401`.
- Los errores `AADSTS501481` y `AADSTS90013` quedan documentados como referencia.

## 5. Evidencia que se debe capturar

Guarda las salidas en `evidencias/YYYY-MM-DD-01-pkce-manual/artefactos/` y redacta antes de publicar:

| Artefacto | Qué debe mostrar |
|---|---|
| `generate-pkce.txt` | Que se generaron `code_verifier` y `code_challenge`; no publiques los valores completos, solo longitudes o valores redactados |
| `authorize-url.txt` | URL con tenant y client ID redactados |
| `token-response.json` | `token_type`, `scope` y `expires_in`; elimina `access_token`, `refresh_token` e `id_token` |
| `call-api-200.txt` | `200` y número de productos; elimina `oid`, `preferred_username` y `name` |
| `call-api-401.txt` | `401` sin cabecera Authorization |
| `call-api-tampered-401.txt` | `401` con token manipulado |
| `cleanup.txt` | Parada de la API y eliminación de `.env` |

Reglas de redacción:

- Sin `access_token`, `refresh_token`, `id_token`, `authorization_code` ni `code_verifier`.
- Sin tenant ID, client ID, object ID ni UPN.
- Sin nombre de usuario, correo ni datos personales.
- Sin capturas que muestren la barra de direcciones con el código de autorización.

## 6. Prueba negativa o de control

- `GET /api/products` sin token debe devolver `401`.
- `GET /api/products` con un token manipulado debe devolver `401`.
- Si alguna de las dos devuelve `200`, la validación no está funcionando: no continúes.

## 7. Limpieza y restauración

- Detén la API con `Ctrl+C`.
- Elimina el fichero `.env` y la respuesta temporal:

```bash
rm -f 01-seguridad-azure/lab/pkce/.env
rm -f /tmp/azure-pkce-token-response.json /tmp/pkce.txt /tmp/call-api-*.txt
```

- Si creaste registros de aplicación solo para el laboratorio, elimínalos o documéntalos como pendientes de limpieza.
- No hay recursos de Azure desplegados que eliminar.

## 8. Coste y tiempo estimados

- **Coste:** 0. Solo tenant de laboratorio y ejecución local.
- **Tiempo:** 1–2 horas, incluyendo el registro de aplicaciones y la gestión del consentimiento.

## 9. Limitaciones y lo que no se ha ejecutado

- La ejecución histórica del 2026-09-02 está documentada en la bitácora, pero no se conservó como evidencia estandarizada.
- No hay tenant disponible en el momento de consolidar esta práctica; la ejecución queda pendiente.
- No hay tests automatizados ni CI para este laboratorio.
- La API es local y HTTP; no incluye TLS ni configuración de producción.
- La validación de scopes y roles granulares no forma parte de este laboratorio.
