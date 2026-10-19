# Runbook — [Módulo] / [Práctica]

> **Estado:** Runbook preparado / Parcial / Validado
>
> **Última ejecución:** [fecha o «no ejecutado»]

## 1. Objetivo

Qué control se valida, qué riesgo se reduce y qué se considerará éxito.

## 2. Alcance

- Componentes incluidos.
- Componentes excluidos.
- Entorno: local, Azure de laboratorio o híbrido.
- Datos: sintéticos o anonimizados.

## 3. Prerrequisitos

| Requisito | Detalle | Verificación |
|---|---|---|
| Sistema / herramienta | Versión mínima | `[comando]` |
| Permisos | Rol o ámbito necesario | `[comando]` |
| Suscripción / tenant | Solo laboratorio | `[comando]` |
| Presupuesto | Límite y alerta | `[referencia]` |

## 4. Variables

| Variable | Valor de ejemplo | Descripción |
|---|---|---|
| `RESOURCE_GROUP` | `rg-lab-...` | Resource group temporal |
| `LOCATION` | `[región]` | Región del laboratorio |
| `PREFIX` | `lab-...` | Prefijo de recursos |

No incluyas valores reales de producción.

## 5. Arquitectura del escenario

Describe o enlaza el diagrama. Indica límites de confianza, flujos y recursos que se crean.

## 6. Ejecución

### Paso 1 — [Nombre]

```bash
[comando]
```

**Resultado esperado:** [salida o estado observable]

**Si falla:** [diagnóstico y alternativa]

### Paso 2 — [Nombre]

```bash
[comando]
```

**Resultado esperado:** [salida o estado observable]

## 7. Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Positiva | [comando o consulta] | [estado] | [PASS / FAIL / no ejecutado] |
| Negativa | [comando o consulta] | [estado] | [PASS / FAIL / no ejecutado] |

## 8. Evidencia

- [ ] Salida de comandos redactada.
- [ ] Consulta o captura relevante.
- [ ] Fecha y entorno.
- [ ] Resultado y limitaciones.
- [ ] Enlace a la entrada del índice de evidencias.

## 9. Limpieza

```bash
[comando de eliminación]
```

**Verificación:** [cómo confirmar que no quedan recursos]

## 10. Coste y tiempo

- **Coste estimado:** [importe o «desconocido»]
- **Coste real:** [importe o «no aplica»]
- **Tiempo estimado:** [minutos]
- **Tiempo real:** [minutos]

## 11. Limitaciones

- [Qué no se ha podido probar.]
- [Qué depende de una suscripción, tenant o presupuesto.]
- [Qué se declara como diseño y no como validación.]

## 12. Referencias

- [README del módulo]
- [Documentación oficial]
- [Evidencia relacionada]
