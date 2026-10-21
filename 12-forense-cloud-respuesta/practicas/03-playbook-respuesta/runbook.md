# Runbook — 12 Forense cloud / Tabletop de respuesta

> **Estado:** Diseño — esqueleto. No ejecutado.
>
> **Última ejecución:** no ejecutado.
>
> **Tipo:** tabletop (simulacro) sobre el playbook; variante de laboratorio opcional.

## 1. Objetivo

Validar que el playbook de respuesta permite investigar un incidente cloud sin destruir la trazabilidad ni dejar la exposición abierta.

Se considerará éxito si al final del simulacro existen:

- Una línea temporal con hora, fuente y hecho.
- Una decisión de contención con responsable, criterio y hora.
- Una lista de evidencias en orden de volatilidad, con su origen.
- Una lista de huecos del playbook y de acciones de mejora.

No es objetivo de este runbook desplegar en producción, medir tiempos reales de detección ni sustituir a un equipo de respuesta.

## 2. Alcance

- **Incluye:** identidad de aplicación, Key Vault, NSG, API/App Service y telemetría en Log Analytics.
- **Excluye:** tenant real, datos personales, producción, ransomware y exfiltración masiva.
- **Entorno:** tabletop sobre la documentación de las prácticas 01–03. Variante opcional en suscripción de laboratorio con datos sintéticos.
- **Datos:** sintéticos o anonimizados; sin secretos reales.

## 3. Prerrequisitos

| Requisito | Detalle | Verificación |
|---|---|---|
| Facilitador | Controla el reloj y las inyecciones | Guion de la sección 6.1 |
| Participantes | SecOps, AppSec y Cloud (pueden ser sombreros de una sola persona) | Acta con roles |
| Duración | 90 min de simulacro + 30 min de hot wash | Reloj |
| Material | Playbook, prácticas 01–03 y plantilla de acta | Enlaces de la sección 12 |
| Acceso de lectura | `Reader`, `Log Analytics Reader`, `Key Vault Reader` | `az role assignment list` |
| Suscripción (solo variante lab) | Temporal, con presupuesto y alerta | `az account show` |
| Presupuesto (solo variante lab) | Límite acordado antes de empezar | Referencia interna |

## 4. Variables

| Variable | Valor de ejemplo | Descripción |
|---|---|---|
| `INC_ID` | `INC-2026-001` | Identificador del incidente |
| `WINDOW_START` | `2026-10-21T08:00:00Z` | Inicio de la ventana a investigar |
| `WINDOW_END` | `2026-10-21T10:00:00Z` | Fin de la ventana |
| `RESOURCE_GROUP` | `rg-lab-forense` | Resource group temporal |
| `NSG_NAME` | `nsg-app` | NSG implicado |
| `KEYVAULT_NAME` | `kv-lab-forense` | Key Vault implicado |
| `APP_NAME` | `app-api-lab` | Aplicación implicada |

No usar valores de producción. En el tabletop, las variables se escriben en el acta para que la timeline sea reproducible.

## 5. Escenario y límites de confianza

Flujos simulados:

1. Una identidad de aplicación lee un secreto en Key Vault (plano de datos).
2. Una cuenta con permisos de red modifica el NSG: abre `22/tcp` a Internet o permite salida.
3. La API registra un pico de `401`.

Límites de confianza:

- Internet → NSG → subred de aplicación → API.
- Identidad → Microsoft Entra ID → Key Vault.
- Recursos → diagnóstico → Log Analytics.

Hipótesis iniciales, no conclusiones:

- Credencial o clave filtrada.
- Token de aplicación robado.
- Regla de red abierta por error o por un atacante.
- Aplicación mal configurada que provoca los `401`.

## 6. Ejecución del simulacro

### 6.1 Guion de inyecciones

| Hora | Inyección del facilitador | Respuesta esperada | Evidencia que se debe pedir |
|---|---|---|---|
| T+00 | Alerta: acceso anómalo a Key Vault desde una identidad de aplicación | Abrir incidente, severidad, ventana y responsable | Alerta, hora, identidad, IP |
| T+10 | Activity Log muestra un cambio de NSG | Identificar autor, hora y regla antes de revertir | JSON del NSG y Activity Log |
| T+20 | Pico de `401` en la API | Distinguir ataque de fallo de aplicación | Logs HTTP y correlación temporal |
| T+30 | Lectura de secreto fuera de la ventana habitual | Confirmar identidad, secreto y hora | Key Vault audit log |
| T+45 | Indicio de persistencia: rol, aplicación o clave nueva | Buscar persistencia antes de erradicar | AuditLogs, `authorized_keys`, cron |
| T+60 | Presión para contener con caída de servicio | Decidir con criterio y registrar quién decide | Acta de decisión |
| T+75 | Servicio restaurado con vigilancia | Confirmar que no hay reingreso | Métricas y logs de 30 min |
| T+90 | Hot wash | Huecos, acciones y responsables | Acta |

### 6.2 Evidencia en orden de volatilidad

| Orden | Fuente | Qué capturar | Herramienta | Riesgo si se pierde |
|---|---|---|---|---|
| 1 | Estado del host | Procesos, conexiones, sesiones y usuarios | `ps`, `ss`, `who`, `last` | Se pierde para siempre |
| 2 | Configuración de red | NSG en vuelo y reglas efectivas | `az network nsg show`, `list-effective-nsg` | Se sobrescribe al revertir |
| 3 | Logs del host | `auth.log` o Security Event Log | `journalctl`, exportación | Rotación o limpieza |
| 4 | Identidad | Sign-in logs, riesgo, sesiones | Entra ID / KQL | Retención limitada |
| 5 | Logs cloud | Activity, Audit, Key Vault, flow logs | Log Analytics | Retención y coste |
| 6 | Disco | Snapshot o imagen | `az snapshot create` | Se altera al reiniciar |

