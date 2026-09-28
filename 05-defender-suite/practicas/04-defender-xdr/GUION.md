# 🧪 Guion — Práctica 04: Defender XDR

## 🎯 Objetivo
Analizar incidentes y correlaciones en Microsoft Defender XDR, comprendiendo cómo se unifican señales de identidad, endpoint, correo y aplicaciones para construir una visión completa del ataque, identificar técnicas MITRE ATT&CK y evaluar opciones de respuesta.

---

## 🧩 Contexto técnico
Microsoft Defender XDR es la plataforma de correlación y respuesta unificada que integra:
- Señales de **Defender for Identity**.
- Señales de **Defender for Endpoint**.
- Señales de **Defender for Office 365**.
- Señales de **Defender for Cloud Apps**.
- Señales de **Azure AD / Entra ID**.

Su objetivo es:
- Correlacionar eventos dispersos en un único incidente.
- Mostrar la cronología completa del ataque.
- Identificar entidades implicadas.
- Clasificar técnicas MITRE ATT&CK.
- Facilitar la respuesta centralizada.

---

## 🛠 Preparación del entorno

### 🔹 1. Revisión del estado del portal
Antes de analizar incidentes:
- Validar que los sensores de Identity y Endpoint están enviando telemetría.
- Confirmar que SafeLinks y SafeAttachments están activos.
- Revisar que no existan errores de ingestión en ningún producto.

### 🔹 2. Requisitos de permisos
El usuario debe disponer de:
- Rol de **Security Reader**, **Security Operator** o superior.
- Acceso al portal de Microsoft Defender XDR.
- Permisos para ejecutar acciones de respuesta (si se van a probar).

---

## 🚨 Análisis de incidentes

### 🔹 3. Revisión de incidentes activos
En Microsoft Defender XDR:
- Acceder a **Incidents**.
- Seleccionar un incidente activo o simulado.
- Revisar:
  - Severidad.
  - Categoría.
  - Técnicas MITRE asociadas.
  - Productos implicados.

### 🔹 4. Correlación de señales
Analizar cómo el incidente agrupa señales de:
- Identity (movimiento lateral, Pass-the-Hash, anomalías de autenticación).
- Endpoint (procesos sospechosos, conexiones anómalas).
- Office 365 (phishing, SafeLinks, SafeAttachments).
- Cloud Apps (actividad anómala en aplicaciones SaaS).

### 🔹 5. Attack Timeline
Revisar la cronología del ataque:
- Evento inicial.
- Expansión del ataque.
- Técnicas MITRE detectadas.
- Entidades afectadas.
- Acciones del atacante simuladas.

---

## 🧬 Análisis de entidades

### 🔹 6. Entidades implicadas
Para cada incidente:
- Revisar usuarios implicados.
- Revisar dispositivos afectados.
- Revisar correos relacionados.
- Revisar procesos y conexiones.
- Revisar aplicaciones cloud utilizadas.

### 🔹 7. Evaluación del impacto
Determinar:
- Alcance del incidente.
- Riesgo para identidades privilegiadas.
- Riesgo para endpoints críticos.
- Riesgo para correo y colaboración.

---

## 🛡 Opciones de respuesta

### 🔹 8. Acciones disponibles
Defender XDR permite:
- Aislar un dispositivo.
- Revocar sesiones de usuario.
- Marcar un correo como malicioso.
- Bloquear un archivo o hash.
- Ejecutar acciones automáticas basadas en reglas.

### 🔹 9. Validación de acciones
En el laboratorio:
- Revisar qué acciones están disponibles.
- Validar que las acciones se muestran correctamente.
- No ejecutar acciones destructivas (laboratorio controlado).

---

## 🧠 Cierre de la práctica

### 🔹 10. Conclusiones técnicas
- Evaluar la correlación entre señales.
- Confirmar que el incidente se construye correctamente.
- Validar que la cronología del ataque es coherente.
- Identificar mejoras futuras (automatización, reglas avanzadas).

### 🔹 11. Registro en bitácora
Se documentará al final del módulo, según tu instrucción.

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
