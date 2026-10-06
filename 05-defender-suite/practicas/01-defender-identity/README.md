# 01 | Defender for Identity

## Descripción del escenario y objetivo de seguridad

**Escenario:** Tenant Microsoft 365 con infraestructura híbrida y uso de Active Directory/Entra ID sin monitoreo activo de actividades anómalas, acceso privilegiado o movimientos laterales.
**Objetivo de seguridad:** Detectar comportamientos sospechosos de identidad, anomalías de autenticación y riesgo de acceso privilegiado mediante Defender for Identity.
**Alcance:** Controladores de dominio, usuarios y grupos del laboratorio, así como validación de alertas de identidad y riesgo asociado.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender for Identity** | Detección de identidad y comportamiento anómalo | Integración con Active Directory y Entra ID. |
| **Sensores de identidad** | Recolección de eventos de autenticación y actividad de dominio | Desplegados en controladores de dominio. |
| **Microsoft Entra ID** | Origen de identidades y autenticación | Validación de sign-ins sospechosos y privilegios. |
| **Timeline de incidentes** | Correlación de actividad sospechosa | Análisis de riesgo de lateral movement. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Detección de anomalías de autenticación | Sensor de Defender for Identity conectado al dominio | Recolección continua de eventos AD | MCSB IA-1 |
| Supervisión de accesos privilegiados | Analítica de comportamiento del usuario y de roles sensibles | Alertas basadas en riesgo | MCSB IA-2 |
| Identificación de lateral movement | Correlación de uso de credenciales y rutas de acceso | Timeline y detecciones de sospecha | MCSB IR-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Conectividad del sensor | Verificación del estado de servicio del sensor | Sensor operativo y conectado | Correcto |
| Detección de actividad anómala | Revisión de eventos de autenticación | Alertas de riesgo visibles | Sí |
| Validación de identidad sospechosa | Análisis de riesgos y alertas | Incidente clasificado con evidencia | Sí |
