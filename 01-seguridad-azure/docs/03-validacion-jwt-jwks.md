# 🔐 Informe técnico — Validación JWT y JWKS

## 📘 Proyecto
Módulo 01 — Seguridad en Azure (Autenticación, Autorización y Protección de APIs).

## 🎯 Objetivo
Documentar cómo se valida un token JWT emitido por Azure AD utilizando JWKS y firma RS256, asegurando que la API comprueba la autenticidad y validez del token antes de permitir el acceso.

## 🛠 Trabajo realizado
1. Análisis de la estructura del JWT:
   - **Header**: algoritmo y tipo de token.
   - **Payload**: claims relevantes para la API.
   - **Signature**: firma RS256 generada por Azure AD.

2. Identificación de claims críticos:
   - `iss` (issuer)
   - `aud` (audience)
   - `exp` (expiración)
   - `nbf` / `iat`
   - `scp` / `roles`

3. Revisión del algoritmo **RS256** utilizado por Azure AD.

4. Documentación del endpoint **JWKS** y su función en la validación de firmas.

5. Explicación del proceso de validación en la API:
   - Obtención de claves públicas desde JWKS.
   - Selección de la clave correcta mediante `kid`.
   - Verificación de la firma RS256.
   - Validación de claims.
   - Rechazo de tokens inválidos o caducados.

6. Revisión de la rotación automática de claves y su impacto en la API.

## 🔍 Validaciones realizadas
- Validación correcta de issuer, audiencia, expiración y firma.
- Confirmación de que la API utiliza JWKS para verificar la firma RS256.
- Revisión de que el documento es conceptual y atemporal.
- Verificación de que la API maneja la rotación de claves sin errores.

## ⚠️ Problemas encontrados
Ninguno. Documento conceptual.

## 🛠 Soluciones aplicadas
No aplica.

## 🧠 Aprendizajes clave
- Validar claims es tan importante como validar la firma.
- JWKS garantiza que la API utiliza claves públicas oficiales.
- La rotación automática de claves exige consultar JWKS periódicamente.
- Tokens sin firma válida deben ser rechazados inmediatamente.
- La API debe validar siempre issuer, audiencia y expiración.

## 📎 Recursos útiles
- https://learn.microsoft.com/azure/active-directory/develop
- https://jwt.io
- https://datatracker.ietf.org/doc/html/rfc7517

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.  
No contiene información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.

## 🔐 Licencia
Este documento se distribuye bajo licencia MIT.  
Consulta el archivo LICENSE en la raíz del repositorio para más información.
