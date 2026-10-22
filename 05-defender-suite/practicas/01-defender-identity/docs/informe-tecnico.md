# Informe técnico — Práctica 01: Defender for Identity

> **En fácil:** este informe cuenta qué se instaló y qué se comprobó al conectar el controlador de dominio con Defender for Identity. Resume lo observado: el sensor queda activo, envía datos y genera las primeras alertas.

## Introducción

Esta práctica aborda la integración de Active Directory con Microsoft Defender for Identity mediante la instalación del sensor oficial, la validación de telemetría y el análisis inicial de señales de seguridad relacionadas con identidades y credenciales. El objetivo es habilitar visibilidad sobre técnicas de ataque basadas en autenticación y movimiento lateral.

## Preparación del entorno

### Validación del controlador de dominio

Antes de desplegar el sensor se verificó:

- Versión del sistema operativo compatible con el sensor.
- Acceso a Internet mediante HTTPS.
- Disponibilidad de los logs necesarios:
  - Security Event Log
  - Directory Service Log
  - Sysmon, si está presente

### Revisión de permisos

Se confirmó que la cuenta utilizada disponía de:

- Permisos de instalación en el DC.
- Permisos para ejecutar el instalador del sensor.
- Acceso al portal de Defender for Identity.

## Descarga del sensor

Desde el portal de Microsoft Defender for Identity se descargó:

- El instalador del sensor.
- La clave de acceso única del tenant.
- La configuración predefinida del sensor.

El paquete se trasladó al controlador de dominio para su instalación.

## Instalación del sensor

### Ejecución del instalador

En el controlador de dominio:

- Se ejecutó el instalador con privilegios elevados.
- Se introdujo la clave de acceso del portal.
- Se validó que el servicio del sensor quedó en estado **Running**.
- Se revisaron los eventos generados por el instalador en el visor de sucesos.

### Validación del servicio

Se comprobó:

- Estado del servicio: **Running**.
- Conectividad con el servicio cloud.
- Lectura de logs del DC.
- Registro de telemetría en el portal.

## Validación de conectividad y telemetría

### Estado del sensor en el portal

El sensor apareció como **Healthy**, mostrando:

- Última conexión.
- Volumen de eventos procesados.
- Estado de los componentes internos.

### Confirmación de ingestión de señales

Se verificó que el portal recibía:

- Eventos de autenticación.
- Cambios de privilegios.
- Accesos a objetos sensibles.
- Actividad de cuentas privilegiadas.

## Revisión inicial de alertas

### Detecciones automáticas

Tras la instalación, el motor de análisis comenzó a generar señales relacionadas con:

- Pass-the-Hash.
- Pass-the-Ticket.
- Kerberoasting.
- Reconocimiento de AD.
- Intentos de movimiento lateral.
- Uso anómalo de cuentas de servicio.

### Análisis de alertas

Para cada alerta se revisó:

- Origen del evento.
- Técnica detectada.
- Impacto potencial.
- Relevancia para el entorno del laboratorio.

## Conclusiones técnicas

- El sensor quedó operativo y en estado **Healthy**.
- La telemetría fluye desde el DC hacia el servicio cloud.
- El motor de análisis generó alertas iniciales.
- Defender for Identity proporciona visibilidad sobre técnicas de ataque basadas en credenciales.
- Mejoras futuras identificadas:
  - Integración con Sysmon.
  - Auditorías avanzadas en el DC.
  - Hardening adicional del controlador de dominio.

## Aviso legal

Este documento describe prácticas realizadas en un entorno de laboratorio. No contiene información sensible ni perteneciente a ninguna organización real. Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
