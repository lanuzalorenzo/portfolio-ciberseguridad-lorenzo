# 📄 **Bitácora — Laboratorio PKCE + Azure AD**  
**Módulo:** 01 — Seguridad en Azure  
**Fecha:** 2026-09-02  

---

## 🎯 Objetivo de la práctica
Implementar un flujo OAuth2 Authorization Code + PKCE contra Azure AD y validar el token JWT en una API local mediante JWKS.

---

## 🛠 Trabajo realizado (cronológico)

### 1. Generación de PKCE
Se creó el script `api-local/scripts/generate-pkce.sh` para generar `code_verifier` y `code_challenge`.

```bash
cd api-local
./scripts/generate-pkce.sh
```

Resultado esperado:

```
code_verifier=...
code_challenge=...
```

---

### 2. Construcción de la URL de autorización
Se configuró la URL de Azure AD:

```
https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize
```

Parámetros utilizados:

- `client_id`
- `response_type=code`
- `redirect_uri=http://localhost:8080/callback`
- `scope=api://<api-client-id>/access_as_user`
- `code_challenge=<challenge>`
- `code_challenge_method=S256`
- `state=<valor aleatorio>`

---

### 3. Intercambio del authorization_code por token
Se creó el script `api-local/scripts/exchange-token.sh`.

```bash
export AZURE_TENANT_ID="<tenant-id>"
export AZURE_CLIENT_ID="<client-id>"
export REDIRECT_URI="http://localhost:8080/callback"
export CODE_VERIFIER="<code_verifier>"
export AUTHORIZATION_CODE="<authorization_code>"
./scripts/exchange-token.sh
```

Respuesta esperada:

```json
{
  "token_type": "Bearer",
  "expires_in": 3599,
  "access_token": "...",
  "refresh_token": "...",
  "scope": "api://<api-client-id>/access_as_user"
}
```

---

### 4. Validación del token en la API local
Se implementó `api-local/utils/validateToken.js` con validación de:

- `kid`
- `aud`
- `iss`
- `nbf`
- `exp`
- firma RS256 mediante JWKS

Endpoint JWKS:

```
https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys
```

---

## 🔍 Validaciones realizadas

### ✔️ Salud de la API
```bash
curl http://localhost:4010/health
```

Resultado esperado:

```json
{
  "ok": true,
  "status": "healthy",
  "service": "lab-azuread-oauth2-pkce-api"
}
```

### ✔️ Llamada sin token
```bash
curl http://localhost:4010/api/products
```

Resultado esperado:

```json
{
  "ok": false,
  "message": "Token no válido o caducado."
}
```

### ✔️ Llamada con token válido
```bash
export ACCESS_TOKEN="<access_token>"
curl -H "Authorization: Bearer $ACCESS_TOKEN" http://localhost:4010/api/products
```

Resultado esperado:

```json
{
  "ok": true,
  "message": "Acceso autorizado mediante OAuth2 PKCE + Azure AD.",
  "products": [ ... ]
}
```

---

## ⚠️ Problemas encontrados

### Error 501481
Causas:
- `redirect_uri` incorrecto  
- PKCE no habilitado  
- cliente mal configurado  

### Error 90013
Causas:
- falta consentimiento delegado  
- scope incorrecto  
- permisos no aceptados  

---

## 🛠 Soluciones aplicadas
- Ajuste del `redirect_uri`  
- Habilitación de PKCE  
- Validación del scope `access_as_user`  
- Consentimiento delegado aplicado  
- Revisión de parámetros del token y JWKS  

---

## 🔐 Implicaciones de seguridad
- PKCE evita ataques de interceptación del authorization_code.  
- La API valida firma, issuer y audiencia antes de permitir acceso.  
- Azure AD rota claves automáticamente mediante JWKS.  
- El flujo es adecuado para clientes públicos sin secretos.  

---

## 📎 Recursos útiles
- Azure AD OAuth2 v2.0  
- PKCE RFC 7636  
- JWKS Microsoft Entra ID  
- Node.js jwks-rsa  

---

## 📘 Estado final del laboratorio
- API local funcional  
- Validación JWT implementada  
- Scripts PKCE y token exchange operativos  
- Pruebas completadas  
- Documentación finalizada  