**Regla:** capturar y hashear (`sha256sum`) antes de mover. En cloud, los logs son duraderos pero la retención es finita; la configuración y las sesiones son lo más volátil.

### 6.3 Criterio de contención

| Situación | Orden | Justificación |
|---|---|---|
| Exfiltración o ejecución activa | Contener primero; capturar lo volátil en paralelo | La disponibilidad no justifica dejar salir datos |
| Sin actividad activa | Capturar y después contener | Se preserva la prueba y se evita destruir contexto |
| Duda | Capturar lo barato (2–5 min) y contener | El coste de esperar es mayor que el de capturar |

La decisión de aceptar una caída temporal la registra el responsable del servicio junto con SecOps, con hora y dato que la justifica.

### 6.4 Comandos preparados (no ejecutados)

```bash
## Captura de la configuración del NSG antes de tocarla
az network nsg show -g "$RESOURCE_GROUP" -n "$NSG_NAME" -o json > "nsg-antes-$INC_ID.json"

## Reglas efectivas de una NIC
az network nic list-effective-nsg -g "$RESOURCE_GROUP" -n "nic-app" -o json

## Actividad de la ventana
az monitor activity-log list \
  --start-time "$WINDOW_START" --end-time "$WINDOW_END" \
  --query "[?contains(operationName.value, 'securityRules')]" -o json
```

> Estado de los comandos: **no ejecutados**. Las consultas KQL están en la [práctica 02](../02-timeline-kql/README.md).

### 6.5 Trampas que el facilitador debe inyectar

| Trampa | Qué debe detectar el equipo |
|---|---|
| Cerrar el NSG con una sesión SSH abierta | El NSG es stateful: la sesión ya establecida sigue viva; hay que aislar o matar la sesión |
| Revocar sesiones de la identidad | Los access tokens ya emitidos siguen válidos hasta caducar; hay que deshabilitar o bloquear |
| Revertir el NSG antes de capturar | Se pierde la configuración exacta y el contexto del cambio |
| Rotar el secreto antes de capturar | Se pierde la versión usada y puede romperse la aplicación |
| Cambiar el NSG a mano si lo gestiona IaC | El siguiente despliegue reabre el puerto; hay que corregir el código |
| Confundir usuario local de SSH con identidad de aplicación | Son dos identidades distintas; hay que cerrar ambas |
| Asumir que el pico de `401` es un ataque | Puede ser la aplicación rota tras rotar un secreto |

## 7. Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Positiva: detección del cambio de NSG | Inyección T+10 | Identificado y documentado en ≤ 10 min | No ejecutado |
| Positiva: timeline reproducible | Acta + fuentes | Cada hecho tiene hora y origen | No ejecutado |
| Negativa: token tras revocar sesiones | Deshabilitar identidad y probar el token | El equipo declara que sigue válido hasta caducar | No ejecutado |
| Negativa: sesión tras cerrar el puerto | Cerrar `22/tcp` con sesión abierta | El equipo aísla o mata la sesión | No ejecutado |
| Control: reversión sin captura | Revertir el NSG sin exportar | El equipo detecta la pérdida de evidencia | No ejecutado |

Criterios de éxito: las seis fases cubiertas, cada decisión con responsable y hora, cada evidencia con origen y retención, y al menos tres huecos documentados.

## 8. Evidencia del tabletop

- [ ] Acta con participantes y roles.
- [ ] Timeline con hora, fuente y hecho.
- [ ] Registro de decisiones (quién, cuándo, con qué dato).
- [ ] Lista de evidencias solicitadas y su origen.
- [ ] Huecos del playbook y acciones de mejora.
- [ ] Hash de los artefactos exportados (solo variante lab).

Estado actual: **vacío**. No hay tabletop ejecutado.

## 9. Limpieza

Tabletop: no crea recursos. Archivar el acta y enlazarla desde la bitácora.

Variante lab:

```bash
az group delete --name "$RESOURCE_GROUP" --yes --no-wait
az group exists --name "$RESOURCE_GROUP"
```

**Verificación:** el resource group no existe y no quedan Key Vault, NSG ni snapshots huérfanos.

## 10. Coste y tiempo

- **Coste tabletop:** 0 €.
- **Coste variante lab:** estimado por debajo de 5 €; no medido.
- **Tiempo:** 90 min de simulacro + 30 min de hot wash.
- **Tiempo real:** no medido.

## 11. Limitaciones

- El tabletop no se ha ejecutado: este documento es un esqueleto.
- No hay workspace de Sentinel ni datos reales; las consultas no se han validado contra producción.
- Los tiempos de detección y contención no están medidos.
- La revocación de sesiones y la rotación de secretos no se han probado en un tenant de laboratorio.
- Una sola persona con tres roles introduce sesgo; el acta debe reflejarlo.
- El mapeo MITRE es orientativo y debe revisarse contra la técnica concreta.
- No cubre ransomware, exfiltración masiva ni respuesta legal.

## 12. Referencias

- [README de la práctica](README.md)
- [Recolección de evidencia](../01-recoleccion-logs-azure/README.md)
- [Consultas KQL](../02-timeline-kql/README.md)
- [Módulo 08 — Redes Azure](../../../08-seguridad-red-azure/README.md)
- [Módulo 09 — Microsoft Sentinel](../../../09-microsoft-sentinel/README.md)
- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- [RFC 3227 — Guidelines for Evidence Collection and Archiving](https://www.rfc-editor.org/rfc/rfc3227)
