# 01 | OAuth 2.0, PKCE y validación de JWT

Este proyecto sigue el recorrido de una autenticación moderna: una aplicación obtiene un token mediante Authorization Code con PKCE y una API valida su firma y sus claims antes de aceptar la solicitud.

## Recorrido técnico

- [Conceptos y contexto](docs/01-conceptos.md)
- [Flujo OAuth 2.0 con PKCE](docs/02-flujo-oauth2-pkce.md)
- [Validación de JWT y JWKS](docs/03-validacion-jwt-jwks.md)
- [Bitácoras del laboratorio](bitacora/)

La API local asociada al laboratorio está documentada en [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure).

## Alcance

El material se centra en el flujo de autorización, la emisión del token y su validación en una API. Los documentos describen el laboratorio; no representan una integración de producción.
