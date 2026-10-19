# 07 | Defender for Storage

> **Estado:** diseño documentado. No ejecutado: no hay cuenta de almacenamiento con Defender for Storage habilitado.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Datos y artefactos de la API almacenados en Azure Storage sin detección de malware, sin clasificación de datos sensibles y con visibilidad limitada de accesos anómalos.  
**Objetivo de seguridad:** Proteger el plano de datos de Storage con Defender for Storage: análisis de malware en carga, descubrimiento de datos sensibles y alertas de actividad sospechosa.  
**Alcance:** Cuenta de almacenamiento de laboratorio, contenedores de blobs y telemetría de Defender.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Storage** | Almacenamiento de blobs | HTTPS only, TLS 1.2, acceso público deshabilitado. |
| **Defender for Storage** | Malware scanning y detección | Habilitado a nivel de cuenta. |
| **Microsoft Purview** | Clasificación de datos | Integración opcional. |
| **Log Analytics** | Evidencia | Diagnóstico de Storage. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Cifrado en tránsito | HTTPS y TLS 1.2 | MCSB DP-3 |
| Acceso público | Deshabilitado; Private Endpoint | MCSB NS-2 |
| Malware scanning | Defender for Storage | MCSB DP-2 |
| Detección de acceso anómalo | Alertas de Defender | MCSB IR-2 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Carga de archivo limpio | Subida a blob | Sin alerta | Pendiente: requiere Storage |
| Carga de EICAR | Subida de muestra de prueba | Alerta de malware | Pendiente |
| Acceso anónimo | Intento de lectura pública | Bloqueo | Pendiente |
| Acceso desde ubicación anómala | Simulación | Alerta | Pendiente |

## Limitaciones

- No se ha desplegado una cuenta de Storage ni habilitado Defender for Storage.
- El análisis de malware tiene coste por GB y requiere configuración de retención.
- La clasificación de datos sensible necesita Purview y etiquetas de confidencialidad.

## Artefactos relacionados

- [Guion de la práctica](GUION.md)
- [Módulo 08 — Redes Azure](../../../08-seguridad-red-azure/README.md)
