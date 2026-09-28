# 🔐 Informe técnico — Flujo OAuth2 PKCE

## 📘 Proyecto
Módulo 01 — Seguridad en Azure (Autenticación, Autorización y Protección de APIs).

## 🎯 Objetivo
Documentar el flujo OAuth2 Authorization Code con PKCE utilizado para obtener tokens emitidos por Azure AD y validar el acceso a una API protegida. El documento debe ser técnico, claro y atemporal.

## 🛠 Trabajo realizado
1. Desglose del rol del `code_verifier`.
2. Explicación del `code_challenge` y su derivación mediante SHA256.
3. Descripción del Authorization Request enviado a Azure AD.
4. Revisión del proceso de autenticación del usuario.
5. Análisis del `authorization_code` emitido por Azure AD.
6. Documentación del intercambio del código por tokens.
7. Explicación del token de acceso (JWT) emitido por Azure AD.
8. Revisión de la validación del token en la API.

## 🔍 Validaciones realizadas
- Confirmación de que el flujo descrito coincide con el implementado en el módulo.
- Validación de que los pasos siguen el estándar OAuth2 + PKCE.
- Revisión de que no se incluyen rutas de UI ni comandos operativos.

## ⚠️ Problemas encontrados
Ninguno. El documento es conceptual.

## 🛠 Soluciones aplicadas
No aplica.

## 🧠 Aprendizajes clave
- PKCE protege el `authorization_code` frente a ataques de interceptación.
- El uso de HTTPS es obligatorio para garantizar la seguridad del flujo.
- El token de acceso debe validarse siempre en la API.
- La API debe rechazar tokens sin firma válida o con claims incorrectos.
- La validación correcta del JWT es esencial para evitar accesos indebidos.

## 📎 Recursos útiles
- https://datatracker.ietf.org/doc/html/rfc7636  
- https://learn.microsoft.com/azure/active-directory/develop  

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.  
No contiene información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.

## 🔐 Licencia
Este documento se distribuye bajo licencia MIT.  
Consulta el archivo LICENSE en la raíz del repositorio para más información.
