# 09 | Microsoft Sentinel

Detectar no es tener un SIEM instalado: es que los eventos lleguen, que una consulta devuelva lo que importa y que alguien sepa qué hacer con la alerta. Este módulo documenta cómo se montaría esa cadena con Microsoft Sentinel sobre la API del laboratorio. Hoy es un diseño: el workspace y los diagnósticos están en el Bicep, pero Sentinel no está habilitado ni hay datos que consultar.

## Lo que ya está escrito

La plantilla de `lab-api-local-azure` crea un workspace de Log Analytics con 30 días de retención y envía allí los diagnósticos de App Service y Key Vault. No se ha desplegado. Sentinel no aparece en la plantilla: habilitarlo, conectar Entra ID y definir analíticas es trabajo pendiente.

## Las dos piezas

- [Detección con KQL y análisis de alertas](practicas/01-deteccion-kql/README.md) — *diseño*: caso de uso definido y consulta tomada del módulo 12; sin workspace con datos.
- [Automatización de respuesta y contención](practicas/02-automatizacion-respuesta/README.md) — *diseño*: playbook y permisos sin probar; el tabletop del módulo 12 ejecutó a mano un procedimiento parecido.

## Cómo se probaría

Un caso concreto: varios inicios de sesión fallidos seguidos de uno correcto desde una IP distinta. La consulta se ejecutaría sobre `SigninLogs`, se convertiría en regla analítica y se comprobaría que genera un incidente con contexto suficiente. Después, un playbook disparado por ese incidente, con una acción reversible y aprobación humana.

## Límites

Sin workspace desplegado no hay consulta que devuelva nada; sin conector de Entra ID no hay `SigninLogs`; y una regla que no se ha visto saltar no está validada. El módulo 10 sí ejecutó una pila ELK local con eventos sintéticos: sirve para demostrar el patrón de consulta, no para afirmar que Sentinel funciona.
