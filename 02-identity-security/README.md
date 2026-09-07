# 🔐 02 — Identity Security en Azure Entra ID

Este módulo recoge el trabajo práctico dedicado a la **seguridad de identidad en Azure Entra ID**, incluyendo la implementación de **MFA**, el diseño y prueba de **Conditional Access**, la **auditoría de actividad** y los procedimientos de **recuperación** en un tenant de laboratorio.

El objetivo es establecer una base sólida de control de acceso y protección de identidad aplicable a entornos reales, documentada de forma técnica, clara y atemporal.

---

## 🧭 Objetivos del módulo

- Implementar y validar **MFA** para cuentas de laboratorio.  
- Diseñar y probar políticas de **Conditional Access**.  
- Auditar inicios de sesión y actividad administrativa.  
- Documentar **playbooks de recuperación** y rollback.  
- Organizar evidencias y documentación técnica por áreas (MFA, CA, auditoría, recuperación).

---

## 🧩 Áreas del módulo

Este módulo se estructura en cuatro áreas principales, cada una con su documentación y evidencias:

### **1. MFA (Multi-Factor Authentication)**  
- Configuración de MFA en Entra ID.  
- Métodos de autenticación.  
- Pruebas de acceso y bloqueo.  
- Documentación técnica y evidencias.

### **2. Conditional Access**  
- Diseño de políticas basadas en condiciones.  
- Ubicación, riesgo, dispositivo, aplicación, sesión.  
- Pruebas controladas en tenant de laboratorio.  
- Plantillas y resultados de las pruebas.

### **3. Auditoría de Identidad**  
- Revisión de inicios de sesión.  
- Análisis de actividad administrativa.  
- Consultas y logs relevantes.  
- Evidencias y análisis técnico.

### **4. Recovery / Rollback**  
- Procedimientos de recuperación ante bloqueos.  
- Playbooks para revertir configuraciones.  
- Buenas prácticas de seguridad y control.

---

## 🗂️ Estructura del módulo

Este módulo contiene:

- `bitacora/` — entradas técnicas y resúmenes del trabajo realizado.  
- `mfa/` — documentación y evidencias de MFA.  
- `conditional-access/` — pruebas y plantillas de políticas CA.  
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
- Control de acceso basado en condiciones.  
- Visibilidad y trazabilidad de actividad administrativa.  
- Capacidad de recuperación ante configuraciones erróneas.

No se abordan aquí temas de seguridad de red, hardening de sistemas ni protección de datos.

---

## ⚖️ Aviso Legal

Este módulo contiene prácticas educativas y de laboratorio realizadas en un entorno controlado.  
No incluye información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas diseñadas exclusivamente para fines formativos.

---

## 📜 Licencia

MIT
