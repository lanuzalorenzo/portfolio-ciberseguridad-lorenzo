# Laboratorio PKCE — API local

> **Estado:** Parcial. Código y documentación consolidados desde `lab-azuread-oauth2-pkce-api`; la ejecución estandarizada queda pendiente de un tenant de laboratorio.
>
> **Práctica:** [01 — PKCE manual con cliente público](../../practicas/01-pkce-manual/README.md) · **Runbook:** [runbook.md](../../practicas/01-pkce-manual/runbook.md).

API local en Node.js/Express que valida tokens JWT emitidos por Microsoft Entra ID usando JWKS y protege el endpoint `/api/products`. El flujo de autenticación es OAuth2 Authorization Code con PKCE y cliente público, sin secreto de cliente.

## Estructura

```text
lab/pkce/
├── .env.example
├── .gitignore
├── package.json
├── package-lock.json
├── server.js
├── utils/
│   └── validateToken.js
└── scripts/
    ├── generate-pkce.sh
    ├── exchange-token.sh
    └── call-api.sh
```

## Requisitos

- Node.js 18 o superior y npm.
- `curl` y `openssl`.
- Un tenant de Microsoft Entra ID con dos registros de aplicación:
  - cliente público con redirect URI `http://localhost/callback`;
  - API que exponga el scope `access_as_user`.

## Puesta en marcha

```bash
cd 01-seguridad-azure/lab/pkce
npm install
cp .env.example .env
# edita .env con los valores del tenant; no lo subas a Git
npm start
```

Endpoints:

- `http://localhost:4010/health`
- `http://localhost:4010/api/products` (protegido)

## Validación

El middleware `utils/validateToken.js` comprueba:

- firma RS256/RS384/RS512 contra JWKS;
- `iss` contra `VALID_ISSUERS` o `AZURE_ISSUER`;
- `aud` contra `API_AUDIENCE`, `AZURE_API_CLIENT_ID` o `AZURE_CLIENT_ID`;
- `exp` y `nbf`.

La prueba negativa es llamar a `/api/products` sin token (`401`) o con un token manipulado (`401`).

## Limitaciones

- Requiere un tenant real para ejecutar el flujo completo; no se ha reejecutado con el estándar de evidencia actual.
- No hay tests automatizados ni CI en este laboratorio.
- La seguridad de la API es de laboratorio: HTTP local, sin TLS.
