# 01 | Detección con KQL y análisis de alertas

Un inicio de sesión fallido no es un incidente; veinte seguidos de un acceso correcto desde otra IP pueden serlo. La detección consiste en escribir esa condición, ejecutarla sobre datos reales y comprobar que la alerta llega con contexto suficiente para investigar. Aquí está el caso y lo que falta para probarlo.

**Referencias:** MCSB LT-1 · NIST SP 800-61

| Pieza | Estado |
|---|---|
| Workspace de Log Analytics con diagnósticos de App Service y Key Vault | Definido en Bicep, sin desplegar |
| Conector de Entra ID para `SigninLogs` | No configurado |
| Consulta de fallos seguidos de acceso correcto | Escrita en el módulo 12, no ejecutada |
| Regla analítica e incidente | No creados |
| Prueba con datos | Pendiente |

El caso: agrupar por usuario, IP y aplicación los fallos de un intervalo corto, y buscar después un acceso correcto desde una IP que no aparecía antes. La consulta existe en el [informe técnico del módulo 12](../../../12-forense-cloud-respuesta/docs/informe-tecnico.md); lo que falta es el workspace con datos y la regla que la convierta en alerta.

Una detección no se valida porque la consulta compile: se valida cuando devuelve el caso sembrado, cuando el ruido es tolerable y cuando el analista puede reconstruir qué pasó con los campos que recibe.

El contexto (usuario, IP, aplicación y hora) decide si la alerta sirve o solo asusta; una consulta sin regla no alerta; y sin conector no hay consulta posible.
