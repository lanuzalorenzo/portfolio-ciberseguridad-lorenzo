# 🔐 Informe técnico Entra ID MFA y Security Defaults

**Fecha:** 2026-09-04  
**Alcance:** Activación de **Security Defaults**, habilitación de **MFA por usuario**, registro de método **TOTP** (Proton Pass) y validación del flujo de autenticación.  
**Nota:** El documento describe **exactamente** las acciones realizadas en la consola web de Entra ID. Al final se incluyen **comandos de ejemplo** para automatizar las mismas operaciones; **no se usaron** en la práctica y están marcados como **pendientes de validar**.

---

## 🧾 Contexto y objetivo

**Contexto:** Tenant de pruebas en Microsoft Entra ID.  
**Objetivo del día:** aplicar una baseline mínima de seguridad activando **Security Defaults**, forzar el registro de MFA en un usuario de laboratorio y verificar que un método TOTP externo (Proton Pass) funciona correctamente en el flujo de autenticación interactivo.

---

## 🛠️ Acciones realizadas en la consola web (paso a paso, tal cual se hicieron)

### 🔎 1. Acceso al portal
- **Portal usado:** `https://entra.microsoft.com`  
- **Cuenta:** cuenta administrativa del tenant de laboratorio.  
- **Acción:** autenticación interactiva para acceder al portal de Entra.

---

### 📋 2. Auditoría visual previa
- **Ruta inspeccionada:** **Entra ID → Identity → Overview → Properties**  
  - **Comprobación:** estado de **Security Defaults** (antes de la acción: **Disabled**).  
- **Ruta inspeccionada:** **Entra ID → Identity → Users → Authentication Methods**  
  - **Comprobación:** existencia de métodos de autenticación registrados por usuarios (resultado: **ninguno** para el usuario de laboratorio).

---

### ✅ 3. Activación de Security Defaults
- **Ruta exacta seguida:** **Entra ID → Identity → Overview → Properties → Security Defaults**  
- **Acción realizada:** cambiar el control **Security Defaults** a **Enabled** y guardar.  
- **Efecto observado inmediatamente:** el portal muestra **Security Defaults: Enabled**.  
- **Implicaciones técnicas inmediatas:**  
  - **MFA obligatorio** para cuentas administrativas.  
  - **Bloqueo de autenticación heredada** (legacy auth) según la baseline.  
  - Aplicación de controles mínimos sin personalización granular.

---

### 🧭 4. Localización del panel clásico de MFA por usuario en la UI moderna
- **Ruta real encontrada:**  
  1. `entra.microsoft.com`  
  2. Menú lateral **Identidad**  
  3. **Usuarios**  
  4. Pestaña **Métodos de autenticación**  
  5. Tarjeta **Autenticación multifactor por usuario** → abrir (esto carga el panel clásico incrustado).  
- **Observación:** la opción **Enforce** no aparece en la UI moderna actual; la acción disponible es **Enable**.

---

### 🔔 5. Habilitación de MFA por usuario (panel clásico)
- **Acción realizada:** seleccionar el usuario de laboratorio en el panel clásico y pulsar **Enable / Habilitar MFA**.  
- **Resultado observado:** el usuario queda marcado como **Enabled**; con **Security Defaults** activo, el usuario deberá registrar un método MFA en el siguiente inicio de sesión.

---

### 📱 6. Registro del método TOTP con Proton Pass
- **Flujo de registro seguido por el usuario:**  
  1. Iniciar sesión con la cuenta habilitada para MFA.  
  2. En el flujo de registro seleccionar **Aplicación de autenticación**.  
  3. Escanear el QR mostrado con **Proton Pass**.  
  4. Introducir el código TOTP de verificación generado por Proton Pass.  
  5. Confirmación visual en la consola: método registrado y verificado.  
- **Resultado técnico:** Proton Pass genera TOTP conforme a **RFC 6238**; códigos de 6 dígitos y ventana temporal estándar, aceptados por Entra ID.

---

