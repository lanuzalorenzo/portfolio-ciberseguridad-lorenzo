# 🧪 Guion — Práctica 03: Defender for Office 365

## 🎯 Objetivo
Configurar y validar políticas avanzadas de protección de correo electrónico en Microsoft Defender for Office 365, incluyendo SafeLinks, SafeAttachments, análisis de amenazas, reputación de URLs y archivos, así como la revisión de alertas generadas por el motor de protección de contenido.

---

## 🧩 Contexto técnico
Microsoft Defender for Office 365 proporciona protección contra amenazas basadas en correo electrónico y colaboración, incluyendo:
- Phishing dirigido y masivo.
- Malware en archivos adjuntos.
- URLs maliciosas o con reputación dudosa.
- Campañas de ingeniería social.
- Análisis detonación en sandbox.
- Detección de patrones de ataque en mensajes.

La práctica se centra en configurar políticas clave y validar su comportamiento.

---

## 🛠 Preparación del entorno

### 🔹 1. Revisión del estado actual
Antes de aplicar nuevas políticas:
- Revisar políticas existentes en el tenant.
- Validar si SafeLinks y SafeAttachments están activos.
- Comprobar si existen reglas heredadas o configuraciones previas.

### 🔹 2. Requisitos de permisos
El usuario debe disponer de:
- Permisos de administrador de seguridad o administrador global.
- Acceso al portal de Microsoft 365 Defender.
- Permisos para modificar políticas de seguridad.

---

## 🔗 Configuración de SafeLinks

### 🔹 3. Creación o ajuste de políticas SafeLinks
SafeLinks analiza URLs en tiempo real y las reescribe para protección.

Pasos:
- Acceder a **Email & Collaboration → Policies & Rules → Threat Policies**.
- Seleccionar **Safe Links**.
- Crear una nueva política o modificar una existente.
- Activar:
  - Reescritura de URLs.
  - Análisis en tiempo real.
  - Protección en aplicaciones de Office.
  - Seguimiento de clics en enlaces.
- Aplicar la política a:
  - Usuarios específicos.
  - Grupos.
  - Toda la organización (según el laboratorio).

### 🔹 4. Validación de SafeLinks
- Enviar un correo con una URL maliciosa simulada.
- Verificar que la URL se reescribe.
- Comprobar que el portal muestra el análisis de reputación.
- Validar que el clic queda registrado.

---

## 📎 Configuración de SafeAttachments

### 🔹 5. Creación o ajuste de políticas SafeAttachments
SafeAttachments analiza archivos adjuntos detonándolos en sandbox.

Pasos:
- Acceder a **Threat Policies → Safe Attachments**.
- Crear o modificar una política.
- Activar:
  - Dynamic Delivery.
  - Bloqueo de archivos maliciosos.
  - Reemplazo de archivos sospechosos.
- Aplicar la política a buzones o grupos.

### 🔹 6. Validación de SafeAttachments
- Enviar un correo con un archivo simulado (EICAR o similar).
- Verificar que el archivo se analiza antes de entregarse.
- Confirmar que el portal muestra el resultado del análisis.
- Validar que el archivo se bloquea si es malicioso.

---

## 📡 Validación de telemetría y señales

### 🔹 7. Revisión de eventos en el portal
En Microsoft 365 Defender:
- Revisar eventos de SafeLinks.
- Revisar eventos de SafeAttachments.
- Validar reputación de URLs y archivos.
- Comprobar actividad de usuarios protegidos.

### 🔹 8. Revisión de alertas
El motor de análisis puede generar alertas relacionadas con:
- Phishing detectado.
- URL maliciosa bloqueada.
- Archivo malicioso en adjunto.
- Campaña de ingeniería social.
- Comportamiento anómalo en clics.

Para cada alerta:
- Revisar el mensaje implicado.
- Validar la técnica detectada.
- Comprobar el impacto potencial.
- Registrar observaciones relevantes.

---

## 🧠 Cierre de la práctica

### 🔹 9. Conclusiones técnicas
- Evaluar la efectividad de SafeLinks y SafeAttachments.
- Confirmar que las políticas aplicadas protegen correctamente.
- Identificar mejoras futuras (anti-phishing avanzado, reglas de impersonation).

### 🔹 10. Registro en bitácora
Se documentará al final del módulo, según tu instrucción.

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
