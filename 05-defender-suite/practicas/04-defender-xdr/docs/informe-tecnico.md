# 🔐 Informe técnico — Práctica 04: Defender XDR

## 🧩 Introducción
Esta práctica se centra en el análisis de incidentes dentro de Microsoft Defender XDR, evaluando cómo la plataforma correlaciona señales procedentes de múltiples productos de seguridad (Identity, Endpoint, Office 365, Cloud Apps) para construir una visión completa del ataque, identificar técnicas MITRE ATT&CK y facilitar la respuesta.

---

## 🛠 Preparación del entorno

### Validación previa
Antes de analizar incidentes se verificó:
- Estado de los sensores de Defender for Identity y Endpoint.
- Funcionamiento de SafeLinks y SafeAttachments.
- Ausencia de errores de ingestión en los distintos productos.
- Permisos adecuados para visualizar y gestionar incidentes.

### Permisos
Se confirmó que la cuenta utilizada disponía de:
- Rol de Security Reader / Security Operator.
- Acceso al portal de Microsoft Defender XDR.
- Permisos para ejecutar acciones de respuesta (si se van a probar).

---

## 🚨 Análisis de incidentes

### Revisión de incidentes activos
En el portal de Microsoft Defender XDR se revisó:
- Lista de incidentes activos.
- Severidad asignada por el motor de análisis.
- Categoría del incidente.
- Técnicas MITRE ATT&CK asociadas.
- Productos implicados en la correlación.

### Correlación de señales
Se analizó cómo el incidente agrupaba señales de:
- **Identity**: movimientos laterales, Pass-the-Hash, anomalías de autenticación.
- **Endpoint**: procesos sospechosos, conexiones anómalas, actividad de scripts.
- **Office 365**: phishing, SafeLinks, SafeAttachments.
- **Cloud Apps**: actividad anómala en aplicaciones SaaS.

La correlación permitió observar cómo eventos aislados se unifican en un único incidente coherente.

---

## 🧬 Attack Timeline

### Cronología del ataque
Se revisó la línea temporal del incidente:
- Evento inicial.
- Expansión del ataque.
- Técnicas MITRE detectadas.
- Entidades afectadas.
- Acciones del atacante simuladas.

La Attack Timeline permitió comprender el flujo del ataque y su progresión.

---

## 🧬 Análisis de entidades

### Entidades implicadas
Para cada incidente se revisó:
- Usuarios implicados.
- Dispositivos afectados.
- Correos relacionados.
- Procesos y conexiones.
- Aplicaciones cloud utilizadas.

### Evaluación del impacto
Se determinó:
- Alcance del incidente.
- Riesgo para identidades privilegiadas.
- Riesgo para endpoints críticos.
- Riesgo para correo y colaboración.

---

## 🛡 Opciones de respuesta

### Acciones disponibles
Defender XDR ofrece:
- Aislamiento de dispositivos.
- Revocación de sesiones de usuario.
- Marcado de correos como maliciosos.
- Bloqueo de archivos o hashes.
- Acciones automáticas basadas en reglas.

### Validación de acciones
En el laboratorio:
- Se revisaron las acciones disponibles.
- Se validó que las acciones se mostraban correctamente.
- No se ejecutaron acciones destructivas.

---

## 🧠 Conclusiones técnicas
- La correlación entre señales funcionó correctamente.
- El incidente se construyó de forma coherente y completa.
- La Attack Timeline proporcionó una visión clara del flujo del ataque.
- Las entidades implicadas se identificaron correctamente.
- Defender XDR demostró capacidades avanzadas de correlación y respuesta.
- Se identificaron mejoras futuras:
  - Automatización de respuesta.
  - Reglas avanzadas de correlación.
  - Integración con flujos de DevSecOps.

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
