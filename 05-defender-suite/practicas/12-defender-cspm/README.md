# 12 | Defender CSPM

> **Estado:** Parcial. La suscripción de laboratorio existe y el plan gratuito ya da recomendaciones; el plan de CSPM, que añade rutas de ataque y explorador, no está activo.
>
> **Referencias:** MCSB DP-3 · GS-1 · GS-2.

Una suscripción puede estar llena de recomendaciones y seguir igual durante meses: una lista de cien hallazgos sin orden no es un plan.

Defender CSPM añade a Defender for Cloud lo que el plan gratuito no tiene: el explorador de seguridad del cloud, el análisis de rutas de ataque y la evaluación sin agente. Su valor no es contar lo que está mal, es decir por dónde se llega.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Plan activo | Revisar qué funciones aparecen tras activarlo | Defender CSPM en la suscripción |
| Recomendaciones del benchmark | Comparar el cumplimiento antes y después | El plan y un ciclo de evaluación |
| Ruta de ataque | Buscar un hallazgo y seguir el camino hasta un recurso expuesto | Datos de postura y al menos un recurso público |
| Cierre | Corregir un hallazgo y comprobar que desaparece | Acceso al recurso y tiempo de reevaluación |

Las rutas de ataque no se han visto nunca en este laboratorio; el plan gratuito sí, en el módulo 04.

## Lecciones

- CSPM no arregla, prioriza. El valor está en la ruta de ataque, no en la lista de recomendaciones.
- El plan gratuito da recomendaciones; el de pago añade explorador y rutas. Saber cuál se mira evita atribuirse funciones que no están.
- Una recomendación sin dueño no se cierra: el panel no cambia hasta que alguien responde por el recurso.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
- [Módulo 04 — Defender for Cloud](../../../04-defender-for-cloud/README.md)
