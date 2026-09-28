# 🔐 Informe técnico — Práctica 03: Defender for Office 365

## 🧩 Introducción
Esta práctica aborda la configuración y validación de políticas avanzadas de protección de correo electrónico en Microsoft Defender for Office 365, incluyendo SafeLinks, SafeAttachments, reputación de URLs y archivos, análisis detonación en sandbox y revisión de alertas generadas por el motor de protección de contenido.

---

## 🛠 Preparación del entorno

### Revisión del estado actual
Antes de aplicar nuevas políticas se verificó:
- Estado de SafeLinks en el tenant.
- Estado de SafeAttachments.
- Existencia de políticas heredadas o configuraciones previas.
- Permisos del usuario para modificar políticas de seguridad.

### Requisitos de permisos
Se confirmó que la cuenta utilizada disponía de:
- Permisos de administrador de seguridad o global.
- Acceso al portal de Microsoft 365 Defender.
- Permisos para modificar políticas de correo.

---

## 🔗 Configuración de SafeLinks

### Creación o ajuste de políticas SafeLinks
SafeLinks reescribe URLs y las analiza en tiempo real.

Se configuró:
- Reescritura de URLs.
- Análisis en tiempo real.
- Protección en aplicaciones de Office.
- Seguimiento de clics.
- Aplicación a usuarios del laboratorio.

### Validación de SafeLinks
Se envió un correo con una URL simulada:
- La URL fue reescrita correctamente.
- El portal mostró reputación y análisis.
- El clic quedó registrado en telemetría.

---

## 📎 Configuración de SafeAttachments

### Creación o ajuste de políticas SafeAttachments
SafeAttachments analiza archivos adjuntos detonándolos en sandbox.

Se configuró:
- Dynamic Delivery.
- Bloqueo de archivos maliciosos.
- Reemplazo de archivos sospechosos.
- Aplicación a buzones del laboratorio.

### Validación de SafeAttachments
Se envió un correo con un archivo simulado:
- El archivo fue analizado antes de entregarse.
- El portal mostró el resultado del análisis.
- El archivo se bloqueó correctamente al ser detectado como malicioso.

---

## 📡 Validación de telemetría y señales

### Revisión de eventos en el portal
En Microsoft 365 Defender se revisó:
- Eventos de SafeLinks.
- Eventos de SafeAttachments.
- Reputación de URLs.
- Reputación de archivos.
- Actividad de usuarios protegidos.

### Revisión de alertas
El motor generó alertas relacionadas con:
- Phishing detectado.
- URL maliciosa bloqueada.
- Archivo malicioso en adjunto.
- Campaña de ingeniería social.
- Comportamiento anómalo en clics.

Para cada alerta se revisó:
- Mensaje implicado.
- Técnica detectada.
- Impacto potencial.
- Relevancia para el laboratorio.

---

## 🧠 Conclusiones técnicas
- SafeLinks y SafeAttachments quedaron configurados correctamente.
- Las políticas aplicadas protegen contra URLs y archivos maliciosos.
- La telemetría de correo fluye correctamente hacia el portal.
- Se detectaron amenazas simuladas de forma inmediata.
- Defender for Office 365 proporciona visibilidad avanzada sobre campañas de phishing y malware.
- Se identificaron mejoras futuras:
  - Configuración de anti-phishing avanzado.
  - Reglas de impersonation.
  - Protección adicional para Teams y SharePoint.

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
