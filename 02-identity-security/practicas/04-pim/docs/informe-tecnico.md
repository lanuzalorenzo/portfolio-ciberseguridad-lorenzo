# 📄 Informe técnico — PIM en Microsoft Entra ID

## 1. Introducción
Privileged Identity Management (PIM) permite gestionar roles privilegiados mediante asignaciones elegibles y activaciones temporales.

## 2. Configuración inicial
- Acceso al portal de Microsoft Entra ID.
- Navegación a **Identity Governance → Privileged Identity Management**.
- Selección de **Microsoft Entra roles → Assignments**.

## 3. Asignación elegible
- Rol seleccionado: **Lector global (Global Reader)**.
- Tipo de asignación: **Eligible**.
- Alcance: **Directory**.

## 4. Activación del rol
- Activación desde **My roles**.
- Requisitos:
  - MFA
  - Motivo
  - Duración limitada

## 5. Auditoría
- Registro de eventos en:
  - **Resource audit**
  - **My audit**

## 6. Conclusión técnica
PIM añade una capa crítica de seguridad al acceso privilegiado, permitiendo activaciones temporales y trazabilidad completa.
