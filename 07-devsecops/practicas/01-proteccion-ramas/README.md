# 01 | Protección de ramas y revisión de cambios

## Descripción del escenario y objetivo de seguridad

**Escenario:** Repositorio de software con varios desarrolladores y flujo de cambios directo hacia la rama principal, sin validación previa ni control de integridad del historial. Esto permite introducir cambios no revisados, sobrescrituras accidentales y falta de trazabilidad operacional.  
**Objetivo de seguridad:** Garantizar que cualquier integración hacia la rama principal pase por revisión con aprobaciones, validación automática y restricciones de integridad del historial.  
**Alcance:** Repositorio Git de laboratorio, rama principal, pull requests, revisión de cambios y reglas de protección del flujo de trabajo.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de seguridad considerados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Repositorio Git** | Almacén del código fuente | Rama principal protegida de escritura directa. |
| **Pull Request** | Canal de revisión y validación | Todos los cambios pasan por este mecanismo. |
| **Required reviewers** | Revisión humana previa a la fusión | Exigido al menos un aprobador. |
| **Status checks** | Validaciones automáticas de calidad y seguridad | Ejecución de pruebas, lint y análisis de seguridad. |
| **Historial de commits** | Trazabilidad del desarrollo | Se evita el `force-push` y el borrado de la rama base. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Protección de la rama principal | Se exige PR para integrar cambios | Política del repositorio | MCSB DS-1 |
| Revisión obligatoria | Se requiere aprobación previa antes de fusionar | Reglas del flujo de integración | MCSB GS-2 |
| Bloqueo de sobreescritura | Se prohibe `force-push` y el borrado de la rama base | Configuración de protección | MCSB IR-1 |
| Validación automática | Checks obligatorios en CI/CD antes de merge | Pipeline y status checks | MCSB DS-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Escritura directa a `main` | Intento de commit directo a la rama protegida | Bloqueado | Sí |
| Fusión via pull request | Apertura del PR y validación | Requiere aprobación previa | Sí |
| Protección de historial | Intento de `force-push` | Rechazado por la política | Sí |
| Validación automática | Ejecución de checks de pipeline | Requisitos obligatorios antes de integrar | Sí |
