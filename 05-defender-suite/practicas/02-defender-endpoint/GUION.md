# 🧪 Guion — Práctica 02: Defender for Endpoint

## 🎯 Objetivo
Realizar el onboarding de dispositivos en Microsoft Defender for Endpoint, validar la ingestión de telemetría, comprobar el estado de protección EDR y analizar las primeras señales generadas por el motor de comportamiento y detección de amenazas.

---

## 🧩 Contexto técnico
Microsoft Defender for Endpoint es una plataforma EDR que proporciona:
- Supervisión completa del comportamiento del sistema.
- Detección de técnicas MITRE ATT&CK.
- Análisis de procesos, conexiones, archivos y actividad sospechosa.
- Alertas automáticas basadas en anomalías y patrones de ataque.
- Capacidad de respuesta ante incidentes (aislamiento, bloqueo, investigación).

La práctica se centra en incorporar un endpoint, validar su telemetría y observar las primeras señales de seguridad.

---

## 🛠 Preparación del entorno

### 🔹 1. Validación del dispositivo
Antes del onboarding se revisa:
- Versión del sistema operativo compatible.
- Conectividad a Internet mediante HTTPS.
- Permisos de ejecución del script de onboarding.
- Estado del antivirus local (si existe coexistencia).

### 🔹 2. Requisitos de permisos
El usuario debe disponer de:
- Acceso al portal de Microsoft Defender for Endpoint.
- Permisos para ejecutar scripts en el endpoint.
- Permisos administrativos en el dispositivo.

---

## 📥 Descarga del paquete de onboarding

### 🔹 3. Obtención del paquete
Desde el portal de Microsoft Defender for Endpoint:
- Acceder a **Settings → Endpoints → Device onboarding**.
- Seleccionar el sistema operativo del endpoint.
- Descargar el paquete de incorporación.
- Copiar el script al dispositivo objetivo.

El paquete incluye:
- Script de onboarding.
- Configuración del agente.
- Clave de registro del tenant.

---

## 🏗 Ejecución del onboarding

### 🔹 4. Ejecución del script
En el endpoint:
- Ejecutar el script con privilegios elevados.
- Validar que el agente se instala correctamente.
- Confirmar que los servicios asociados quedan activos.
- Revisar el visor de sucesos para detectar errores de instalación.

### 🔹 5. Validación inicial
Comprobar:
- El dispositivo aparece en el portal como **Active**.
- El estado de protección es **Onboarded**.
- La telemetría comienza a enviarse (procesos, conexiones, eventos).

---

## 📡 Validación de telemetría y señales

### 🔹 6. Estado del dispositivo en el portal
En Defender for Endpoint:
- Revisar la página del dispositivo.
- Confirmar:
  - Última conexión.
  - Eventos recibidos.
  - Estado del sensor EDR.
  - Información del sistema.

### 🔹 7. Confirmación de ingestión de telemetría
Validar que el portal recibe:
- Procesos iniciados.
- Conexiones de red.
- Actividad del sistema de archivos.
- Eventos de seguridad del endpoint.

---

## 🔍 Revisión inicial de alertas EDR

### 🔹 8. Detecciones automáticas
Tras el onboarding, el motor EDR puede generar señales relacionadas con:
- Ejecución de procesos sospechosos.
- Conexiones anómalas.
- Actividad de scripts.
- Técnicas MITRE ATT&CK detectadas.
- Comportamientos potencialmente maliciosos.

### 🔹 9. Análisis de alertas
Para cada alerta:
- Revisar el proceso implicado.
- Validar la técnica MITRE asociada.
- Comprobar el impacto potencial.
- Registrar observaciones relevantes.

---

## 🧠 Cierre de la práctica

### 🔹 10. Conclusiones técnicas
- Evaluar la calidad de la telemetría recibida.
- Confirmar que el endpoint está completamente operativo.
- Identificar mejoras futuras (integración con Sysmon, hardening del endpoint, reglas de reducción de superficie de ataque).

### 🔹 11. Registro en bitácora
Documentar:
- Estado final del endpoint.
- Validaciones realizadas.
- Alertas observadas.
- Próximos pasos del módulo.

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
