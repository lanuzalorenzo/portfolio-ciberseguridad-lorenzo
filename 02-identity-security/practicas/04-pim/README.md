# 🔐 Práctica 04 — Privileged Identity Management (PIM)

## 🎯 Objetivo
Configurar y validar el uso de Privileged Identity Management (PIM) para gestionar roles privilegiados de forma temporal y controlada en Microsoft Entra ID.

## 🧭 Contexto
Esta práctica forma parte del módulo 02 — Identity Security.  
El objetivo es demostrar el uso de asignaciones elegibles, activación temporal de roles y buenas prácticas de privilegios mínimos.

## 🛠 Procedimiento
1. Acceder al portal de Microsoft Entra ID.
2. Navegar a **Identity Governance → Privileged Identity Management**.
3. Entrar en **Microsoft Entra roles → Assignments**.
4. Crear una asignación elegible para el rol **Lector global (Global Reader)**.
5. Activar el rol desde **My roles** proporcionando:
   - motivo de activación  
   - duración  
   - verificación MFA  
6. Validar que el rol aparece como **Active** durante el periodo configurado.
7. Desactivar el rol manualmente desde **My roles**.
8. Confirmar que vuelve al estado **Eligible**.

## 🔍 Validaciones
- El rol aparece en la sección **Eligible assignments**.
- La activación temporal requiere MFA.
- El rol pasa a estado **Active** durante la ventana de uso.
- La desactivación devuelve el rol al estado **Eligible**.
- Se registran eventos en **Resource audit** y **My audit**.

## 🧩 Conclusiones
PIM permite aplicar privilegios mínimos y control temporal sobre roles sensibles.  
La activación bajo demanda, junto con MFA y auditoría, reduce el riesgo de exposición de permisos permanentes.

## ⚖️ Aviso Legal
Práctica realizada en un entorno de laboratorio sin datos reales.
