# 🔐 Ejercicio 02 — Passwordless Authentication

Implementación de autenticación sin contraseña en Microsoft Entra ID mediante:
- Microsoft Authenticator (passwordless)
- Passkey / FIDO2
- Windows Hello for Business
- Usuario nativo del tenant

Este ejercicio valida que un usuario puede autenticarse sin contraseña utilizando métodos modernos y seguros.

---

## 📐 Arquitectura del caso práctico
- **Usuario de pruebas:** `test@lanuzalorenzooutlook.onmicrosoft.com`
- **Métodos configurados:**
  - Microsoft Authenticator (passwordless)
  - Passkey / FIDO2
  - Windows Hello for Business
- **Entorno:** laboratorio del módulo 02 — Identity Security
- **Objetivo:** habilitar y validar autenticación sin contraseña en el tenant.

---

## 🛠 Trabajo realizado
- Habilitación de métodos passwordless en Microsoft Entra ID.
- Registro del usuario en Microsoft Authenticator.
- Configuración de Passkey / FIDO2.
- Activación de Windows Hello for Business.
- Validación del inicio de sesión sin contraseña.

---

## 🔍 Validaciones
- El usuario puede iniciar sesión con Microsoft Authenticator sin contraseña.
- El dispositivo registra correctamente la Passkey / FIDO2.
- Windows Hello for Business permite autenticación biométrica.
- El flujo completo funciona sin credenciales tradicionales.

---

## 🧪 Caso práctico final
El usuario inicia sesión sin contraseña utilizando:
- Microsoft Authenticator (notificación + número)
- Passkey / FIDO2
- Windows Hello for Business

Resultado:
- Autenticación exitosa sin uso de contraseña.
- Reducción del riesgo asociado a credenciales tradicionales.
- Flujo passwordless completamente funcional.

---

## 📄 Documentación completa
- `./docs/passwordless-configuracion.md`
- Bitácoras del módulo: `../../bitacora/`

---

## 🔐 Implicaciones de seguridad
La autenticación sin contraseña:
- Reduce el riesgo de phishing.
- Elimina la dependencia de contraseñas débiles.
- Mejora la experiencia del usuario.
- Aumenta la seguridad del tenant mediante MFA implícito.
