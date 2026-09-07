# Validación JWT y JWKS

🧾 Contexto
Este documento explica cómo se valida un token JWT emitido por Azure AD utilizando JWKS y firma RS256 dentro del módulo de Seguridad en Azure.

🎯 Objetivo
Describir de forma técnica y atemporal el proceso de validación de tokens JWT y el uso de JWKS para verificar firmas.

🛠 Trabajo realizado
- Desglose de la estructura del JWT (header, payload, signature).
- Identificación de claims relevantes para la API.
- Revisión del algoritmo RS256 utilizado por Azure AD.
- Documentación del endpoint JWKS y su función.
- Explicación del proceso de validación en la API.
- Revisión de la rotación automática de claves.

🔍 Validaciones realizadas
- Confirmación de que la API valida correctamente issuer, audiencia y expiración.
- Validación de que la firma RS256 se comprueba mediante JWKS.
- Revisión de que el documento no incluye procedimientos operativos.

⚠️ Problemas encontrados
Ninguno. Documento conceptual.

🛠 Soluciones aplicadas
No aplica.

🔐 Implicaciones de seguridad
- Validación estricta de claims evita accesos indebidos.
- Uso de JWKS garantiza que la API utiliza claves públicas oficiales.
- La rotación automática de claves requiere que la API consulte JWKS periódicamente.
- Tokens sin firma válida deben ser rechazados inmediatamente.

📎 Recursos útiles
- https://learn.microsoft.com/azure/active-directory/develop/
- https://jwt.io/
- https://datatracker.ietf.org/doc/html/rfc7517

⚙️ Comandos utilizados (opcional)
No aplica.

⚙️ Comandos pendientes de validar (opcional)
No aplica.

⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio. No contiene información sensible ni perteneciente a ninguna organización real.
