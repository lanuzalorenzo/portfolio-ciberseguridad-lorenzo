# Bitácora — 2026-09-02: Laboratorio manual de OAuth2 PKCE

> [!NOTE]
> Los scripts mencionados viven ahora en `lab-api-local-azure`.

**Objetivo:** Diseccionar el flujo PKCE manualmente usando bash y curl para entender exactamente qué ocurre por debajo antes de depender de librerías mágicas.

Para complementar la integración de .NET de esta mañana, decidí hacer el flujo "a mano". Escribí un pequeño script en bash (`generate-pkce.sh`) para generar un `code_verifier` y derivar su `code_challenge` mediante SHA256. 

Con el challenge en mano, construí la URL de `/authorize` y me logué en el navegador. Azure me devolvió el `authorization_code`. Hasta aquí, sin problemas (ya había resuelto los temas del App Registration).

El siguiente paso fue armar el POST hacia el endpoint de token (`exchange-token.sh`). Pasé mi tenant, el client_id, el redirect_uri y, lo más importante, inyecté el `authorization_code` junto al `code_verifier` en texto plano. Azure me respondió con un bonito JSON conteniendo el `access_token` (JWT).

Para rizar el rizo, en vez de usar .NET, probé a validar ese JWT con un pequeño script suelto en Node (`validateToken.js`), apuntando explícitamente al endpoint JWKS (`/discovery/v2.0/keys`) para bajar las claves públicas de Microsoft. Comprobé que al alterar un solo carácter del token, la validación de la firma RS256 fallaba inmediatamente.

Laboratorio completado con éxito. Ver los engranajes criptográficos por dentro ayuda muchísimo a entender los posibles vectores de ataque.
