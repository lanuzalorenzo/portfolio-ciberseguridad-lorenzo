# 02 | Detección de secretos y credenciales expuestas

> **Estado:** validado localmente y en CI (run 39243360276, 2026-10-19).

## Descripción del escenario y objetivo de seguridad

**Escenario:** Historial de desarrollo que puede contener tokens, claves, cadenas de conexión o credenciales insertadas accidentalmente.  
**Objetivo de seguridad:** Detectar y eliminar credenciales expuestas antes de que se integren o compartan.  
**Alcance:** Historial Git, pull requests, releases y flujo de desarrollo.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Gitleaks** | Detección de secretos | Escaneo del historial completo en CI. |
| **Allowlist acotada** | Evitar falsos positivos | Solo rutas de documentación y patrones `$TOKEN`/JWT truncados. |
| **GitHub Actions** | Ejecución automática | Push, PR y ejecución manual. |
| **Respuesta** | Rotación y limpieza | Procedimiento documentado. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Escaneo temprano | Gitleaks en cada push/PR | MCSB IM-1 |
| Revisión de historial | `fetch-depth: 0` | MCSB IM-2 |
| Bloqueo en CI | `--exit-code 2` | MCSB DS-2 |
| Rotación | Regenerar credenciales comprometidas | MCSB IA-3 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Escaneo del historial | Gitleaks 8.30.1 sobre historial completo | Sin secretos reales | PASS local y CI: 0 leaks |
| Falsos positivos de documentación | Allowlist por ruta y patrón | Sin ocultar secretos arbitrarios | PASS: allowlist acotada |
| Bloqueo en CI | `--exit-code 2` | Falla ante hallazgo | PASS CI: job completado sin hallazgos |

## Limitación

La allowlist de documentación podría ocultar un secreto real introducido en un `.md`. Se revisa manualmente y se mantiene limitada a patrones de placeholder. Si se detecta un secreto real, se rota y se evalúa la reescritura del historial.

## Artefactos relacionados

- [Informe técnico](informe.md)
- [`.gitleaks.toml`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.gitleaks.toml)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
