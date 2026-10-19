# 🔐 Laboratorio: OAuth2 Authorization Code Flow con PKCE en Azure AD

## 🧾 Descripción
Este laboratorio muestra cómo proteger una API local con tokens JWT emitidos por Microsoft Entra ID (Azure AD) utilizando el flujo OAuth2 Authorization Code con PKCE.  
El flujo PKCE elimina la necesidad de un client secret y permite que aplicaciones públicas (SPA, móviles, scripts) realicen autenticación segura.

---

# 🏛️ Arquitectura del flujo

Usuario / Navegador  
→ Solicita acceso a la aplicación

Azure AD / Microsoft Entra ID  
→ Emite authorization code + PKCE challenge

Cliente (SPA / Script / App pública)  
→ Intercambia authorization code usando code_verifier

Azure AD  
→ Emite access_token + refresh_token

API local (Node.js + Express)  
→ Valida JWT usando JWKS

Respuesta  
→ Datos protegidos

---

# ❓ ¿Por qué PKCE?
PKCE asegura el flujo Authorization Code en clientes que **no pueden almacenar secretos**.  
El servidor comprueba que el code_verifier coincide con el code_challenge original, evitando ataques de interceptación del authorization code.

---

# 🧩 1. Registro de aplicaciones en Azure AD

Se registran dos aplicaciones:

### ✔️ Aplicación cliente (SPA / script)
- No usa client secret  
- Debe permitir flujo Authorization Code + PKCE  
- Debe tener permisos delegados sobre la API

### ✔️ API protegida (Resource API)
Debe exponer un scope, por ejemplo:

```
api://<api-client-id>/access_as_user
```

---

# 🧩 2. Generación de PKCE

El cliente genera:

- **code_verifier** → cadena aleatoria de 43–128 caracteres  
- **code_challenge** → `BASE64URL(SHA256(code_verifier))`

Script incluido en el laboratorio:

```
./api-local/scripts/generate-pkce.sh
```

---

# 🧩 3. Construcción de la URL de autorización

```
[https://login.microsoftonline.com/](https://login.microsoftonline.com/)<tenant-id>/oauth2/v2.0/authorize
  ?client_id=<client-id>
  &response_type=code
  &redirect_uri=http://localhost/callback
  &response_mode=query
  &scope=api://<api-client-id>/access_as_user
  &state=123456
  &code_challenge=<code_challenge>
  &code_challenge_method=S256
```

---

# 🧩 4. Obtención del authorization_code

Tras autenticarse, Azure AD redirige a:

```
http://localhost/callback?code=<authorization_code>&state=123456
```

---

# 🧩 5. Intercambio del authorization_code por token

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

Respuesta:

- access_token  
- refresh_token  
- expires_in  
- token_type  

---

# 🧩 6. Validación del JWT en la API local

La API **no confía en el cliente**.  
Valida el token usando JWKS:

```
https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys
```

Se verifica:

- `iss`  
- `aud`  
- `exp`  
- `nbf`  
- firma RS256  
- `kid` presente en JWKS  

Código relevante:
- `api-local/server.js`  
- `api-local/utils/validateToken.js`

---

# ⚠️ Errores comunes

### ❌ Error 501481  
Falta autorización o flujo PKCE no habilitado.

Soluciones:
- Usar `response_type=code`  
- Usar `code_challenge_method=S256`  
- Revisar `redirect_uri`  
- Habilitar *public client flows* si aplica  

---

### ❌ Error 90013  
Falta consentimiento o permisos delegados.

Soluciones:
- Conceder permisos delegados  
- Aceptar consentimiento administrativo  
- Revisar scope correcto  

---

### ❌ Token inválido en la API local

Causas:
- `aud` incorrecto  
- `iss` incorrecto  
- firma no válida  
- token expirado  

Soluciones:
- Revisar `.env`  
- Revisar `API_AUDIENCE`  
- Revisar `AZURE_TENANT_ID` y `AZURE_CLIENT_ID`  

---

# 🧪 Pasos del laboratorio

1. Instalar dependencias:
   ```bash
   cd api-local
   npm install
   ```

2. Iniciar API:
   ```bash
   npm start
   ```

3. Generar PKCE:
   ```bash
   ./scripts/generate-pkce.sh
   ```

4. Construir URL de autorización  
5. Autenticarse y obtener authorization_code  
6. Intercambiar código por token:
   ```bash
   ./scripts/exchange-token.sh
   ```

7. Consumir API:
   ```bash
   export ACCESS_TOKEN="<access_token>"
   ./scripts/call-api.sh
   ```

---

# 🧩 Buenas prácticas

- Nunca enviar client secret en clientes públicos  
- Usar siempre `S256`  
- Validar JWT en la API, no en el front-end  
- Mantener `redirect_uri` exacto  
- Revisar permisos y consentimiento  

---

# ✔️ Conclusión
PKCE añade una capa crítica de seguridad al flujo Authorization Code en aplicaciones públicas.  
Combinado con validación JWT mediante JWKS en la API, se obtiene un modelo robusto para proteger recursos y garantizar acceso seguro.
