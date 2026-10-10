# Bitácora — Inicio del módulo 10

## Contexto y alcance

Este módulo continúa la línea del portfolio hacia la observabilidad y la seguridad operativa. Tras los módulos centrados en Azure, Defender y Sentinel, se incorpora un enfoque basado en ELK para analizar eventos, correlacionar señales y construir una vista operativa del riesgo.

## Objetivo

Definir la estructura del módulo, identificar el caso de uso de seguridad y documentar qué tipo de log, pipeline y visualización serán relevantes para un laboratorio práctico.

## Trabajo realizado

- Revisión del recorrido del portfolio para consolidar continuidad temática.
- Identificación del eje principal: ingestión, correlación y visualización de registros de seguridad.
- Definición de una estructura de módulo basada en README, bitácora y prácticas.
- Planteamiento de dos prácticas principales: ingestión con Logstash y análisis con Kibana.
- Enmarcado del trabajo como laboratorio y diseño técnico, no como despliegue real de producción.

## Resultados y validaciones

- La propuesta mantiene coherencia con el conjunto del portfolio.
- ELK encaja como complemento de Sentinel y de la observabilidad de entornos cloud.
- La estructura del módulo queda alineada con los módulos anteriores.

## Pendientes y riesgos

- Falta definir el escenario real o simulado de eventos.
- No se han ejecutado pruebas ni validado dashboards en un entorno operativo.
- La elección del volumen y tipo de logs condicionará la utilidad del diseño.

## Aprendizaje clave

- ELK funciona muy bien como capa de analítica y visualización, pero requiere una estrategia clara de normalización y correlación.
- La continuidad del portfolio exige que cada módulo aporte un eje distinto de seguridad: identidad, posture, respuesta y ahora analítica.

## Siguiente paso

Preparar la primera práctica dedicando la siguiente sesión a la ingestión de logs en Logstash y a la definición del modelo de datos para un caso de seguridad.
