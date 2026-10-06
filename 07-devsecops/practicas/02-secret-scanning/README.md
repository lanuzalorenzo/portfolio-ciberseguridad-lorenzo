# 02 | Detección de secretos y credenciales expuestas

## Descripción del escenario y objetivo de seguridad

**Escenario:** Repositorio con historial de desarrollo que puede contener tokens, claves, cadenas de conexión o credenciales insertadas accidentalmente en código, variables de entorno o archivos de configuración.  
**Objetivo de seguridad:** Detectar y eliminar credenciales expuestas antes de que se integren en el repositorio o se compartan con terceros.  
**Alcance:** Repositorio Git, historial de cambios, pull requests, releases y validación de secretos en los flujos de desarrollo.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de seguridad considerados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Secret scanning** | Detección de cadenas confidenciales | Escaneo activo en commits y PRs. |
| **Pre-commit hooks** | Prevención local antes de subir cambios | Validación temprana del código. |
| **Repositorios remotos** | Origen del código y trazabilidad | GitHub / Azure DevOps / GitLab con controles de seguridad. |
| **Auditoría y alertas** | Evidencia y notificación de exposición | Alertas por riesgo y resolución. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Escaneo temprano de secretos | Verificación previa al merge | GitHub secret scanning / herramientas de análisis | MCSB IM-1 |
| Revisión de historial | Búsqueda de credenciales en commits previos | Auditoría periódica del repositorio | MCSB IM-2 |
| Bloqueo en PR | Rechazo automático si se detecta una clave | Gates de seguridad | MCSB DS-2 |
| Rotación de credenciales | Eliminar y regenerar credenciales comprometidas | Respuesta operativa | MCSB IA-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Detección de credenciales sintéticas | Inserción controlada o análisis de patrones | Hallazgo detectado | Sí |
| Validación en PR | Ejecución del escáner con cambio sospechoso | Bloqueo del merge | Sí |
| Revisión de historial | Búsqueda de secretos en commits previos | Riesgos detectados y corregibles | Sí |
