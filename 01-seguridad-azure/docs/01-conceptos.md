# Conceptos del módulo 01

🧾 Contexto
Este documento recoge los conceptos fundamentales utilizados en el módulo de Seguridad en Azure, donde se trabaja con autenticación, autorización y protección de APIs mediante Azure AD, OAuth2, PKCE y JWT.

🎯 Objetivo
Definir y explicar los conceptos clave necesarios para comprender el flujo de autenticación y autorización implementado en el módulo.

🛠 Trabajo realizado
- Revisión de los conceptos base de autenticación y autorización.
- Identificación de los elementos principales del estándar OAuth2.
- Análisis del rol de PKCE en clientes públicos.
- Desglose de la estructura de un JWT.
- Revisión del funcionamiento de JWKS y firma RS256.
- Contextualización de Azure AD como proveedor de identidad.

🔍 Validaciones realizadas
- Confirmación de que los conceptos se alinean con el flujo implementado.
- Validación de que la terminología coincide con la usada por Azure AD.
- Revisión de que los conceptos son atemporales y no dependen del laboratorio.

⚠️ Problemas encontrados
Ninguno. Este documento es conceptual.

🛠 Soluciones aplicadas
No aplica.

🔐 Implicaciones de seguridad
- Uso de PKCE para evitar interceptación del authorization_code.
- Uso de JWT firmados con RS256 para garantizar integridad.
- Dependencia de JWKS para validar firmas de tokens.
- Importancia de validar issuer, audiencia y expiración.

📎 Recursos útiles
- https://learn.microsoft.com/azure/active-directory
- https://datatracker.ietf.org/doc/html/rfc7636
- https://jwt.io/

⚙️ Comandos utilizados (opcional)
No aplica.

⚙️ Comandos pendientes de validar (opcional)
No aplica.

⚖️ Aviso Legal
Este documento describe conceptos utilizados en un entorno de laboratorio. No contiene información sensible ni perteneciente a ninguna organización real.