# 03 | Defender for Office 365

## Descripción del escenario y objetivo de seguridad

**Escenario:** Entorno de Microsoft 365 con políticas de correo no reforzadas, que incrementa el riesgo de phishing, malware y acceso a enlaces maliciosos a través del bandeja de entrada.
**Objetivo de seguridad:** Evaluar y activar políticas de correo seguro, validando SafeLinks, SafeAttachments y detección de amenazas a través de Defender for Office 365.
**Alcance:** Tenant de laboratorio, buzones de correo, políticas de correo electrónico y revisión de alertas asociadas a amenazas de correo.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender for Office 365** | Protección del correo y colaboración | Políticas de seguridad y análisis de mensajes. |
| **SafeLinks** | Reescritura y validación de URLs maliciosas | Bloqueo y análisis de enlaces sospechosos. |
| **SafeAttachments** | Análisis dinámico de adjuntos | Sustitución del archivo por una versión escaneada. |
| **Threat Explorer** | Revisión de campañas y mensajes maliciosos | Análisis de indicadores y patrones. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Protección de enlaces | SafeLinks con políticas de bloqueo y seguimiento | Reglas de seguridad del tenant | MCSB AM-1 |
| Protección de adjuntos | SafeAttachments para análisis en sandbox | Filtrado previo a entrega | MCSB AM-2 |
| Detección de campañas | Revisión de amenazas y campañas de phishing | Alertas automatizadas | MCSB IR-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Validación de SafeLinks | Simulación de URL sospechosa | Bloqueo o análisis de la URL | Correcto |
| Validación de SafeAttachments | Envío de archivo sintético malicioso | Escaneo y bloqueo previo | Correcto |
| Revisión de alertas | Consulta del portal de correo y alertas | Indicadores y tendencia visibles | Sí |
