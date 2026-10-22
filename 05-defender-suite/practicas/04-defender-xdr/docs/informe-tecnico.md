# Informe técnico — Práctica 04: Defender XDR

> **En fácil:** este informe cuenta qué se observó al reunir en un solo incidente las señales de identidad, equipo, correo y aplicaciones. La idea es leer la historia del ataque en orden, no cuatro historias separadas.

## Introducción

Esta práctica se centra en el análisis de incidentes dentro de Microsoft Defender XDR: cómo la plataforma correlaciona señales procedentes de varios productos de seguridad (Identity, Endpoint, Office 365 y Cloud Apps) para construir una visión del ataque, identificar técnicas MITRE ATT&CK y facilitar la respuesta.

## Preparación del entorno

### Validación previa

Antes de analizar incidentes se verificó:

- Estado de los sensores de Defender for Identity y Endpoint.
- Funcionamiento de SafeLinks y SafeAttachments.
- Ausencia de errores de ingestión en los distintos productos.
- Permisos adecuados para visualizar y gestionar incidentes.

### Permisos

Se confirmó que la cuenta utilizada disponía de:

- Rol de Security Reader o Security Operator.
- Acceso al portal de Microsoft Defender XDR.
- Permisos para ejecutar acciones de respuesta, si se van a probar.

## Análisis de incidentes

### Revisión de incidentes activos

En el portal de Microsoft Defender XDR se revisó:

- Lista de incidentes activos.
- Severidad asignada por el motor de análisis.
- Categoría del incidente.
- Técnicas MITRE ATT&CK asociadas.
- Productos implicados en la correlación.

### Correlación de señales

Se analizó cómo el incidente agrupaba señales de:

- **Identity**: movimientos laterales, Pass-the-Hash y anomalías de autenticación.
- **Endpoint**: procesos sospechosos, conexiones anómalas y actividad de scripts.
- **Office 365**: phishing, SafeLinks y SafeAttachments.
- **Cloud Apps**: actividad anómala en aplicaciones SaaS.

La correlación mostró cómo eventos aislados se unifican en un único incidente.

## Attack Timeline

### Cronología del ataque

Se revisó la línea temporal del incidente:

- Evento inicial.
- Expansión del ataque.
- Técnicas MITRE detectadas.
- Entidades afectadas.
- Acciones del atacante simuladas.

La Attack Timeline mostró el flujo del ataque y su progresión.

## Análisis de entidades

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

## Opciones de respuesta

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

## Conclusiones técnicas

- La correlación entre señales funcionó.
- El incidente se construyó de forma coherente.
- La Attack Timeline mostró el flujo del ataque.
- Las entidades implicadas se identificaron.
- Defender XDR correlacionó señales de varios productos en un único incidente.
- Mejoras futuras identificadas:
  - Automatización de respuesta.
  - Reglas de correlación avanzadas.
  - Integración con flujos de DevSecOps.

## Aviso legal

Este documento describe prácticas realizadas en un entorno de laboratorio. No contiene información sensible ni perteneciente a ninguna organización real. Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
