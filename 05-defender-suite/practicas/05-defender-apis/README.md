# 05 | Defender for APIs

> **Estado:** diseño documentado. No ejecutado: la API no está desplegada en Azure API Management ni tiene Defender for APIs habilitado.

## Descripción del escenario y objetivo de seguridad

**Escenario:** API REST expuesta a clientes sin protección de runtime específica para tráfico de APIs, con visibilidad limitada de abuso de negocio, BOLA/BFLA y patrones de ataque del OWASP API Security Top 10.  
**Objetivo de seguridad:** Incorporar Microsoft Defender for APIs sobre Azure API Management para descubrir, clasificar y detectar comportamiento anómalo en las operaciones de la API.  
**Alcance:** API `EcommerceApi` publicada en API Management; suscripciones, productos, políticas y telemetría de Defender for APIs.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure API Management** | Gateway y publicación de la API | Importación de OpenAPI; políticas de cuota y JWT. |
| **Defender for APIs** | Protección de runtime y postura | Onboarding de la API en Defender for Cloud. |
| **Microsoft Defender for Cloud** | Consola de hallazgos | Alertas y recomendaciones de API. |
| **Log Analytics** | Evidencia y correlación | Diagnóstico de APIM y Defender. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Inventario de APIs | Importación desde OpenAPI | OWASP API9 |
| Detección de abuso | Defender for APIs | OWASP API1/API4/API5 |
| Límites de consumo | Políticas de APIM | OWASP API4 |
| Autenticación centralizada | Validación JWT en APIM y API | OWASP API2 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Onboarding de la API | Defender for Cloud → Defender for APIs | API descubierta y clasificada | Pendiente: requiere APIM desplegado |
| Detección de tráfico anómalo | Simulación de enumeración de pedidos | Alerta de comportamiento sospechoso | Pendiente |
| Aplicación de cuota | Pruebas de volumen contra APIM | `429` y alerta | Pendiente |
| Correlación con Sentinel | Consulta KQL de alertas | Incidente trazable | Pendiente |

## Limitaciones

- Requiere un despliegue real de API Management y una suscripción con Defender for APIs.
- El coste de APIM y Defender no se ha estimado.
- La API actual no aplica scopes/roles; APIM puede complementar, pero no sustituir, la autorización de la aplicación.

## Artefactos relacionados

- [API de referencia](https://github.com/lanuzalorenzo/lab-api-local-azure)
- [Módulo 11 — Hacking ético de APIs](../../../11-hacking-etico-api/README.md)
- [Guion de la práctica](GUION.md)
