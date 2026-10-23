# Índice de evidencias

> **Estado:** 7 evidencias registradas: 3 de ejecución y 4 documentales o verificables.

Este directorio centraliza las evidencias del laboratorio final. Cada entrada debe poder rastrearse hasta un runbook, un informe o un run de CI, y hasta un entorno concreto. No es un repositorio de capturas sueltas.

> Una evidencia es el recibo de algo que se hizo: qué se ejecutó, cuándo, con qué resultado y dónde está la prueba. Un informe escrito a posteriori no es lo mismo que el registro de una ejecución, y aquí se distinguen.

## Dos tipos de evidencia

| Tipo | Qué aporta | Qué no aporta |
|---|---|---|
| **Ejecución** | Carpeta fechada con comandos, salida redactada y artefactos | Nada: es el registro completo |
| **Documental** | Informe técnico + bitácora fechada + tabla de resultados | No conserva la salida original ni capturas |
| **Verificable** | Un run de CI reproducible y enlazado | Solo cubre lo que el pipeline ejecuta |

Una evidencia documental **no se presenta como una captura**. Si la práctica se reejecuta, se sustituye por una evidencia de ejecución.

## Convención de nombres

```text
YYYY-MM-DD-modulo-practica/
  README.md          # resumen, resultado y limitaciones
  comandos.md        # comandos ejecutados y salida redactada
  artefactos/        # capturas, consultas, JSON o logs redactados
```

Ejemplo:

```text
2026-10-19-10-elk-ingesta/
```

## Dos rutas dentro de la evidencia de ejecución

| Ruta | Qué registra | Núcleo |
|---|---|---|
| **A — Ejecución** | Algo que se ejecutó: comandos, salida y artefactos | Comandos, validación, artefactos |
| **B — Decisión** | Algo que se decidió: tabletop, triaje, simulacro, respuesta a incidente | El caso, propuestas y valoración, decisión óptima |

Una evidencia de **decisión** se indexa como de ejecución —se hizo, con fecha y acta—, pero **no puede declarar PASS sin acta de decisiones**. Lo que prueba es criterio, no capacidad técnica: el estado del módulo no sube a **Validado** hasta que exista recolección real.

## Contenido mínimo de una evidencia de ejecución (ruta A)

- Fecha y responsable.
- Runbook utilizado.
- Entorno y alcance.
- Comandos ejecutados.
- Resultado observado: PASS, FAIL o parcial.
- Prueba negativa o de control, si aplica.
- Limpieza realizada.
- Coste, si hubo recursos cloud.
- Limitaciones y lo que no se ha ejecutado.
- Enlaces a artefactos redactados.

## Reglas de redacción

- Sin secretos, tokens, claves ni cadenas de conexión.
- Sin direcciones IP internas, nombres de máquinas ni identificadores reales.
- Sin datos personales.
- Sin capturas que muestren información fuera del alcance.
- Si un dato es necesario para entender la evidencia, se sustituye por un placeholder explícito.

## Evidencias de ejecución

| Fecha | Módulo | Práctica | Resultado | Enlace |
|---|---|---|---|---|
| 2026-10-19 | 10 — ELK Stack Security | 01 — Ingestión y normalización · 02 — Kibana | Validado en local | [Ver evidencia](2026-10-19-10-elk-ingesta/README.md) |
| 2026-10-21 | 11 — Hacking ético de APIs | 01 — BOLA/BFLA · 03 — Mass assignment | Validado en local | [Ver evidencia](2026-10-21-11-api-bola/README.md) |
| 2026-10-22 | 12 — Forense cloud y respuesta | 03 — Playbook de respuesta · tabletop | PASS como tabletop (sin recolección técnica) | [Ver acta](2026-10-22-12-tabletop/README.md) |

## Evidencias documentales y verificables

| Fecha | Módulo | Tipo | Qué prueba | Enlace |
|---|---|---|---|---|
| 2026-09-11 | 02 — Identity Security | Documental | 7 prácticas (MFA, Passwordless, SSPR, PIM, RBAC, Key Vault, Managed Identities) con informe técnico, tabla de resultados y bitácora | [Módulo](../../02-identity-security/README.md) |
| 2026-09-15 | 03 — Cloud Audits | Documental | 3 auditorías (suscripciones, recursos críticos, identidades) con hallazgos y recomendaciones | [Módulo](../../03-cloud-audits/README.md) |
| 2026-09-25 | 04 — Defender for Cloud | Documental | 4 prácticas (planes, recomendaciones, workloads, hardening) con informe y bitácora | [Módulo](../../04-defender-for-cloud/README.md) |
| 2026-10-19 | 07 — DevSecOps | Verificable (CI) | Pipeline completa en verde: build, 10 pruebas, Gitleaks, CodeQL, Trivy SCA, contenedor no-root e IaC | [Run 39243360276](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/39243360276) |

> Las evidencias documentales se apoyan en el informe y la bitácora del módulo. Declaran explícitamente que no se conservó la salida original; por eso no se mezclan con las de ejecución.

## Pendiente

- Módulo 01: reejecutar PKCE manual con tenant de laboratorio y generar evidencia de ejecución.
- Módulo 06: ejecutar los controles con licencia P1/P2; hoy son diseño y no hay resultados que tabular.
- Módulo 12: ejecutar la variante de laboratorio del tabletop y la recolección técnica con datos sintéticos.

## Plantilla

Usa la [plantilla de evidencia](../../plantillas/evidencia-template.md) como punto de partida. Tiene dos rutas: **A** para lo ejecutado y **B** para lo decidido (tabletop, triaje, simulacro). El acta `2026-10-22-12-tabletop` es la primera evidencia escrita con la ruta B.
