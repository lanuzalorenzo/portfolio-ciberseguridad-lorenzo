# 🔐 Informe técnico — Configuración de MFA en Microsoft Entra ID

## 🧾 Contexto
Tenant de laboratorio en Microsoft Entra ID.  
Se requiere habilitar MFA, registrar un método TOTP externo y validar el flujo completo de autenticación.

---

## 🎯 Objetivo
Aplicar una configuración mínima de seguridad basada en Security Defaults, habilitar MFA para un usuario de laboratorio y verificar el funcionamiento de un método TOTP externo (Proton Pass).

---

## 🛠 Trabajo realizado

### 1. Activación de Security Defaults
- Acceso al portal: https://entra.microsoft.com  
- Ruta: Identidad → Overview → Properties  
- Acción: activar **Security Defaults**.  
- Efectos:
  - MFA obligatorio para administradores.  
  - Bloqueo de autenticación heredada.  
  - Baseline mínima sin granularidad avanzada.

### 2. Localización del panel clásico de MFA
- Ruta real en la UI moderna:
  - Identidad → Usuarios  
  - Métodos de autenticación  
  - Tarjeta: **Autenticación multifactor por usuario**  
- Observación: la opción clásica **Enforce** ya no aparece; solo **Enable**.

### 3. Habilitación de MFA por usuario
- Selección del usuario en el panel clásico.  
- Acción: **Enable MFA**.  
- Resultado: el usuario debe registrar MFA en el siguiente inicio de sesión.

### 4. Registro del método TOTP externo (Proton Pass)
- Flujo seguido:
  - Inicio de sesión del usuario.  
  - Selección de “Aplicación de autenticación”.  
  - Escaneo del QR con Proton Pass.  
  - Introducción del código TOTP.  
- Resultado: método registrado y verificado correctamente.

### 5. Validación del flujo MFA
- Inicio de sesión con MFA habilitado.  
- Introducción del código TOTP desde Proton Pass.  
- Resultado: autenticación completada y MFA aplicado.

---

## 🔍 Validaciones realizadas
- Security Defaults activo.  
- Usuario marcado como **Enabled** para MFA.  
- Método TOTP registrado y funcional.  
- Flujo de autenticación validado de extremo a extremo.

---

## ⚠️ Problemas encontrados
- El panel clásico de MFA está oculto dentro de la UI moderna.  
- Documentación oficial aún referencia opciones que ya no existen (como **Enforce**).

---

## 🛠 Soluciones aplicadas
- Documentación de la ruta real hacia el panel clásico.  
- Ajuste del procedimiento para la interfaz moderna.  
- Validación del comportamiento de Security Defaults como reemplazo de Enforce.

---

## 🔐 Implicaciones de seguridad
- Security Defaults es adecuado para laboratorios y entornos pequeños
