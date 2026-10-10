# Bitácora — Cierre del módulo 10

## Contexto y alcance

Este cierre consolida el recorrido del módulo ELK Stack Security y lo sitúa dentro del conjunto del portfolio de ciberseguridad. El objetivo es dejar constancia de la progresión técnica de este bloque: desde la ingesta de eventos hasta la detección visual con Kibana.

## Objetivo

Cerrar el módulo con una revisión del flujo completo, resumir el caso de uso y dejar claro qué elementos son útiles para la observabilidad y qué aspectos quedan pendientes de validación técnica real.

## Trabajo realizado

- Definición del caso de uso de seguridad basado en autenticación fallida, patrones de uso anómalo y actividad privilegiada.
- Diseño de la ingesta con Logstash y preparación del esquema de normalización.
- Elaboración de la práctica de Kibana para convertir la señal en detección visual.
- Documentación del flujo completo en README, bitácora e informes técnicos.
- Revisión de la coherencia del módulo con el resto del portfolio.

## Resultados y validaciones

- La práctica queda conectada con la lógica del portfolio: normalización, detección y respuesta operativa.
- ELK se presenta como una capa útil de observabilidad y análisis para contextos de seguridad.
- El módulo mantiene la disciplina del repositorio: diseño y documentación, sin afirmar despliegues o validaciones no ejecutadas.

## Pendientes y riesgos

- No se ha ejecutado el laboratorio completo en un entorno real ni operativo.
- El caso de uso sigue siendo un escenario simulado y debe interpretarse como diseño técnico.
- La validación real de dashboards, índices y consultas dependerá de un entorno con volumen y contexto adecuados.

## Aprendizaje clave

- ELK no es solo una herramienta de log; también es una capa de análisis de seguridad y contexto de riesgo.
- El gran valor de la pila radica en la normalización y la correlación entre eventos.
- La detección visual necesita un caso de uso definido para ser útil; sin hipótesis clara, las búsquedas se convierten en ruido.

## Siguiente paso

Ampliar este módulo con una práctica adicional centrada en alertas o detección más concreta, o cerrar el bloque y pasar al siguiente eje del portfolio con nueva continuidad temática.
