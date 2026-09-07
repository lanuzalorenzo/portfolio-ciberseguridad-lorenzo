# 📄 Bitácora — MFA en Microsoft Entra ID

## 📘 Proyecto
Portfolio de Ciberseguridad — Módulo 02: Identity Security

## 🎯 Objetivo
Habilitar y validar MFA en el tenant de laboratorio de Microsoft Entra ID, localizar el panel real de configuración, registrar un método TOTP externo y comprobar el flujo completo de autenticación.

---

## 🛠 Trabajo realizado

### 1. Activación de Security Defaults
- Activación de Security Defaults desde la interfaz moderna de Entra.
- MFA pasa a ser obligatorio para administradores y usuarios en riesgo.
- El control aparece como lista desplegable (Enabled/Disabled).

### 2. Localización del panel real de MFA por usuario
- Identificación del panel clásico de MFA dentro de la UI moderna.
- Ruta efectiva:
  - Identidad → Usuarios  
  - Pestañas superiores → Métodos de autenticación  
  - Tarjeta → Autenticación multifactor por usuario
- El panel clásico aparece incrustado en la interfaz moderna.

### 3. Habilitación de MFA por usuario
- Selección del usuario en el panel clásico.
- Activación de “Habilitar MFA”.
- La opción “Enforce” ya no existe en la UI moderna.
- Con Security Defaults habilitado, el usuario debe registrar MFA en el siguiente inicio de sesión.

### 4. Registro del método TOTP externo (Proton Pass)
- Inicio de sesión del usuario para completar el registro MFA.
- Selección de “Aplicación de autenticación”.
- Escaneo del código QR con Proton Pass.
- Verificación del código TOTP.
- Confirmación de funcionamiento correcto del método TOTP.

### 5. Validación del flujo MFA
- Prueba de inicio de sesión con MFA activo.
- Introducción del código TOTP generado por Proton Pass.
- Autenticación completada correctamente.

---

## 🔍 Validaciones realizadas
- Security Defaults activado y funcional.
- Panel de MFA localizado correctamente en la UI moderna.
- MFA habilitado para el usuario del laboratorio.
- Método TOTP externo registrado y operativo.
- Flujo de autenticación validado de extremo a extremo.

---

## ⚠️ Problemas encontrados
- La ruta hacia el panel clásico de MFA está más oculta que en la documentación oficial.
- La desaparición de “Enforce” puede generar confusión en documentación antigua.

---

## 🛠 Soluciones aplicadas
- Documentación de la ruta real hacia el panel de MFA.
- Ajuste del procedimiento para la nueva interfaz moderna.
- Validación del comportamiento de Security Defaults como reemplazo de “Enforce”.

---

## 🧠 Aprendizajes clave
- Security Defaults simplifica MFA pero limita personalización avanzada.
- Proton Pass funciona perfectamente como método TOTP para Entra ID.
- La UI moderna de Entra integra paneles clásicos de forma no evidente.
- La autenticación multifactor es obligatoria en escenarios de riesgo.

---

## 📎 Recursos útiles
- Documentación oficial de Microsoft Entra ID  
- Guía de MFA  
- Proton Pass (TOTP)  
- Conceptos básicos de identidad en Azure
