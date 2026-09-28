# 🔐 Informe técnico — Práctica 02: Defender for Endpoint

## 🧩 Introducción
Esta práctica aborda el proceso de onboarding de dispositivos en Microsoft Defender for Endpoint, la validación de telemetría EDR, la revisión del estado de protección y el análisis inicial de señales generadas por el motor de comportamiento. El objetivo es habilitar visibilidad completa sobre procesos, conexiones, actividad del sistema y técnicas MITRE ATT&CK detectadas en el endpoint.

---

## 🛠 Preparación del entorno

### Validación del dispositivo
Antes del onboarding se verificó:
- Versión del sistema operativo compatible con Defender for Endpoint.
- Conectividad a Internet mediante HTTPS.
- Permisos administrativos para ejecutar el script de incorporación.
- Estado del antivirus local para evitar conflictos con el agente EDR.

### Revisión de permisos
Se confirmó que la cuenta utilizada disponía de:
- Acceso al portal de Microsoft Defender for Endpoint.
- Permisos para ejecutar scripts en el endpoint.
- Privilegios administrativos en el dispositivo.

---

## 📥 Descarga del paquete de onboarding
Desde el portal de Microsoft Defender for Endpoint se descargó:
- El script de incorporación.
- La configuración del agente.
- La clave de registro del tenant.

El paquete se trasladó al endpoint para su ejecución.

---

## 🏗 Ejecución del onboarding

### Instalación del agente
En el endpoint:
- Se ejecutó el script con privilegios elevados.
- Se validó que el agente se instaló correctamente.
- Se confirmó que los servicios asociados quedaron activos.
- Se revisaron los eventos generados por el instalador en el visor de sucesos.

### Validación inicial
Se comprobó:
- El dispositivo apareció en el portal como **Active**.
- El estado de protección se mostró como **Onboarded**.
- La telemetría comenzó a enviarse (procesos, conexiones, eventos del sistema).

---

## 📡 Validación de telemetría y señales

### Estado del dispositivo en el portal
En Defender for Endpoint se revisó:
- Última conexión del dispositivo.
- Eventos recibidos.
- Estado del sensor EDR.
- Información del sistema (procesos, red, archivos).

### Confirmación de ingestión de telemetría
Se verificó que el portal recibía:
- Procesos iniciados.
- Conexiones de red.
- Actividad del sistema de archivos.
- Eventos de seguridad del endpoint.

---

## 🔍 Revisión inicial de alertas EDR

### Detecciones automáticas
Tras el onboarding, el motor EDR generó señales relacionadas con:
- Ejecución de procesos sospechosos.
- Conexiones anómalas.
- Actividad de scripts.
- Técnicas MITRE ATT&CK detectadas.
- Comportamientos potencialmente maliciosos.

### Análisis de alertas
Para cada alerta se revisó:
- Proceso implicado.
- Técnica MITRE asociada.
- Impacto potencial.
- Relevancia para el entorno del laboratorio.

---

## 🧠 Conclusiones técnicas
- El endpoint quedó completamente operativo y en estado **Active**.
- La telemetría EDR fluye correctamente hacia el servicio cloud.
- Se generaron alertas iniciales que demuestran la capacidad del motor de análisis.
- Defender for Endpoint proporciona visibilidad avanzada sobre procesos, conexiones y técnicas MITRE ATT&CK.
- Se identificaron posibles mejoras futuras:
  - Integración con Sysmon.
  - Hardening del endpoint.
  - Configuración de reglas de reducción de superficie de ataque (ASR).

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
