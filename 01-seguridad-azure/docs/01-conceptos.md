# 🔐 Informe técnico — Conceptos del Módulo 01

## 📘 Proyecto
Módulo 01 — Seguridad en Azure (Autenticación, Autorización y Protección de APIs).

## 🎯 Objetivo
Definir y explicar los conceptos fundamentales necesarios para comprender el flujo de autenticación y autorización implementado en el módulo, incluyendo OAuth2, PKCE, JWT y Azure AD como proveedor de identidad.

## 🛠 Trabajo realizado
1. Revisión de los conceptos base de autenticación y autorización.
2. Identificación de los elementos principales del estándar OAuth2.
3. Análisis del rol de PKCE en clientes públicos.
4. Desglose de la estructura de un JWT.
5. Revisión del funcionamiento de JWKS y firma RS256.
6. Contextualización de Azure AD como proveedor de identidad.

## 🔍 Validaciones realizadas
- Confirmación de que los conceptos se alinean con el flujo implementado.
- Validación de que la terminología coincide con la usada por Azure AD.
- Revisión de que los conceptos son atemporales y no dependen del laboratorio.

## ⚠️ Problemas encontrados
- Ninguno. Este documento es conceptual.

## 🛠 Soluciones aplicadas
- No aplica.

## 🧠 Aprendizajes clave
- Importancia de PKCE para proteger el authorization_code.
- Relevancia de validar correctamente los JWT emitidos por Azure AD.
- Comprensión del uso de JWKS para verificar firmas RS256.
- Necesidad de validar issuer, audiencia y expiración en cada token.
- Relación entre OAuth2, PKCE y Azure AD en flujos modernos de autenticación.

## 📎 Recursos útiles
- https://learn.microsoft.com/azure/active-directory
- https://datatracker.ietf.org/doc/html/rfc7636
- https://jwt.io

## ⚖️ Aviso Legal
Este documento describe conceptos utilizados en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.

## 🔐 Licencia
Este documento se distribuye bajo licencia MIT.
Consulta el archivo LICENSE en la raíz del repositorio para más información.
