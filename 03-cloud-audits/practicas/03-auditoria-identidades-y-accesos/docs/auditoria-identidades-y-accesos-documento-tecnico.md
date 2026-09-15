# 🔐 Informe técnico — Auditoría de identidades y accesos

## 📘 Contexto  
Suscripción cloud de laboratorio.  
El objetivo es auditar identidades, roles, permisos y accesos para detectar riesgos derivados de una mala gestión de privilegios.

---

## 🎯 Objetivo  
Evaluar el estado de seguridad de las identidades y accesos dentro de la suscripción, identificar permisos excesivos, cuentas huérfanas, configuraciones débiles y documentar hallazgos de forma técnica y atemporal.

---

## 🛠 Trabajo realizado

### 1. Inventario de identidades  
- Enumeración de usuarios, grupos y cuentas de servicio.  
- Clasificación por tipo de identidad y nivel de exposición.  
- Identificación de identidades inactivas o sin uso reciente.

### 2. Revisión de roles y permisos  
- Validación de roles asignados a cada identidad.  
- Análisis de permisos efectivos y privilegios heredados.  
- Detección de accesos excesivos o no justificados.

### 3. Auditoría de accesos privilegiados  
- Revisión de cuentas con roles administrativos.  
- Validación de accesos críticos a recursos sensibles.  
- Identificación de rutas de escalada de privilegios.

### 4. Evaluación de políticas de acceso  
- Revisión de políticas de autenticación.  
- Validación de MFA, contraseñas y métodos de acceso.  
- Identificación de identidades sin políticas aplicadas.

### 5. Documentación de hallazgos  
- Registro técnico de cada hallazgo.  
- Clasificación por criticidad.  
- Propuesta de mitigaciones y endurecimiento.

---

## 🔍 Validaciones realizadas  
- Identidades inventariadas correctamente.  
- Roles y permisos revisados.  
- Accesos privilegiados validados.  
- Políticas de acceso evaluadas.  
- Hallazgos documentados según estándar técnico.

---

## ⚠️ Problemas encontrados  
- Identidades con roles administrativos sin justificación.  
- Permisos excesivos sobre recursos sensibles.  
- Cuentas inactivas sin deshabilitar.  
- Ausencia de MFA en identidades críticas.

---

## 🛠 Soluciones aplicadas  
- Recomendación de aplicar MFA obligatorio.  
- Ajuste de roles y permisos excesivos.  
- Deshabilitación de identidades inactivas.  
- Propuesta de políticas de acceso más restrictivas.

---

## 🧠 Implicaciones de seguridad  
- Reducción de riesgo de escalada de privilegios.  
- Mejora del control de accesos.  
- Alineación con buenas prácticas de seguridad cloud.  
- Identificación de riesgos que requieren mitigación inmediata.

---

## 📎 Recursos útiles  
- Documentación oficial del proveedor cloud.  
- Guías de buenas prácticas de gestión de identidades.  
- Referencias de auditoría cloud.

---

## ⚙️ Comandos utilizados (opcional)  
N/A — Auditoría realizada desde consola y paneles de administración.

---

## ⚖️ Aviso Legal  
Este documento describe prácticas realizadas en un entorno de laboratorio.  
No contiene información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.