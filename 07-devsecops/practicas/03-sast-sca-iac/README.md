# 03 | SAST, SCA e IaC scanning

> **Estado:** validado en CI (run 39243360276, 2026-10-19). SAST, SCA e IaC completaron sin hallazgos CRITICAL/HIGH.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Proyecto con dependencias de terceros, infraestructura declarativa y lógica de aplicación sin validación automatizada antes del merge.  
**Objetivo de seguridad:** Automatizar la validación de código, dependencias y plantillas antes de la entrega.  
**Alcance:** Código .NET, paquetes NuGet y plantillas Bicep.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **CodeQL** | SAST para C# | `security-extended`, autobuild. |
| **Trivy fs** | SCA de dependencias | CRITICAL/HIGH, `ignore-unfixed`. |
| **Trivy config** | IaC scanning | ARM compilado desde Bicep. |
| **Dependency Review** | Revisión de cambios de dependencias | Solo PR, severidad High. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| SAST | CodeQL en cada push/PR | MCSB PV-2 |
| SCA | Trivy bloqueante | MCSB PV-3 |
| IaC | Trivy config sobre ARM | MCSB DS-1 |
| Bloqueo por hallazgos | `exit-code: 1` | MCSB IR-2 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| SAST | CodeQL | Hallazgos publicados en Security | PASS CI: CodeQL completado y SARIF publicado |
| SCA | Trivy fs | Sin CRITICAL/HIGH no corregidos | PASS local y CI: 0 hallazgos |
| IaC | `bicep build` + Trivy config | Plantilla válida y sin CRITICAL/HIGH | PASS local y CI: hallazgos AZU justificados |
| Dependency Review | PR con cambio de paquete | Bloqueo por severidad High | Implementado |

## Limitaciones

- Trivy no interpreta `.bicep`; se compila a ARM antes del escaneo.
- `AZU-0013` se suprime con justificación porque el Key Vault usa `defaultAction: Deny`, sin acceso público y con Private Endpoint; Trivy no evalúa bien el bloque `networkAcls` del ARM compilado.
- CodeQL y el escaneo de imagen requieren GitHub Actions; no se han ejecutado localmente.

## Artefactos relacionados

- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
- [Plantilla Bicep](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/main.bicep)
- [Justificación de Trivy](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.trivyignore)
