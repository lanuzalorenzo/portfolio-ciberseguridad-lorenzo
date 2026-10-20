# Alcance y autorización del laboratorio

> **Estado:** documentado. Define las condiciones con las que se ejecutan las pruebas del módulo 11. No es una autorización para probar sistemas de terceros.
>
> **Última revisión:** 2026-10-20

## Para qué existe este documento

Una prueba ofensiva se clasifica por quién autoriza, sobre qué activos y con qué límites, no por la herramienta que usa. Este documento fija esas tres cosas para el módulo 11: qué se prueba, qué queda fuera y qué se hace si algo se sale de lo previsto.

En el laboratorio no hay cliente ni contrato: el titular de los sistemas es el propio autor. Por eso la declaración de alcance sustituye a la carta de autorización y cumple la misma función: dejar por escrito, antes de ejecutar, dónde se puede llegar.

## Activos incluidos

| Activo | Qué se prueba | Dónde vive |
|---|---|---|
| `EcommerceApi` en ejecución local | Endpoints de pedidos y productos, validación de entrada, límites | `lab-api-local-azure` |
| Pruebas de integración | Identidades de test A y B, recursos cruzados y regresión | `tests/EcommerceApi.Tests/` |
| Configuración JWT | Validación de emisor, audiencia, firma y claims | Configuración de la API |

## Fuera de alcance

- Cualquier sistema que no sea una instancia local arrancada desde el repositorio propio.
- La red del centro de estudios, la red doméstica, la LAN del autor y el resto de equipos del entorno.
- Tenants, suscripciones, dominios, APIs y datos de terceros.
- Tokens, credenciales o datos de clientes reales.
- Denegación de servicio, persistencia, movimiento lateral y pruebas sobre personas.
- Un despliegue de Azure/APIM sin autorización explícita, presupuesto, grupo de recursos temporal y plan de limpieza.

El entorno se limita a la API levantada por `WebApplicationFactory` o por el contenedor local. Si una prueba necesita Azure, se describe como pendiente hasta que exista un entorno autorizado.

## Condiciones de ejecución

| Condición | Regla del módulo |
|---|---|
| Origen | Máquina local del autor; sin salida hacia redes ajenas |
| Datos | Sintéticos, creados por las propias pruebas |
| Identidades | Dos identidades de test; nunca cuentas reales |
| Técnicas | Peticiones HTTP, análisis de configuración y lectura de código |
| Ritmo | El de la suite de pruebas; sin escaneo masivo ni fuzzing sostenido |
| Ventana | La de la sesión de trabajo, sin necesidad de franja horaria |
| Registro | Cada prueba deja hipótesis, resultado observado y evidencia enlazada |

### Criterios de parada

- La API deja de responder o la suite entra en un estado que no se puede explicar.
- Aparece un dato que no es sintético o una credencial real.
- Una prueba empieza a afectar a un proceso o servicio fuera del repositorio.
- El comportamiento observado no coincide con el documentado y no hay forma de acotarlo.

Ante cualquiera de estos casos: detener la ejecución, anotar el estado, restaurar el entorno y revisar el alcance antes de continuar.

## Evidencias y retirada

- La evidencia se limita a salidas de test, configuración redactada y extractos de código. No se guardan tokens, cabeceras de autorización ni identificadores reales.
- Los pedidos y productos creados por las pruebas viven en el almacén en memoria y desaparecen al reiniciar la API; no se generan cuentas, ficheros ni tareas persistentes.
- Si una prueba necesitara crear un artefacto duradero, se registraría aquí y se retiraría al terminar.
- Los hallazgos se documentan aunque no se puedan remediar en el momento; el estado (`validado`, `parcial`, `pendiente`) refleja lo ejecutado, no lo deseado.

## Límites de esta declaración

- No cubre un pentest real: no hay cliente, contrato, reglas de enfrentamiento pactadas ni seguro de responsabilidad.
- No cubre un despliegue en Azure, ni APIM, ni WAF, ni un tenant con usuarios delegados.
- No convierte el módulo en una auditoría de cumplimiento. La relación con marcos se recoge en [`cumplimiento-normativo/`](../../cumplimiento-normativo/README.md), que distingue control, evidencia y certificación.
- El modelo de fases usado en el módulo es una herramienta de organización del trabajo, no una metodología certificada.

## Referencias

- [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x00-header/): criterio de clasificación de los hallazgos del módulo.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): guía de pruebas de aplicación.
- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final): planificación, descubrimiento, ataque e informe.
- [PTES](http://www.pentest-standard.org/): estructura de un proyecto de pruebas de penetración.
