# 🔐 02-identity-security

## 🧾 Descripción
Módulo dedicado a la seguridad de identidad en Azure Entra ID.  
Incluye la implementación de MFA, diseño y prueba de políticas de Conditional Access, auditoría de actividad y procedimientos de recuperación en un tenant de laboratorio.  
El objetivo es establecer una base sólida de control de acceso y protección de identidad aplicable a entornos reales.

---

## 🎯 Objetivos del módulo
- Implementar y validar MFA para cuentas de laboratorio.
- Diseñar y probar políticas de Conditional Access.
- Auditar inicios de sesión y actividad administrativa.
- Documentar playbooks de recuperación y rollback.
- Organizar evidencias y documentación técnica por áreas (MFA, CA, auditoría, recuperación).

---

## 🗂️ Estructura del módulo
- `bitacora/` — entradas técnicas y resúmenes del trabajo realizado.
- `mfa/` — guías, evidencias y configuraciones de MFA.
- `conditional-access/` — plantillas y pruebas de políticas.
- `auditoria/` — consultas, logs y análisis de actividad.
- `recovery/` — procedimientos y playbooks de rollback.
- `README.md` — documento principal del módulo.

---

## ⚙️ Requisitos
- Tenant de laboratorio en Azure Entra ID.
- Permisos administrativos adecuados (Global Administrator o equivalente).
- Herramientas recomendadas:
  - Azure Portal (entra.microsoft.com)
  - Microsoft Graph PowerShell
  - Azure CLI

---

## 🧪 Alcance del módulo
Este módulo se centra en:

- Protección de identidad mediante MFA y políticas de acceso.
- Control de acceso basado en condiciones (ubicación, dispositivo, riesgo, etc.).
- Visibilidad y trazabilidad de actividad administrativa y de inicio de sesión.
- Capacidad de recuperación ante configuraciones erróneas o bloqueos no deseados.

No se abordan aquí temas de seguridad de red, hardening de sistemas ni protección de datos.

---

## ✍️ Autor
Lorenzo Lanuza

---

## ⚖️ Aviso Legal
Este módulo contiene prácticas educativas y de laboratorio realizadas en un entorno controlado.  
No incluye información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas diseñadas exclusivamente para fines formativos.

---

## 📜 Licencia
MIT
