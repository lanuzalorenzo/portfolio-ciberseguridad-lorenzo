# 11 | Hacking ético de APIs

> **Estado:** validación local ejecutada. Las pruebas de autorización, mass assignment y validación de entrada se ejecutan contra la API local. El pentest contra un despliegue real de Azure/APIM está pendiente.

Este módulo convierte la API de referencia en un objetivo controlado para validar controles del **OWASP API Security Top 10 (2023)**. No es un catálogo de ataques: cada prueba tiene una hipótesis, una evidencia y una remediación verificable.

## Autorización y ética

- Todas las pruebas se ejecutan contra `lab-api-local-azure`, un laboratorio propio.
- No se escanean dominios, APIs ni tenants de terceros.
- No se incluyen tokens, secretos ni datos de clientes.
- Las pruebas que requieren Azure se describen como pendientes hasta disponer de un entorno autorizado.

## Objetivo

- Validar BOLA/IDOR y BFLA en los endpoints de pedidos.
- Revisar la configuración de validación JWT y los claims relevantes.
- Probar *mass assignment*, validación de entrada y consumo de recursos.
- Documentar hallazgos con severidad, evidencia y estado de remediación.

## Carga de trabajo

[**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure): API .NET 10 con autenticación Entra ID, DTOs, aislamiento de pedidos por usuario y pruebas de integración.

## Metodología

1. **Reconocimiento:** inventario de endpoints, métodos y modelos.
2. **Autenticación:** obtención de tokens de laboratorio y verificación de claims.
3. **Autorización:** pruebas con dos identidades (A y B) y recursos cruzados.
4. **Entrada:** mass assignment, tipos, límites y validación.
5. **Consumo:** rate limit y tamaño de petición.
6. **Remediación:** cambio de código, prueba de regresión y evidencia.
7. **Informe:** hallazgo, severidad, impacto, evidencia y estado.

## Prácticas

- [BOLA/BFLA: aislamiento de pedidos](practicas/01-bola-bfla/README.md) — *validado localmente*
- [Endurecimiento de JWT y claims](practicas/02-jwt-claims/README.md) — *configuración revisada; token real pendiente*
- [Rate limiting y mass assignment](practicas/03-rate-limiting-mass-assignment/README.md) — *validado localmente; rate limit manual pendiente*
- [Informe final y matriz OWASP API Top 10](practicas/04-informe-final/README.md) — *documentado*

## Relación con otros módulos

- [01 — OAuth 2.0, PKCE y JWT](../01-seguridad-azure/README.md): fundamento de autenticación.
- [07 — DevSecOps](../07-devsecops/README.md): SAST/SCA y pruebas en CI.
- [08 — Redes Azure](../08-seguridad-red-azure/README.md): exposición y Private Endpoints.
- [12 — Forense cloud](../12-forense-cloud-respuesta/README.md): evidencia y respuesta.

## Alcance

El módulo demuestra pruebas de seguridad de API sobre un laboratorio local y deja explícito qué requiere un despliegue real (APIM, WAF, tokens de Entra, dos usuarios delegados). No se presenta como un pentest de producción.
