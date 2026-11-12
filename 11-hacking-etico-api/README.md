# 11 | Hacking ético de APIs

La API del laboratorio está protegida por autenticación, pero eso no dice si un usuario puede leer el pedido de otro ni si el cliente puede fijar el precio de un producto. Este módulo prueba esas dos cosas sobre la API local, con dos identidades y pruebas de integración, y deja escrito qué falta para un pentest real.

## Autorización y ética

Todas las pruebas se ejecutan contra `lab-api-local-azure`, un laboratorio propio. No se escanean dominios, APIs ni tenants de terceros, y no se usan tokens ni datos de clientes. Lo que requiere Azure queda pendiente hasta tener un entorno autorizado. El alcance, los criterios de parada y la retirada de artefactos están en [Alcance y autorización del laboratorio](docs/alcance-y-autorizacion.md).

## Qué se probó

| Frente | Estado | Práctica |
|---|---|---|
| BOLA/BFLA en pedidos | Validado localmente; `POST /api/products` sin rol (H-03) | [01](practicas/01-bola-bfla/README.md) |
| JWT y claims | Configuración revisada; token real pendiente | [02](practicas/02-jwt-claims/README.md) |
| Mass assignment y entrada | Validado localmente | [03](practicas/03-rate-limiting-mass-assignment/README.md) |
| Consumo | Rate limit validado (secuencial y concurrente); límite de 16 KB validado (201 a 16 KB exactos, 413 a 17 KB) | [03](practicas/03-rate-limiting-mass-assignment/README.md) |
| DAST (análisis dinámico) sin autenticar | Parcial: 0 FAIL y 0 WARN, 62 PASS; endpoints tras JWT sin cubrir | [Evidencia](../laboratorio-final/evidencias/2026-11-08-11-api-dast/README.md) |
| Inclusión de ficheros en PHP | Validado localmente en un laboratorio aparte | [Lab](lab/upload-progress-include/README.md) |
| Informe | Documentado | [04](practicas/04-informe-final/README.md) |

La carga de trabajo es [EcommerceApi](https://github.com/lanuzalorenzo/lab-api-local-azure): API .NET 10 con Entra ID, DTOs, aislamiento de pedidos y pruebas de integración. El [runbook](practicas/01-bola-bfla/runbook.md) y la [evidencia de ejecución](../laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md) acompañan a la práctica 01; la práctica 03 tiene su propio [runbook](practicas/03-rate-limiting-mass-assignment/runbook.md) y sus evidencias [secuencial](../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit/README.md), [de carga](../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit-carga/README.md) y [límite de cuerpo](../laboratorio-final/evidencias/2026-11-12-11-api-body-limit/README.md).

El [laboratorio de inclusión de ficheros](lab/upload-progress-include/README.md) no usa la API: es una aplicación PHP mínima, en dos contenedores sin salida a Internet, que separa dos cosas que suelen confundirse. El fallo del motor de PHP conocido como PHP2Shell se corrige actualizando; la cadena de este laboratorio, que escribe en la sesión y ejecuta al incluirla, sobrevive a esa actualización porque el fallo está en el código. Su [evidencia](../laboratorio-final/evidencias/2026-11-02-11-upload-progress-include/README.md) incluye la prueba de control sobre la versión parcheada.

## Límites

Las pruebas usan un esquema de autenticación de test, no tokens de Entra ID; no hay despliegue con APIM ni WAF; y el rate limit se probó con ráfagas secuenciales y concurrentes, sin calibrar contra un SLO. El módulo demuestra el ciclo hallazgo-remediación-regresión en local, no un pentest de producción.
