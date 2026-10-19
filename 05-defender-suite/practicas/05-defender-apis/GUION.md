# Guion — Práctica 05: Defender for APIs

## Objetivo

Publicar `EcommerceApi` en Azure API Management y habilitar Defender for APIs para validar descubrimiento, clasificación y detección de abuso.

## Contexto

Defender for APIs analiza el tráfico de APIs gestionadas en APIM y genera hallazgos de postura y alertas de runtime. No inspecciona una API que solo se ejecuta en local.

## Preparación

1. Crear una instancia de API Management (nivel de laboratorio).
2. Importar el OpenAPI de la API.
3. Configurar una política de validación JWT y una cuota de peticiones.
4. Habilitar Defender for APIs en Defender for Cloud.
5. Registrar la API en el plan de Defender.

## Ejecución

1. Verificar que la API aparece en el inventario de Defender for APIs.
2. Revisar la clasificación de operaciones y datos sensibles.
3. Ejecutar tráfico normal y confirmar telemetría.
4. Simular enumeración de pedidos (`GET /api/orders/{id}` con IDs consecutivos) y peticiones masivas.
5. Revisar alertas y recomendaciones en Defender for Cloud.
6. Exportar evidencia a Log Analytics y correlacionar en Sentinel.

## Validaciones

| Prueba | Resultado esperado |
|---|---|
| Descubrimiento | API y operaciones visibles |
| Clasificación | Operaciones y datos etiquetados |
| Tráfico anómalo | Alerta de comportamiento sospechoso |
| Cuota | `429` y registro |
| Correlación | Consulta KQL con evidencia |

## Cierre

Documentar hallazgos, falsos positivos y ajustes de política. Registrar el estado real: si APIM o Defender no están disponibles, la práctica queda como diseño y no como validación ejecutada.
