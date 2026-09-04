# Bitácora del Bloque: MFA en Microsoft Entra ID  
**Fecha:** 2026-09-04  
**Proyecto:** Portfolio Ciberseguridad – Lorenzo  
**Bloque:** 01-seguridad-azure / MFA  
**Estado:** ✅ COMPLETADO

---

## Objetivo del Bloque
Habilitar MFA en el tenant de pruebas de Microsoft Entra ID, documentar la ruta real hacia el panel de configuración, registrar un método TOTP externo (Proton Pass) y validar el flujo de autenticación.  
Se trabaja íntegramente en la interfaz moderna de **entra.microsoft.com**.

---

## Acciones Realizadas

### 1. Activación de Security Defaults
**Acción:** Activar Security Defaults desde la interfaz moderna.  
**Ruta:** *Microsoft Entra ID → Identity → Overview → Properties → Security Defaults*.  
**Detalle:**  
- El control aparece como **dropdown list** (Enabled/Disabled).  
- Se selecciona **Enabled**.  
- MFA pasa a ser obligatorio para administradores y usuarios en riesgo.  
**Fecha:** 2026-09-04  
**Estado:** ✅ Completado

---

### 2. Ubicación real del panel de MFA por usuario
**Acción:** Localizar el panel clásico de MFA dentro de la UI moderna.  
**Ruta correcta:**  
1. entra.microsoft.com  
2. Identidad  
3. Usuarios  
4. Pestañas superiores → **Métodos de autenticación**  
5. Tarjeta → **Autenticación multifactor por usuario**  
**Detalle:**  
- La opción está más escondida que en la documentación oficial.  
- La tarjeta abre el panel clásico incrustado en Entra.  
**Estado:** ✅ Completado

---

### 3. Habilitación de MFA por usuario
**Acción:** Habilitar MFA para el usuario del lab.  
**Detalle:**  
- Se selecciona el usuario en el panel clásico.  
- Se aplica **Habilitar MFA**.  
- La opción **Enforce** ya no existe en la UI moderna.  
- Con Security Defaults + Enable, el usuario queda obligado a registrar MFA en el siguiente inicio de sesión.  
**Estado:** ✅ Completado

---

### 4. Registro del método MFA (Proton Pass)
**Acción:** Registrar un método TOTP externo.  
**Detalle:**  
- Inicio de sesión del usuario para completar MFA.  
- Selección de **Aplicación de autenticación**.  
- Escaneo del QR con **Proton Pass**.  
- Verificación del código TOTP.  
- Confirmación de que Proton Pass funciona correctamente con Entra ID.  
**Estado:** ✅ Completado

---

### 5. Validación del flujo MFA
**Acción:** Probar inicio de sesión con MFA activo.  
**Detalle:**  
- El usuario introduce el código TOTP generado por Proton Pass.  
- Autenticación completada correctamente.  
**Estado:** ✅ Completado

---

## Commits Recomendados

```bash
# Commit 1: Activación de Security Defaults
git add .
git commit -m "feat(security): activar Security Defaults en Entra ID"

# Commit 2: Documentación de MFA
git add 01-seguridad-azure/bitacora/2026-09-04-mfa-entra-id.md
git commit -m "docs(bitacora): añadir bitácora de configuración MFA en Entra ID"

# Commit 3: Ajustes del bloque de seguridad
git add .
git commit -m "chore(security): documentar ruta real de MFA y registro TOTP externo"
```

---

## Estado Actual del Bloque
✅ Security Defaults activado  
✅ MFA habilitado por usuario  
✅ Método TOTP configurado (Proton Pass)  
✅ Flujo de autenticación validado  
⚙️ Preparado para políticas de acceso condicional (CA)

---

## Pendiente (Próximas Fases)
- Implementar políticas de acceso condicional (CA).  
- Bloqueo de acceso sin MFA.  
- Requerir MFA por riesgo o ubicación.  
- Integración con App Registrations.  
- Auditoría y logs de seguridad.  

---

## Checklist de Finalización
- [x] Security Defaults activado  
- [x] MFA habilitado  
- [x] Método TOTP registrado  
- [x] Validación de inicio de sesión  
- [x] Documentación en bitácora  
- [x] Commits preparados  

---

## Notas Importantes
- La opción **Enforce** ya no existe en la UI moderna de Entra ID.  
- Proton Pass funciona perfectamente como método TOTP para Entra ID.  
- La ruta hacia el panel de MFA está más oculta que en la documentación oficial.  
- Security Defaults simplifica MFA pero limita personalización avanzada.

---

## Recursos Útiles
- Microsoft Entra ID  
- Documentación de MFA  
- Proton Pass (TOTP)  
- Azure AD Identity Fundamentals  

---

## Cambios Recientes
**2026-09-04:** Activación de Security Defaults y configuración MFA → ✅  
**2026-09-04:** Registro de método TOTP externo → ✅  
**2026-09-04:** Validación del flujo MFA → ✅  

---

## Responsables
**Desarrollador:** Lorenzo  
**Proyecto:** Portfolio Ciberseguridad  
**Bloque MFA:** CERRADO ✅  
**Próxima fase:** Acceso Condicional (2026-09-05)
```

---
