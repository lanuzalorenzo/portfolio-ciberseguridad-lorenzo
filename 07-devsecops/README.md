# 07 | DevSecOps y gobernanza del software

Este módulo centra la seguridad del desarrollo en la protección del flujo de cambios, la revisión de código y la automatización de controles de seguridad antes de que un cambio llegue a producción. La práctica de protección de ramas es la base, pero el verdadero valor del módulo está en convertir la seguridad en un requisito intrínseco del ciclo de vida del software (*Shift-Left Security*).

## Carga de trabajo y aplicación de referencia

Los controles, políticas y pipelines documentados en este módulo se implementan de forma práctica sobre la aplicación empresarial [**EcommerceApi (lab-api-local-azure)**](https://github.com/lanuzalorenzo/lab-api-local-azure), cuyo pipeline CI en GitHub Actions ejecuta de forma automatizada escaneo de secretos (Gitleaks), análisis estático de dependencias NuGet (Trivy SCA) y verificación del contenedor Docker non-root.

## Objetivo del módulo

Validar cómo una estrategia DevSecOps minimiza el riesgo de cambios no revisados, credenciales expuestas, despliegues no controlados y vulnerabilidades introducidas en repositorios o pipelines de entrega.

## Prácticas documentadas

- [Protección de ramas y revisión de cambios](practicas/01-proteccion-ramas/README.md)
- [Detección de secretos y credenciales expuestas](practicas/02-secret-scanning/README.md)
- [SAST, SCA e IaC scanning](practicas/03-sast-sca-iac/README.md)
- [Pipeline segura por defecto y validación de entregas](practicas/04-pipeline-security/README.md)

## Registro del trabajo

Las [bitácoras del módulo](bitacora/) documentan la evolución del laboratorio, la revisión de controles y la consolidación del enfoque DevSecOps del portfolio.

## Alcance

Este módulo recoge las prácticas de referencia en seguridad del repositorio, análisis estático y control de integraciones aplicadas a un flujo de trabajo real. La documentación se mantiene alineada con el estilo del resto del portfolio y vinculada con los workflows de CI/CD de `lab-api-local-azure`.


## Arquitectura y componentes de seguridad considerados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Repositorio Git** | Origen del código y trazabilidad de cambios | Control del flujo de integración y revisión. |
| **Pull Request** | Canal de validación y aprobación | Revisión obligatoria antes de fusionar. |
| **Branch protection** | Protección de la rama principal | Evita commits directos, force push y borrado. |
| **Secret scanning** | Detección de credenciales y tokens | Escaneo en commits, PRs y ramas. |
| **SAST / SCA / IaC scanning** | Identificación de vulnerabilidades y riesgos estáticos | Revisión automática del código y plantillas. |
| **Pipelines seguras** | Validación y hardening del flujo de entrega | Rechazo de cambios con fallos o riesgo de seguridad. |
| **Auditoría de cambios** | Evidencia de trazabilidad | Registros ligibles para revisión y compliance. |

## Controles DevSecOps implementados

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Protección de rama principal | Se exige revisión previa y no se permite escritura directa | GitHub / Azure DevOps / GitLab policy | MCSB DS-1 |
| Revisión obligatoria | Pull Request con validación de aprobador(es) | Governance de repositorio | MCSB GS-2 |
| Detección de secretos | Escaneo de tokens, claves y credenciales | Secret scanning en CI/CD y repositorio | MCSB IM-1 |
| Seguridad estática | SAST, SCA e IaC scanning | Escaneo automatizado previo al merge | MCSB PV-2 |
| Pipelines seguras | Validación de artefactos y permisos mínimos | Policy-as-code y gates | MCSB DS-2 |
| Integridad del historial | Se evita el force push y el borrado de la rama base | Política de repositorio | MCSB IR-1 |

## Validación del módulo

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Protección de rama principal | Revisión de reglas de repositorio | Rama main protegida | Sí |
| Revisión obligatoria | Validación de pull request | Requiere aprobación previa | Sí |
| Detección de secretos | Analítica de credenciales expuestas | Hallazgos visibles y corregibles | Sí |
| Seguridad estática | Escaneo de código y IaC | Riesgos detectados en tiempo de validación | Sí |
| Pipeline segura | Validación del flujo | Rechazo de entregas inseguras | Sí |
