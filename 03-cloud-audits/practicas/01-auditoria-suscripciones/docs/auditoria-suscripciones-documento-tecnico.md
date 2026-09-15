# 🔐 Informe técnico — Auditoría de suscripciones

## 📘 Proyecto  
Auditoría de suscripción cloud de laboratorio.  
Se requiere revisar configuración, permisos, roles, recursos críticos y políticas de seguridad.

---

## 🎯 Objetivo  
Evaluar el estado de seguridad de la suscripción, identificar configuraciones inseguras, revisar accesos críticos y documentar hallazgos de forma técnica y atemporal.

---

## 🛠 Trabajo realizado

1. **Revisión de configuración general de la suscripción**  
   - Análisis de propiedades globales.  
   - Identificación de configuraciones por defecto y parámetros críticos.

2. **Análisis de roles y permisos asignados**  
   - Revisión de roles RBAC.  
   - Identificación de asignaciones con privilegios elevados.  
   - Validación de accesos heredados.

3. **Identificación de accesos privilegiados**  
   - Detección de cuentas con permisos administrativos.  
   - Revisión de grupos con roles críticos.

4. **Evaluación de recursos críticos**  
   - Análisis de recursos sensibles (almacenamiento, claves, identidades, redes).  
   - Revisión de configuraciones de seguridad aplicadas.

5. **Detección de configuraciones inseguras**  
   - Identificación de parámetros débiles o no recomendados.  
   - Revisión de políticas aplicadas y su cumplimiento.

6. **Documentación de hallazgos**  
   - Registro técnico de cada hallazgo.  
   - Clasificación por criticidad.  
   - Propuesta de mejoras.

---

## 🔍 Validaciones realizadas  
- Roles y permisos revisados.  
- Accesos privilegiados identificados.  
- Recursos críticos evaluados.  
- Configuraciones inseguras detectadas.  
- Hallazgos documentados correctamente.

---

## ⚠️ Problemas encontrados  
- Roles con privilegios excesivos.  
- Recursos sin configuraciones de seguridad recomendadas.  
- Falta de políticas de cumplimiento en algunos servicios.

---

## 🛠 Soluciones aplicadas  
- Recomendación de ajuste de roles.  
- Propuesta de endurecimiento de recursos críticos.  
- Sugerencia de aplicación de políticas de seguridad.

---

## 🧠 Aprendizajes clave  
- Importancia de revisar roles heredados.  
- Necesidad de aplicar políticas de seguridad consistentes.  
- Riesgos asociados a configuraciones por defecto.

---

## 📎 Recursos útiles  
- Documentación oficial del proveedor cloud.  
- Guías de buenas prácticas de seguridad.  
- Referencias de auditoría cloud.

---

## ⚙️ Comandos utilizados  
N/A — Auditoría realizada desde consola y paneles de administración.

---

## ⚖️ Aviso Legal  
Este documento describe prácticas realizadas en un entorno de laboratorio.  
No contiene información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
