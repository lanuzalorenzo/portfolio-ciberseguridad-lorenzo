# Flujo OAuth2 PKCE

🧾 Contexto
Este documento describe el flujo OAuth2 Authorization Code con PKCE utilizado en el módulo para obtener tokens de acceso emitidos por Azure AD y proteger una API en .NET.

🎯 Objetivo
Documentar el flujo completo de OAuth2 PKCE de forma técnica, clara y atemporal, sin incluir procedimientos operativos.

🛠 Trabajo realizado
- Desglose del rol del code_verifier.
- Explicación del code_challenge y su derivación mediante SHA256.
- Descripción del Authorization Request enviado a Azure AD.
- Revisión del proceso de autenticación del usuario.
- Análisis del authorization_code emitido por Azure AD.
- Documentación del intercambio de código por tokens.
- Explicación del token de acceso emitido (JWT).
- Revisión de la validación del token en la API.

🔍 Validaciones realizadas
- Confirmación de que el flujo descrito coincide con el implementado en el módulo.
- Validación de que los pasos siguen el estándar OAuth2 + PKCE.
- Revisión de que no se incluyen rutas de UI ni comandos.

⚠️ Problemas encontrados
Ninguno. El documento es conceptual.

🛠 Soluciones aplicadas
No aplica.

🔐 Implicaciones de seguridad
- PKCE evita ataques de interceptación del authorization_code.
- El uso de HTTPS es obligatorio para proteger el flujo.
- El token de acceso debe validarse siempre en la API.
- La API debe rechazar tokens sin firma válida o con claims incorrectos.

📎 Recursos útiles
- https://datatracker.ietf.org/doc/html/rfc7636
- https://learn.microsoft.com/azure/active-directory/develop/

⚙️ Comandos utilizados (opcional)
No aplica.

⚙️ Comandos pendientes de validar (opcional)
No aplica.

⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio. No contiene información sensible ni perteneciente a ninguna organización real.
