# Índice de evidencias

> **Evidencias registradas:** 22: 16 de ejecución y 6 documentales o verificables.

Este directorio centraliza las evidencias del laboratorio final. Cada entrada debe poder rastrearse hasta un runbook, un informe o un run de CI, y hasta un entorno concreto. No es un repositorio de capturas sueltas.

> Una evidencia es el recibo de algo que se hizo: qué se ejecutó, cuándo, con qué resultado y dónde está la prueba. Un informe escrito a posteriori no es lo mismo que el registro de una ejecución, y aquí se distinguen.

## Tipos de evidencia

| Tipo | Qué aporta | Límite |
|---|---|---|
| **Ejecución** | Carpeta fechada con comandos, salida redactada y artefactos | No sustituye al runbook |
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

## Contenido mínimo

La [plantilla de evidencia](../../plantillas/evidencia-template.md) fija los apartados y las dos rutas. El índice solo añade lo específico: runbook utilizado, fecha, resultado y limitaciones.

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
| 2026-11-02 | 11 — Hacking ético de APIs | Laboratorio de inclusión de ficheros en PHP | Validado en local | [Ver evidencia](2026-11-02-11-upload-progress-include/README.md) |
| 2026-11-05 | 11 — Hacking ético de APIs | 03 — Rate limiting y mass assignment | Validado en local (ráfaga secuencial) | [Ver evidencia](2026-11-05-11-api-rate-limit/README.md) |
| 2026-11-05 | 11 — Hacking ético de APIs | 03 — Rate limiting bajo carga | Validado en local (concurrencia) | [Ver evidencia](2026-11-05-11-api-rate-limit-carga/README.md) |
| 2026-11-06 | Laboratorio local | VM de pruebas con disco del perfil cifrado | Validado en local; perfil móvil pendiente | [Ver evidencia](2026-11-06-lab-vm-pruebas/README.md) |
| 2026-11-08 | 11 — Hacking ético de APIs | DAST (análisis dinámico) sin autenticar — ZAP baseline | Parcial: 0 FAIL y 0 WARN; endpoints de negocio sin cubrir | [Ver evidencia](2026-11-08-11-api-dast/README.md) |
| 2026-11-09 | Laboratorio final — Workload (caso local) | Caída intermitente del CLR por `libunwind` en una solución .NET distinta de EcommerceApi | Validado en local | [Ver evidencia](2026-11-09-dotnet-clr-libunwind/README.md) |
| 2026-11-09 | 07 — DevSecOps | Remediación de la cabecera `Server` en EcommerceApi: hallazgo, causa, parche, prueba de regresión y run de CI | Validado en local y en CI | [Ver evidencia](2026-11-09-07-remediacion-server-header/README.md) |
| 2026-11-12 | 11 — Hacking ético de APIs | Límite de cuerpo de 16 KB: 16 384 bytes aceptados y 17 408 rechazados con `413` | Validado en local | [Ver evidencia](2026-11-12-11-api-body-limit/README.md) |
| 2026-11-12 | 07 — DevSecOps | Inventario del binario publicado: 5 PDB antes, 0 después; sin secretos en el host descompilado | Validado en local | [Ver evidencia](2026-11-12-05-api-binary/README.md) |
| 2026-11-15 | 02 — Identity Security | 08 — Robo y reutilización de la cookie de sesión: extracción del perfil real, cierre en servidor y caducidad | Validado en local | [Ver evidencia](2026-11-15-02-cookie-sesion/README.md) |
| 2026-11-22 | 11 — Hacking ético de APIs | Agente autónomo contra la API: BOLA en 5–14 s en las tres tandas y escritura sin rol en una, sin salida a Internet; del lado azul, el log da ruta y código pero no identidad | Validado en local (ataque); Parcial (detección, sin SIEM) | [Ver evidencia](2026-11-22-11-api-agente/README.md) |
| 2026-11-26 | 08 — Seguridad de red en Azure | Red desplegada y API en Container Apps: VNet, NSG y subredes; `/health` 200 y 401 sin token | Validado en la capa gratuita; capa de pago en Diseño | [Ver evidencia](2026-11-26-08-red-y-api/README.md) |
| 2026-11-26 | 01 — OAuth 2.0, PKCE y JWT | 01 — PKCE manual con cliente público: autorización, canje, validación JWKS y dos pruebas negativas | Validado en local | [Ver evidencia](../../01-seguridad-azure/practicas/01-pkce-manual/evidencias/2026-11-26-01-pkce-manual/README.md) |

## Evidencias documentales y verificables

| Fecha | Módulo | Tipo | Qué prueba | Enlace |
|---|---|---|---|---|
| 2026-09-11 | 02 — Identity Security | Documental | 7 prácticas (MFA, Passwordless, SSPR, PIM, RBAC, Key Vault, Managed Identities) con informe técnico, tabla de resultados y bitácora | [Módulo](../../02-identity-security/README.md) |
| 2026-09-15 | 03 — Cloud Audits | Documental | 3 auditorías (suscripciones, recursos críticos, identidades) con hallazgos y recomendaciones | [Módulo](../../03-cloud-audits/README.md) |
| 2026-09-25 | 04 — Defender for Cloud | Documental | 4 prácticas (planes, recomendaciones, workloads, hardening) con informe y bitácora | [Módulo](../../04-defender-for-cloud/README.md) |
| 2026-10-19 | 07 — DevSecOps | Verificable (CI) | Pipeline completa en verde: build, 10 pruebas, Gitleaks, CodeQL, Trivy SCA, contenedor no-root e IaC | [Run 39243360276](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/39243360276) |
| 2026-11-12 | 07 — DevSecOps | Verificable (CI) | SBOM CycloneDX de la imagen publicada, adjunto a la ejecución: 3 842 componentes, con el digest de la imagen y el del fichero | [Run 43245455930](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/43245455930) |
| 2026-11-12 | 07 — DevSecOps | Verificable (CI) | Imagen firmada con cosign keyless y SBOM atestado; `cosign verify` y `cosign verify-attestation` en verde | [Run 43314295991](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/43314295991) |

> Las evidencias documentales se apoyan en el informe y la bitácora del módulo. Declaran explícitamente que no se conservó la salida original; por eso no se mezclan con las de ejecución.

## Pendiente

- Módulo 06: ejecutar los controles con licencia P1/P2; hoy son diseño y no hay resultados que tabular.
- Módulo 11: ejecutar DAST activo y autenticado cuando exista tenant.
- Módulo 11: probar una regla de detección con identidad y propiedad del dato (KQL/SIEM) sobre los logs del agente; hoy la detección es `grep` y queda en parcial.
- Módulo 12: ejecutar la variante de laboratorio del tabletop y la recolección técnica con datos sintéticos.
- Workload: confirmar el arreglo de `libunwind` en Ubuntu con una versión que incluya la corrección de `libunwind/libunwind#993`.

## Plantilla

Usa la [plantilla de evidencia](../../plantillas/evidencia-template.md) como punto de partida. Tiene dos rutas: **A** para lo ejecutado y **B** para lo decidido (tabletop, triaje, simulacro). El acta `2026-10-22-12-tabletop` es la primera evidencia escrita con la ruta B.
