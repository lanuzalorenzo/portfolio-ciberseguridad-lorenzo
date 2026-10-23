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
| Consumo | Rate limit y cuerpo definidos; prueba de carga pendiente | [03](practicas/03-rate-limiting-mass-assignment/README.md) |
| Informe | Documentado | [04](practicas/04-informe-final/README.md) |

La carga de trabajo es [EcommerceApi](https://github.com/lanuzalorenzo/lab-api-local-azure): API .NET 10 con Entra ID, DTOs, aislamiento de pedidos y pruebas de integración. El [runbook](practicas/01-bola-bfla/runbook.md) y la [evidencia de ejecución](../docs/laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md) acompañan a la práctica 01.

## Límites

Las pruebas usan un esquema de autenticación de test, no tokens de Entra ID; no hay despliegue con APIM ni WAF; y el rate limit no se ha calibrado bajo carga. El módulo demuestra el ciclo hallazgo-remediación-regresión en local, no un pentest de producción.
