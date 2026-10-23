# 01 | Activación de planes

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB GS-1, EP-1, EP-2, IR-2.

Una suscripción recién creada ya trae Defender for Cloud, pero en su versión mínima: inventario, Secure Score y recomendaciones. Sabe qué hay; no sabe qué pasa dentro. La diferencia entre saber y vigilar son los planes de pago, y elegirlos es una decisión de coste tanto como de riesgo.

## Qué se decidió

| Plan | Coste | Decisión en el laboratorio |
|---|---|---|
| Foundational CSPM | Gratuito | Activo por defecto |
| Defender CSPM | Por recurso | Evaluado, no activado |
| Defender for Servers Plan 1 | Por servidor y hora | **Activado** |
| Defender for Servers Plan 2 | Por servidor y hora | Evaluado, no activado |
| Defender for Storage | Por cuenta | Evaluado, no activado |

## Validación

| Prueba | Resultado observado |
|---|---|
| Estado de los planes | Foundational CSPM y Servers Plan 1 en *On* |
| Extensión MDE en la VM de prueba | Instalada sola, sin onboarding manual |
| Secure Score tras la activación | Aparecen controles de endpoint y de configuración del sistema |

## Lecciones

- Activar el catálogo entero es fácil y caro; el valor está en justificar cada plan por el riesgo que cubre.
- El aprovisionamiento automático del agente funciona, pero conviene excluir las máquinas no críticas.
- El CSPM gratuito da visibilidad suficiente para empezar; lo que falta después no es inventario, es detección.

## Más detalle

- [Catálogo evaluado y verificación](docs/informe-tecnico.md)
