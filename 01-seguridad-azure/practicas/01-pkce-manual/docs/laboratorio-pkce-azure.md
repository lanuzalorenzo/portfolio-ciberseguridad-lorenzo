# Laboratorio — OAuth 2.0 Authorization Code con PKCE

> **En fácil:** una aplicación pública pide permiso a Microsoft Entra ID sin guardar ninguna contraseña. Entra ID devuelve un pase temporal y la API comprueba que el pase es auténtico antes de responder. Es como una consigna: se entrega un resguardo, no la llave maestra.

## Descripción

Este laboratorio muestra cómo proteger una API local con tokens JWT emitidos por Microsoft Entra ID (Azure AD) mediante el flujo OAuth 2.0 Authorization Code con PKCE. PKCE elimina la necesidad de un client secret y permite que aplicaciones públicas (SPA, móviles, scripts) se autentiquen sin guardar credenciales.

## Arquitectura del flujo

| Paso | Quién | Qué ocurre |
|---|---|---|
| 1 | Usuario o navegador | Solicita acceso a la aplicación |
| 2 | Microsoft Entra ID | Emite authorization code y PKCE challenge |
| 3 | Cliente (SPA, script, app pública) | Intercambia el authorization code usando `code_verifier` |
| 4 | Microsoft Entra ID | Emite `access_token` y `refresh_token` |
| 5 | API local (Node.js + Express) | Valida el JWT usando JWKS |
| 6 | API local | Devuelve los datos protegidos |

## ¿Por qué PKCE?

PKCE protege el flujo Authorization Code en clientes que no pueden almacenar secretos. El servidor comprueba que el `code_verifier` coincide con el `code_challenge` original, lo que evita el uso de un authorization code interceptado.

## 1. Registro de aplicaciones en Azure AD

Se registran dos aplicaciones.

### Aplicación cliente (SPA o script)

- No usa client secret.
- Debe permitir el flujo Authorization Code + PKCE.
- Debe tener permisos delegados sobre la API.

### API protegida (recurso)

Debe exponer un scope, por ejemplo:

```text
api://<api-client-id>/access_as_user
```

## 2. Generación de PKCE

El cliente genera dos valores:

- `code_verifier`: cadena aleatoria de 43 a 128 caracteres.
- `code_challenge`: `BASE64URL(SHA256(code_verifier))`.

Script incluido en el laboratorio:

```bash
./api-local/scripts/generate-pkce.sh
```

## 3. Construcción de la URL de autorización

```text
https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize
  ?client_id=<client-id>
  &response_type=code
  &redirect_uri=http://localhost/callback
  &response_mode=query
  &scope=api://<api-client-id>/access_as_user
  &state=123456
  &code_challenge=<code_challenge>
  &code_challenge_method=S256
```

## 4. Obtención del authorization code

Tras autenticarse, Entra ID redirige a:

```text
http://localhost/callback?code=<authorization_code>&state=123456
```

## 5. Intercambio del código por token

```bash
curl -X POST \
  "https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "client_id=<client-id>" \
  --data-urlencode "scope=api://<api-client-id>/access_as_user" \
  --data-urlencode "code=<authorization_code>" \
  --data-urlencode "redirect_uri=http://localhost/callback" \
  --data-urlencode "grant_type=authorization_code" \
  --data-urlencode "code_verifier=<code_verifier>"
```

La respuesta contiene:

- `access_token`
- `refresh_token`
- `expires_in`
- `token_type`

## 6. Validación del JWT en la API local

La API no confía en el cliente: valida el token con las claves JWKS publicadas en:

```text
https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys
```

Se verifica:

- `iss`
- `aud`
- `exp`
- `nbf`
- firma RS256
- que el `kid` esté presente en JWKS

El código relevante está en `api-local/server.js` y `api-local/utils/validateToken.js`.

## 7. Errores comunes

### Error 501481

Falta autorización o el flujo PKCE no está habilitado. Comprueba:

- `response_type=code`
- `code_challenge_method=S256`
- `redirect_uri`
- *public client flows*, si aplica

### Error 90013

Falta consentimiento o permisos delegados. Comprueba:

- los permisos delegados concedidos
- el consentimiento administrativo
- el scope solicitado

### Token inválido en la API local

Causas: `aud` incorrecto, `iss` incorrecto, firma no válida o token expirado.

Revisa `.env`, `API_AUDIENCE`, `AZURE_TENANT_ID` y `AZURE_CLIENT_ID`.

## 8. Pasos del laboratorio

1. Instalar dependencias:

   ```bash
   cd api-local
   npm install
   ```

2. Iniciar la API:

   ```bash
   npm start
   ```

3. Generar PKCE:

   ```bash
   ./scripts/generate-pkce.sh
   ```

4. Construir la URL de autorización.

5. Autenticarse y obtener el authorization code.

6. Intercambiar el código por un token:

   ```bash
   ./scripts/exchange-token.sh
   ```

7. Consumir la API:

   ```bash
   export ACCESS_TOKEN="<access_token>"
   ./scripts/call-api.sh
   ```

## 9. Buenas prácticas

- No enviar client secret en clientes públicos.
- Usar siempre S256.
- Validar el JWT en la API, no en el front-end.
- Mantener el `redirect_uri` exacto.
- Revisar permisos y consentimiento.

## 10. Conclusión

PKCE añade una capa de seguridad al flujo Authorization Code en aplicaciones públicas. La validación del JWT con JWKS completa el modelo: la API no confía en lo que le envía el cliente.
