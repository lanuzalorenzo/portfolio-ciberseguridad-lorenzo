# 🔐 Ejercicio 03 — Self-Service Password Reset (SSPR)

Implementación completa de Self-Service Password Reset (SSPR) en Microsoft Entra ID dentro del laboratorio de identidad.  
Este ejercicio valida que los usuarios pueden restablecer su contraseña de forma autónoma mediante los métodos de recuperación configurados.

---

## 📐 Arquitectura del caso práctico
Para este ejercicio se define un escenario realista dentro del tenant:

- **Usuario de pruebas:** `test@lanuzalorenzooutlook.onmicrosoft.com`
- **Tipo de usuario:** nativo del tenant (compatible con MFA, SSPR y Passwordless)
- **Métodos de recuperación configurados:**
  - Email alternativo
  - Teléfono móvil
  - Microsoft Authenticator (si está registrado)
- **Alcance de SSPR:** habilitado para todos los usuarios del laboratorio
- **Objetivo:** validar que el usuario puede recuperar su contraseña sin intervención del administrador.

---

## 🛠 Trabajo realizado
- Habilitación de SSPR en Microsoft Entra ID.
- Configuración de métodos de recuperación permitidos.
- Registro previo de métodos por parte del usuario de pruebas.
- Validación del flujo completo de restablecimiento de contraseña.
- Documentación técnica del proceso y de las implicaciones de seguridad.

---

## 🔍 Validación del flujo
El usuario accede a la ruta oficial de recuperación de contraseña:

👉 https://aka.ms/sspr

Flujo validado:
1. Introducción del UPN.  
2. Selección del método de verificación.  
3. Recepción y validación del código.  
4. Restablecimiento de contraseña cumpliendo la política del tenant.  
5. Inicio de sesión correcto con la nueva credencial.

---

## 🧪 Caso práctico final
El flujo completo se ejecuta correctamente:

- El usuario puede iniciar el proceso sin intervención del administrador.  
- Los métodos configurados aparecen disponibles.  
- La contraseña se restablece de forma segura.  
- El inicio de sesión posterior confirma la validez del proceso.

Este caso práctico demuestra que SSPR está correctamente habilitado, configurado y funcional en el entorno del laboratorio.

---

## 📄 Documentación completa
La documentación técnica del ejercicio se encuentra en:

- `./docs/sspr-configuracion.md`  
- Bitácoras del módulo: `../../bitacora/`

---

## 🔐 Implicaciones de seguridad
SSPR reduce la carga operativa del administrador y mejora la resiliencia del tenant.  
Permite una recuperación segura y autónoma de credenciales, evitando bloqueos y aumentando la disponibilidad del entorno.