### 🔐 7. Validación del flujo de autenticación
- **Prueba realizada:** nuevo inicio de sesión interactivo con el usuario; en el prompt MFA introducir el código TOTP desde Proton Pass.  
- **Resultado:** inicio de sesión completado y acceso concedido. El evento de autenticación mostró MFA aplicado en la sesión interactiva.

---

## ⚙️ Comandos de ejemplo para reproducir (NO usados en la práctica — pendientes de validar)

> **Advertencia:** los comandos siguientes **no se ejecutaron** durante la práctica. Requieren permisos administrativos y scopes adecuados. Probar primero en un tenant de laboratorio y validar efectos antes de aplicar en producción.

**A. Microsoft Graph PowerShell — activar Security Defaults**
```powershell
Connect-MgGraph -Scopes "Policy.ReadWrite.Authorization"
Update-MgOrganization -SecurityDefaultsEnabled $true
Get-MgOrganization | Select-Object Id, SecurityDefaultsEnabled
```

**B. Azure CLI (az rest) — activar Security Defaults**
```bash
az login
az rest --method PATCH \
  --uri "https://graph.microsoft.com/v1.0/organization" \
  --headers "Content-Type=application/json" \
  --body '{"securityDefaultsEnabled": true}'
```

**C. MSOnline legacy — habilitar MFA por usuario**
```powershell
Connect-MsolService
Set-MsolUser -UserPrincipalName usuario@dominio.com -StrongAuthenticationRequirements @(@{RelyingParty="*";State="Enabled"})
Get-MsolUser -UserPrincipalName usuario@dominio.com | Select UserPrincipalName, StrongAuthenticationRequirements
```

**D. Microsoft Graph — listar métodos de autenticación del usuario**
```powershell
Connect-MgGraph -Scopes "User.Read.All","AuditLog.Read.All"
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users/usuario@dominio.com/authentication/methods"
```

**E. Microsoft Graph — consultar sign-in logs**
```powershell
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/auditLogs/signIns?$filter=userPrincipalName eq 'usuario@dominio.com'&$top=20"
```

---

## 🔍 Validaciones realizadas y comprobaciones recomendadas

- **Realizadas:**  
  - Comprobación visual de **Security Defaults** activo.  
  - Usuario marcado como **Enabled** para MFA.  
  - Registro y verificación TOTP con Proton Pass.  
  - Inicio de sesión con MFA validado.

- **Recomendadas y pendientes:**  
  - Revisar **Sign-in logs** en Entra ID para confirmar eventos MFA y detalles de `authenticationMethods`.  
  - Revisar **Audit logs** para registrar la activación de Security Defaults y la habilitación de MFA por usuario.  
  - Ejecutar los comandos de ejemplo en un tenant de laboratorio con dry-run y plan de rollback.  
  - Diseñar políticas de **Conditional Access** para reemplazar o complementar Security Defaults cuando se requiera granularidad.  
  - Documentar y probar procedimientos de recuperación para usuarios que pierdan acceso a su app TOTP.

---

## ⚠️ Observaciones de seguridad e implicaciones operativas

- **Security Defaults** es una **baseline rápida** pero **no** permite controles granulares; para requisitos empresariales migrar a **Conditional Access** y diseñar políticas por riesgo, aplicación y ubicación.  
- **TOTP externo (Proton Pass)** es compatible; en entornos corporativos valorar autenticadores gestionados (Microsoft Authenticator, FIDO2, passwordless) y definir procesos de recuperación y respaldo de métodos.  
- **Auditoría continua:** integrar logs en SIEM (por ejemplo, Azure Sentinel) y crear alertas para intentos de bypass, múltiples fallos MFA o cambios administrativos críticos.  
- **Procedimiento de recuperación:** definir y probar el proceso para usuarios que pierdan acceso a su app TOTP (registro de métodos alternativos, soporte y verificación de identidad).

---

✅ **Estado final:** Security Defaults activado, MFA por usuario habilitado, método TOTP con Proton Pass registrado y validado. El tenant queda preparado para avanzar a **Conditional Access** y a políticas de identidad más granulares.