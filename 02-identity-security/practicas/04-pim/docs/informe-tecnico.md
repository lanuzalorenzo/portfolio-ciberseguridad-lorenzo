# 🔐 Informe técnico — Privileged Identity Management (PIM)

## 🧾 Contexto
Práctica realizada dentro del laboratorio del módulo **02 — Identity Security**, enfocada en la gestión de roles privilegiados mediante activaciones temporales en Microsoft Entra ID.

---

## 🎯 Objetivo
Configurar y validar el uso de **Privileged Identity Management (PIM)** para:
- Asignar roles como *Eligible*.
- Activar roles de forma temporal.
- Aplicar controles de seguridad como MFA y justificación.
- Verificar auditoría y trazabilidad.

---

## 🛠 Trabajo realizado

### 1. Acceso a PIM
Ruta utilizada:
**Identity Governance → Privileged Identity Management → Microsoft Entra roles**

### 2. Revisión de roles asignados
- Verificación de roles existentes.
- Confirmación de que el usuario de pruebas tiene asignación *Eligible*.

### 3. Activación del rol
Acciones realizadas:
- Navegar a **My roles**.
- Seleccionar el rol **Global Reader**.
- Activar el rol proporcionando:
  - Justificación.
  - Duración.
  - Verificación MFA.

### 4. Validación de estado
- Confirmación de que el rol pasa a estado **Active**.
- Verificación de permisos disponibles durante la activación.

### 5. Desactivación del rol
- Desactivación manual desde **My roles**.
- Confirmación de retorno al estado **Eligible**.

---

## 🔍 Validaciones realizadas
- El rol aparece correctamente como **Eligible** antes de la activación.
- La activación requiere MFA.
- La activación exige justificación.
- El rol queda en estado **Active** durante el tiempo configurado.
- La auditoría registra:
  - Activación.
  - Desactivación.
  - Justificación.
  - Duración.

---

## ⚠️ Problemas encontrados
- La interfaz moderna oculta algunas rutas clásicas documentadas en guías antiguas.
- El usuario debe tener métodos MFA configurados para activar roles.

---

## 🛠 Soluciones aplicadas
- Documentación de rutas reales de la UI moderna.
- Registro previo de métodos MFA en **My Sign-Ins**.
- Validación del flujo completo con usuario nativo del tenant.

---

## 🔐 Implicaciones de seguridad
- PIM reduce el riesgo de permisos permanentes.
- Obliga a usar MFA para roles sensibles.
- Aporta trazabilidad completa mediante auditoría.
- Permite aplicar el principio de privilegios mínimos.

---

## 📎 Recursos útiles
- https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-configure
- https://learn.microsoft.com/entra/identity/

---

## ⚙️ Comandos utilizados (opcional)
_No se utilizaron comandos en esta práctica._

---

## ⚙️ Comandos pendientes de validar (opcional)
_No aplica._

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.  
No contiene información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
