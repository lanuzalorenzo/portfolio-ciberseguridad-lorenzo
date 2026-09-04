# 🔐 02-identity-security

**Estado:** 🟡 WIP — en progreso (última actualización: 2026-09-04)

## 🧾 Descripción
Módulo dedicado a la **seguridad de identidad**: MFA, Conditional Access, auditoría de Entra ID y hardening del tenant. Contiene guías prácticas, evidencias y playbooks para pruebas en tenant de laboratorio.

## 🎯 Objetivos
- Implementar y validar MFA en el tenant de laboratorio.
- Diseñar y probar políticas básicas de Conditional Access.
- Auditar eventos de sign-in y cambios administrativos.
- Documentar procedimientos de recuperación y playbooks de rollback.

## 🗂️ Estructura
- `bitacora/` — entradas diarias y resúmenes.
- `mfa/` — guías, informes y evidencias de MFA.
- `conditional-access/` — plantillas de políticas y pruebas.
- `auditoria/` — consultas, logs y análisis.
- `README.md` — este fichero.

## ⚙️ Requisitos
- Cuenta administrativa en tenant de laboratorio.
- Permisos: **Global Administrator** o equivalente.
- Herramientas recomendadas: Azure Portal (`entra.microsoft.com`), Microsoft Graph PowerShell, Azure CLI.

## ✅ Checklist de cierre
- [ ] README final revisado y pulido
- [ ] Todas las bitácoras movidas y fechadas
- [ ] Scripts validados en tenant de laboratorio
- [ ] Playbook de rollback documentado
- [ ] Informe final y conclusiones

## ✍️ Autor
Lorenzo Lanuzalorenzo

## 📜 Licencia
MIT