# Laboratorio PKCE — API local

> **Estado:** Validado (2026-11-26). Ejecutado contra el tenant del laboratorio; la evidencia está en [`practicas/01-pkce-manual/evidencias/2026-11-26-01-pkce-manual/`](../../practicas/01-pkce-manual/evidencias/2026-11-26-01-pkce-manual/README.md).
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
  - API que exponga el scope `acceso`.

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

- Requiere un tenant real; la ejecución del 2026-11-26 está en la evidencia de la práctica.
- El CI del repositorio comprueba la carga del módulo y audita las dependencias; no prueba el flujo.
- La seguridad de la API es de laboratorio: HTTP local, sin TLS.
