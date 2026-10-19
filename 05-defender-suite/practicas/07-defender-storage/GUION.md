# Guion — Práctica 07: Defender for Storage

## Objetivo

Validar la protección del plano de datos de Azure Storage con Defender for Storage.

## Preparación

1. Crear una cuenta de Storage de laboratorio.
2. Deshabilitar el acceso público y forzar HTTPS/TLS 1.2.
3. Configurar un Private Endpoint.
4. Habilitar Defender for Storage y el análisis de malware.
5. Configurar diagnóstico a Log Analytics.

## Ejecución

1. Subir un archivo limpio y confirmar que no hay alerta.
2. Subir la muestra EICAR (entorno aislado) y confirmar la alerta.
3. Intentar acceso anónimo y confirmar el bloqueo.
4. Revisar alertas de acceso anómalo.
5. Exportar evidencia y documentar hallazgos.

## Validaciones

| Prueba | Resultado esperado |
|---|---|
| Archivo limpio | Sin alerta |
| EICAR | Alerta de malware |
| Acceso anónimo | Bloqueo |
| Acceso anómalo | Alerta |

## Cierre

Registrar el estado real. Si no hay cuenta de Storage o Defender habilitado, la práctica queda como diseño.
