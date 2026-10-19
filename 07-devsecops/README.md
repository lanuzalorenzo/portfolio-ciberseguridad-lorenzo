# 07 | DevSecOps y gobernanza del software

> **Estado:** parcialmente validado. Controles de repositorio y pipeline implementados; la primera ejecución verde del pipeline ampliado debe confirmarse en GitHub Actions.

Este módulo centra la seguridad del desarrollo en la protección del flujo de cambios, la revisión de código y la automatización de controles antes de que un cambio llegue a producción. La protección de ramas es la base; el valor principal está en convertir la seguridad en un requisito del ciclo de vida (*Shift-Left Security*).

## Carga de trabajo de referencia

Los controles se aplican sobre [**EcommerceApi (lab-api-local-azure)**](https://github.com/lanuzalorenzo/lab-api-local-azure). Su pipeline ejecuta compilación, pruebas de integración, Gitleaks, CodeQL, Trivy SCA, escaneo de contenedor y Trivy config sobre Bicep.

## Objetivo del módulo

Reducir el riesgo de cambios no revisados, credenciales expuestas, dependencias vulnerables, configuraciones inseguras y entregas sin validación.

## Prácticas documentadas

- [Protección de ramas y revisión de cambios](practicas/01-proteccion-ramas/README.md)
- [Detección de secretos y credenciales expuestas](practicas/02-secret-scanning/README.md)
- [SAST, SCA e IaC scanning](practicas/03-sast-sca-iac/README.md)
- [Pipeline segura por defecto y validación de entregas](practicas/04-pipeline-security/README.md)

## Controles y estado real

| Control | Implementación | Estado | Evidencia |
|---|---|---|---|
| Protección de rama principal | PR + revisión + bloqueo de force-push/borrado | Implementado en repositorios de código | Reglas de GitHub |
| Revisión obligatoria | Aprobación previa al merge | Implementado con bypass de administrador documentado | Configuración del repositorio |
| Detección de secretos | Gitleaks sobre historial completo | Implementado; validado localmente | `.gitleaks.toml`, workflow |
| SAST | CodeQL C# (`security-extended`) | Implementado en workflow; ejecución en GitHub pendiente | Workflow `devsecops-ci.yml` |
| SCA | Trivy filesystem, CRITICAL/HIGH | Implementado; validado localmente | Workflow, Trivy |
| Contenedor | Docker multi-stage, usuario no-root, Trivy image | Implementado | `Dockerfile`, workflow |
| IaC | Bicep + Trivy config | Implementado; validado con `bicep build` y Trivy local | `infra/`, workflow |
| Dependency Review | Bloqueo por severidad High en PR | Implementado | Workflow |
| OIDC a Azure | Identidad federada sin secretos | Diseñado, no activo | `infra/README.md` |
| Pruebas de integración | xUnit, 10 pruebas | Implementado y ejecutado localmente | `tests/EcommerceApi.Tests` |

## Validación del módulo

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Protección de rama principal | Revisión de reglas del repositorio | `main` protegida con PR | PASS: regla activa; bypass de admin documentado |
| Revisión obligatoria | Configuración de pull request | Aprobación previa | PASS: revisión requerida |
| Detección de secretos | Gitleaks sobre historial | Sin hallazgos reales | PASS local: 27 commits escaneados, 0 leaks |
| SAST | CodeQL en CI | Análisis publicado | Implementado; pendiente de ejecución remota |
| SCA | Trivy sobre dependencias | Sin CRITICAL/HIGH no corregidos | PASS local: 0 hallazgos |
| IaC | `bicep build` + Trivy config | Plantilla válida y sin CRITICAL/HIGH | PASS local; AZU-0013 justificado en `.trivyignore` |
| Contenedor no-root | `docker run --entrypoint id` | UID distinto de 0 | Definido en el workflow; Docker no disponible en el entorno local |
| Pipeline bloqueante | Revisión del workflow | Fallo ante hallazgos críticos | Implementado; pendiente de ejecución remota |

## Limitaciones

- El propietario administrador puede omitir la protección de rama; la regla no es una defensa absoluta contra la propia cuenta comprometida.
- CodeQL y el escaneo de contenedor se ejecutan en GitHub Actions; no se han reproducido localmente en este entorno.
- El análisis IaC usa el ARM compilado desde Bicep porque Trivy no interpreta `.bicep` directamente.
- No hay workflow de despliegue ni OIDC activo.
- El escaneo de secretos necesita una allowlist para ejemplos de documentación; la allowlist está acotada por ruta y patrón.

## Registro del trabajo

Las [bitácoras del módulo](bitacora/) documentan la evolución del laboratorio y las decisiones técnicas.
