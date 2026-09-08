# 🔐 Informe técnico — Configuración de SSPR en Microsoft Entra ID

## 📐 Arquitectura del caso práctico
Para validar SSPR en un entorno realista dentro del laboratorio de identidad, se define el siguiente escenario:

- **Usuario de pruebas:** `test@lanuzalorenzooutlook.onmicrosoft.com`
- **Tipo de usuario:** nativo del tenant (ideal para MFA, SSPR y Passwordless)
- **Métodos de recuperación configurados:**
  - Email alternativo
  - Teléfono móvil
  - Microsoft Authenticator (si está registrado)
- **Alcance de SSPR:** habilitado para todos los usuarios del laboratorio
- **Objetivo del caso práctico:** demostrar que el usuario puede recuperar su contraseña sin intervención del administrador y validar el flujo completo de restablecimiento.

---

## 🧾 Contexto
Laboratorio de identidad en Microsoft Entra ID.  
Se requiere habilitar Self-Service Password Reset (SSPR) y validar el flujo completo de recuperación de contraseña para un usuario de pruebas.

---

## 🎯 Objetivo
Configurar SSPR, habilitar métodos de recuperación y verificar que un usuario puede restablecer su contraseña sin intervención del administrador.

---

## 🛠 Trabajo realizado

### Habilitación de SSPR en el tenant
**Ruta:** Identidad → Métodos de autenticación → Self-Service Password Reset  
**Enabled:** Selected  
**Target:** All users (laboratorio)

### Configuración de métodos de recuperación
Métodos habilitados:
- Email alternativo  
- Teléfono móvil  
- Microsoft Authenticator (si ya está registrado)

### Asignación del usuario de pruebas
- **Usuario:** `test@lanuzalorenzooutlook.onmicrosoft.com`
- **Motivo:** usuario nativo compatible con MFA, SSPR y Passwordless.

---

## 🔍 Validación del flujo SSPR
**Ruta:** https://aka.ms/sspr

**Flujo seguido:**
1. Introducción del UPN  
2. Selección del método de verificación  
3. Recepción del código  
4. Restablecimiento de contraseña  

**Resultado:** contraseña restablecida correctamente.

---

## 🧪 Caso práctico final — Validación completa de SSPR

### 1. Inicio del flujo
El usuario accede a la ruta oficial de recuperación de contraseña:  
https://aka.ms/sspr

Introduce su UPN y selecciona “No recuerdo mi contraseña”.

### 2. Selección del método de verificación
El sistema muestra los métodos previamente registrados:
- Email alternativo  
- Teléfono móvil  
- Microsoft Authenticator  

El usuario selecciona uno de ellos y recibe el código de verificación.

### 3. Restablecimiento de contraseña
Tras validar el código, el usuario introduce una nueva contraseña cumpliendo los requisitos del tenant.

**Resultado:**
- Contraseña actualizada correctamente  
- El usuario puede iniciar sesión con la nueva credencial  
- El flujo completo funciona sin intervención del administrador

### 4. Conclusión
El ejercicio demuestra que SSPR está correctamente habilitado, configurado y funcional en el entorno del laboratorio.  
La recuperación de contraseña es segura, autónoma y reduce la carga operativa del administrador.

---

## ⚠️ Problemas encontrados
- Algunos métodos no aparecen si el usuario no los registró previamente.  
- La UI moderna oculta rutas antiguas documentadas en guías previas.

---

## 🛠 Soluciones aplicadas
- Registro previo de métodos en My Sign-Ins.  
- Documentación de rutas reales en la interfaz moderna.  
- Validación del flujo completo con usuario nativo.

---

## 🔐 Implicaciones de seguridad
SSPR reduce la carga del administrador y mejora la resiliencia del tenant.  
Permite recuperación segura sin intervención manual y evita bloqueos operativos.
