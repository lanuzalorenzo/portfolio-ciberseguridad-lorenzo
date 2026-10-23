# 03 | SAST, SCA e IaC

> **Estado:** **Validado** en CI (run 39243360276, 2026-10-19). Los tres análisis terminaron sin hallazgos CRITICAL ni HIGH.
>
> **Referencias:** MCSB PV-2, PV-3, DS-1, IR-2.

Tres preguntas distintas antes del merge: si el código tiene un patrón vulnerable, si una dependencia arrastra un CVE y si la infraestructura declarada abre algo que no debería. Cada una la responde una herramienta, y las tres pueden tumbar el pipeline.

## Qué se aplicó

| Análisis | Herramienta y configuración |
|---|---|
| SAST | CodeQL para C#, consultas `security-extended`, autobuild |
| SCA | Trivy filesystem, CRITICAL y HIGH, `ignore-unfixed` |
| IaC | `bicep build` y Trivy config sobre el ARM compilado |
| Dependencias nuevas | Dependency Review en el PR, bloqueo por severidad High |

## Validación

| Prueba | Resultado observado |
|---|---|
| CodeQL | Completado y SARIF publicado en Security |
| Trivy fs | 0 hallazgos CRITICAL/HIGH sin corregir |
| Trivy config | Plantilla válida; `AZU-0013` justificado en `.trivyignore` |

## Lecciones

- Trivy no lee `.bicep`: hay que compilar a ARM y escanear esa salida, con el desfase que eso supone.
- `ignore-unfixed` evita bloquear por lo que no tiene parche, pero deja ese riesgo sin fecha de arreglo.
- Una supresión sin justificación escrita es un agujero silencioso; `AZU-0013` se explica porque Trivy no interpreta bien el bloque `networkAcls`.

## Más detalle

- [Módulo 07](../../README.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
- [Plantilla Bicep](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/main.bicep)
- [Justificación de Trivy](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.trivyignore)
