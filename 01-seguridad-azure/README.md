# 01 | OAuth 2.0, PKCE y validación de JWT

> **Estado:** validado en laboratorio. Flujo y validación documentados; la API de referencia aplica validación JWT y autorización por usuario. La práctica de PKCE manual conserva una ejecución histórica y su evidencia estandarizada queda como **Parcial**.

Este módulo analiza e implementa la capa de **Seguridad en Aplicaciones (AppSec) e Identidad** para APIs REST: el flujo completo de autenticación moderna donde una aplicación cliente obtiene un token mediante Authorization Code con PKCE y una API empresarial valida criptográficamente su firma y sus *claims* antes de autorizar cualquier operación de negocio.

## Carga de trabajo asociada

La API empresarial utilizada para validar estos flujos es [**EcommerceApi (lab-api-local-azure)**](https://github.com/lanuzalorenzo/lab-api-local-azure), desarrollada en **.NET (C#)** con integración nativa del middleware `JwtBearer` contra los endpoints de **Microsoft Entra ID (v2.0)**.

## Recorrido técnico

- [Conceptos y contexto](docs/01-conceptos.md): Fundamentos de tokens de acceso, delegated scopes y roles.
- [Flujo OAuth 2.0 con PKCE](docs/02-flujo-oauth2-pkce.md): Obtención segura de tokens sin secretos en clientes públicos.
- [Validación de JWT y JWKS](docs/03-validacion-jwt-jwks.md): Verificación criptográfica de firma asimétrica contra el endpoint Discovery de Microsoft Entra ID.
- [Bitácoras del laboratorio](bitacora/): Registro cronológico de diseño, pruebas y decisiones técnicas.

## Prácticas

- [01 — PKCE manual con cliente público](practicas/01-pkce-manual/README.md): flujo Authorization Code + PKCE, canje de token y validación JWKS con un cliente público. Estado **Parcial**: runbook preparado y evidencia pendiente de reejecución con tenant.

## Alcance y rigor técnico

El material documenta el protocolo de autorización, la emisión de tokens y la lógica de validación en la API. Los documentos describen un entorno de laboratorio técnico controlado y reproducible; las credenciales y datos de tenant han sido redactados.

> **Nota sobre el historial:** antes de migrar la API a `lab-api-local-azure`, este repositorio contenía su documentación. Algunos ejemplos históricos usan `Authorization: Bearer $TOKEN` y cabeceras JWT truncadas con `...`. Son marcadores, no credenciales válidas. Se conservan por trazabilidad y están cubiertos por la allowlist acotada de `.gitleaks.toml`; no se reescribió el historial. Si alguna vez se usó un token real, debe rotarse.

