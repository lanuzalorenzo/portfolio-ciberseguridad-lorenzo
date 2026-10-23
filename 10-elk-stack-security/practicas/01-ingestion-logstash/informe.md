# Informe técnico — Ingestión y normalización con Logstash

## Estado del documento

Diseño del laboratorio en curso. No se ha ejecutado una validación real en entorno operativo.

## Escenario

Se propone un caso de uso realista basado en actividades de seguridad en un sistema Linux con servicios web y acceso remoto. El ejemplo central será la correlación de:

- intentos repetidos de acceso SSH;
- fallos de autenticación para usuarios privilegiados;
- uso inusual de comandos con permisos elevados;
- accesos anómalos a rutas o endpoints del servicio web.

El objetivo es revisar cómo Logstash puede transformar estos eventos heterogéneos en datos normales y prepararlos para detección y análisis posterior.

## Diseño propuesto

1. Definir una fuente de logs con volumen reducido pero representativo: `auth.log`, `secure.log` y logs de acceso HTTP.
2. Montar una pipeline con filtros básicos: `grok`, `mutate`, `date` y `geoip` si se necesita contextualizar IPs.
3. Identificar campos clave para seguridad: host, servicio, usuario, ip_origen, evento, resultado, timestamp y detalle.
4. Crear una estructura de índices que permita distinguir entre autenticación, servicio web y actividad del sistema.
5. Enviar los eventos a Elasticsearch con una forma de correlacionar por usuario, host e IP.
6. Validar con consultas simples desde Kibana y preparar la base para paneles de detección.

## Caso real de log propuesto

Ejemplo de patrón de eventos a recoger:

- Login fallido desde una IP extranjera repetida en varias ventanas temporales.
- Uso de `sudo` en una sesión sin historial previo de uso administrativo.
- Acceso a rutas no habituales del servicio web en un periodo breve.
- Múltiples intentos de autenticación para el mismo usuario en un corto intervalo.

Este tipo de combinación es útil porque puede reflejar actividades de fuerza bruta, acceso anómalo, enumeración o intento de escalada.

## Consideraciones técnicas

- El esquema debe priorizar la trazabilidad sobre el volumen de campos.
- Un buen pipeline de normalización no solo separa eventos, sino que facilita la comparación entre host, usuario y origen.
- La detección aprovecha mucho más si cada evento tiene contexto, no solo el mensaje textualmente crudo.
- La ingesta debe permitir distinguir eventos de autenticación, sistema y web para no mezclar señales no comparables.

## Siguientes pasos

- Ejecutar una prueba de flujo con logs de ejemplo.
- Validar el número de documentos indexados por tipo de evento.
- Revisar la visualización inicial de eventos en Kibana y preparar métricas simples de anomalía.
- Definir una detección básica orientada a intentos múltiples, IPs repetidas y comportamiento fuera de horario.
