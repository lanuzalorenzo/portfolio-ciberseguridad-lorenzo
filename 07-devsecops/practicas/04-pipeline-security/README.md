# 04 | Pipeline segura por defecto y validación de entregas

> **Estado:** parcial. Permisos mínimos y gates implementados y validados en CI; OIDC y despliegue no activos.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Pipeline que ejecuta cambios sin comprobaciones suficientes, con permisos excesivos y validaciones incompletas antes de publicar artefactos.  
**Objetivo de seguridad:** Diseñar una pipeline con permisos mínimos, gates de seguridad y credenciales efímeras.  
**Alcance:** CI/CD, artefactos, entornos, autenticación y gates.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **GitHub Actions** | Orquestación | Jobs independientes y `concurrency`. |
| **Permisos** | Mínimo privilegio | `contents: read`; `security-events: write` solo donde se publica SARIF. |
| **Gates** | Validación | Build, tests, SAST, SCA, secretos, contenedor e IaC. |
| **OIDC** | Autenticación federada | Diseñado, no activo. |
| **Entornos** | Control de despliegue | No hay workflow de despliegue. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Permisos mínimos | Permisos por job | MCSB DS-2 |
| Validación de releases | Gates bloqueantes | MCSB DS-1 |
| Protección de entornos | Aprobación por etapa | MCSB GS-2 |
| Sin secretos estáticos | OIDC (diseño) | MCSB IM-1 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Build y tests | `dotnet build`, `dotnet test` | Fallo si no compila o no pasan | PASS local y CI: 10 pruebas |
| Permisos mínimos | Revisión del workflow | Permisos acotados | PASS: revisado |
| Gates de seguridad | Revisión del workflow | Bloqueo ante hallazgos | PASS CI: jobs de Gitleaks, CodeQL, Trivy y contenedor en verde |
| OIDC | Revisión de `infra/README.md` | Sin secretos de larga duración | Diseñado, no activo |

## Limitaciones

- No hay suscripción de Azure asociada, por lo que no se ha validado un despliegue con OIDC.
- Los gates se ejecutan en GitHub Actions; el despliegue y la autenticación OIDC no están activos.
- La pipeline no firma artefactos ni genera SBOM; es una línea de trabajo pendiente.

## Artefactos relacionados

- [Informe técnico](informe.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
- [Diseño OIDC](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/README.md)
