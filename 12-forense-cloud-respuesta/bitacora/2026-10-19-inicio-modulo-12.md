# Bitácora — Inicio del módulo 12

## Objetivo

Añadir una capa de forense cloud y respuesta que complemente la detección del módulo 09 y el diseño de red del módulo 08.

## Contexto y alcance

- Azure Activity Log, Entra ID, Defender, App Service, Key Vault y NSG flow logs.
- Sin workspace de Sentinel ni datos reales.
- KQL revisado, no ejecutado.

## Trabajo realizado

- Definición de fuentes y retención.
- Procedimiento de preservación y cadena de custodia.
- Consultas KQL para línea temporal.
- Playbook de respuesta basado en NIST SP 800-61.
- Mapeo orientativo a MITRE ATT&CK.

## Resultados

- Modelo de evidencia documentado.
- Consultas listas para validar en un workspace.
- Playbook y tabletop diseñados.

## Pendientes o riesgos

- Desplegar Log Analytics y diagnóstico.
- Ejecutar consultas con datos de laboratorio.
- Realizar un tabletop y medir tiempos.
- Validar retención y coste.

## Aprendizaje

La respuesta a incidentes cloud depende de la calidad de la telemetría y de la preservación. Sin logs centralizados y retención suficiente, la investigación se limita a hipótesis.

## Siguiente paso

Integrar el diagnóstico del Bicep en un despliegue de laboratorio y ejecutar un incidente simulado.
