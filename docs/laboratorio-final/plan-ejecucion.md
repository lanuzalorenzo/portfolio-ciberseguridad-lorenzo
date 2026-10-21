# Plan de ejecución

> **Estado:** Fase 0 en curso. Dos evidencias de ejecución (ELK y BOLA/BFLA) y cuatro documentales o verificables (02, 03, 04 y 07); falta el tabletop para cerrar el gate. Ninguna fase Azure se ha ejecutado.

## Principios

1. **Local primero:** generar evidencia sin coste antes de desplegar en Azure.
2. **Una rebanada vertical por vez:** un runbook, una ejecución, una evidencia.
3. **Gate antes de avanzar:** no se pasa de fase sin cerrar la anterior o declarar una excepción.
4. **Coste controlado:** resource group temporal, presupuesto y destrucción al terminar.
5. **Sin datos reales:** solo datos sintéticos o anonimizados.
6. **Estado honesto:** diseño, runbook preparado y validación no son lo mismo.

## Fase 0 — Local, coste cero

**Objetivo:** fijar el estándar de runbook y evidencia con prácticas que no dependen de Azure.

| Entregable | Estado |
|---|---|
| Evidencia local de API y módulo 11 | Validado: evidencia `2026-10-21-11-api-bola` registrada en el índice |
| Runbook de ELK (módulo 10) | Validado en local |
| Ejecución de ELK con logs sintéticos | Validado en local: ingesta, 6 consultas KQL, dashboard y exportación |
| Runbook del tabletop forense (módulo 12) | Pendiente |
| Ejecución del tabletop y acta | Pendiente |
| Primera entrada del índice de evidencias | Validado: evidencias ELK (10) y BOLA/BFLA (11) enlazadas |

**Gate de salida:**

- Tres evidencias locales enlazadas.
- Plantillas de runbook y evidencia usadas al menos una vez.
- Estados actualizados en portfolio, web y perfil.
- Coste: 0.

## Fase 1 — Azure mínimo

**Objetivo:** validar una porción pequeña de la arquitectura cloud y destruirla.

| Entregable | Estado |
|---|---|
| Parámetros y comandos de despliegue del Bicep del módulo 08 | Pendiente |
| Presupuesto y resource group temporal | Pendiente |
| Despliegue de VNet, NSG, Private Endpoint, DNS privado y Key Vault | Pendiente |
| Validación positiva y negativa de conectividad | Pendiente |
| Evidencia redactada | Pendiente |
| Destrucción del resource group | Pendiente |
| Evaluación de Defender for Storage | Pendiente |

**Requisitos:**

- Autorización explícita del usuario.
- Suscripción de laboratorio y presupuesto con alertas.
- Resource group etiquetado con `lab`, `owner` y `expires`.
- Datos sintéticos.
- Plan de limpieza escrito antes de desplegar.

**Gate de salida:**

- Evidencia de despliegue y validación.
- Resource group eliminado y verificado.
- Coste real documentado.
- Limitaciones declaradas.

## Fase 2 — Azure avanzado

**Objetivo:** cubrir los controles de mayor coste y complejidad, solo si la Fase 1 está cerrada.

| Entregable | Estado |
|---|---|
| APIM + Defender for APIs | Pendiente |
| AKS/ACR + Defender for Containers | Pendiente |
| Sentinel: workspace, ingesta, reglas KQL y playbook | Pendiente |
| Entra ID real para el módulo 11 | Pendiente |

**Requisitos adicionales:**

- Presupuesto aprobado para cada bloque.
- Ventana de ejecución y limpieza.
- Confirmación de que los recursos caros se eliminan el mismo día.
- Evidencia propia por control, sin mezclar con la Fase 1.

**Gate de salida:**

- Cada control con evidencia, coste y limpieza verificada.
- Ningún recurso huérfano.
- Estados actualizados y brechas declaradas.

## Definition of done

Una práctica se considera cerrada cuando:

1. Tiene un `runbook.md` con comandos y resultados esperados.
2. Se ha ejecutado en un entorno identificado.
3. La evidencia está fechada, redactada y enlazada.
4. Existe una prueba negativa o de control cuando aplica.
5. La limpieza se ha ejecutado y verificado.
6. El README del módulo refleja el estado real.
7. La web, el perfil y la matriz de cumplimiento siguen siendo coherentes.

## Costes y limpieza

- **Fase 0:** coste cero.
- **Fase 1:** coste bajo, no nulo; requiere presupuesto y destrucción el mismo día.
- **Fase 2:** coste alto y aprovisionamiento lento; APIM, AKS y Sentinel son los bloques más caros.

Reglas:

- Crear un resource group por ejecución.
- Configurar alertas de presupuesto antes del despliegue.
- Capturar evidencia antes de destruir.
- Verificar la eliminación del resource group.
- No reutilizar recursos de producción.

## Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Coste inesperado | Alto | Presupuesto, etiquetas, destrucción y revisión diaria |
| Comandos no probados | Medio | Marcar como no ejecutados y validar en laboratorio |
| Evidencia con datos sensibles | Alto | Redacción y revisión antes de publicar |
| Diseño presentado como validación | Alto | Taxonomía de estados y enlaces a evidencia |
| Deriva entre módulos, web y perfil | Medio | Revisión de coherencia en cada cierre |
| Dependencia de una suscripción | Medio | Fase 0 local y diseño reproducible |

## Estado actual

| Fase | Estado | Nota |
|---|---|---|
| Fase 0 | En curso | API validada en CI y en local (evidencia 11); ELK validado en local con evidencia; tabletop forense pendiente |
| Fase 1 | Pendiente | Requiere suscripción, presupuesto y autorización |
| Fase 2 | Pendiente | No se inicia sin cerrar la Fase 1 |

## Próximo paso

Convertir el tabletop forense del módulo 12 en un runbook ejecutable y registrar su acta.
