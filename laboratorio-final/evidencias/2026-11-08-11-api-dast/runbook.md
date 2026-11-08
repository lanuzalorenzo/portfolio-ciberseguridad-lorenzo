# Runbook — Baseline DAST sin autenticar

Prerrequisitos, comandos y límites para repetir el escaneo pasivo de la superficie anónima de EcommerceApi.

## Prerrequisitos y permisos

- Docker 29.x y acceso a `ghcr.io` para descargar ZAP una vez.
- Clon de `lab-api-local-azure`; los comandos suponen `$HOME/lab-api-local-azure`, ajusta la ruta si es otra.
- Imagen local `ecommerce-api:local` construida desde el árbol que se quiere medir. Si hay que reconstruirla, `GITHUB_TOKEN` en el entorno para el feed de paquetes.
- Sin recursos cloud, sin tenant y sin credenciales. Solo se escanea la superficie anónima.

## Variables y nombres

- API: `http://localhost:8080`.
- Directorio de trabajo: `~/zap-dast`.
- Imagen de ZAP fijada por digest: `ghcr.io/zaproxy/zaproxy@sha256:9624669db72f54d86c4b46a7064518bd9bf79d8c61a4c31befa9923489f328af` (2.17.0).

## Comandos

```bash
cd "$HOME/lab-api-local-azure"
docker compose up -d
sleep 3
curl -i http://localhost:8080/health

mkdir -p ~/zap-dast && cd ~/zap-dast
docker run --rm --network host -v "$PWD:/zap/wrk:rw" \
  ghcr.io/zaproxy/zaproxy@sha256:9624669db72f54d86c4b46a7064518bd9bf79d8c61a4c31befa9923489f328af \
  zap-baseline.py -t http://localhost:8080/health \
  -r zap-report.html -J zap-report.json -w zap-report.md
```

## Resultado esperado

- `/health` responde `200` con `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy` y `Permissions-Policy`.
- ZAP termina con `FAIL-NEW: 0`, `WARN-NEW: 0` y exit `0`.
- El aviso `Job spider error accessing URL http://localhost:8080/ status code returned : 404` es esperado: la raíz no existe.

## Evidencia a capturar

- Los informes HTML, JSON y Markdown de ZAP.
- La salida de consola con el resumen y los PASS.
- Versiones y digests en `artefactos/entorno.txt`.

## Prueba negativa o de control

**Pendiente.** Falta escanear un objetivo vulnerable conocido y comprobar que ZAP lo detecta, para demostrar que el `0 FAIL` no es un escáner mudo.

## Limpieza

```bash
docker rm -f api-dast
docker volume rm api-dast-data
cd "$HOME/lab-api-local-azure" && docker compose down
```

## Coste y tiempo

- 15–20 min, incluida la descarga de la imagen la primera vez.
- Sin coste cloud.

## Limitaciones

- Solo cubre la superficie anónima; los endpoints con JWT no se prueban.
- No se ejecutó escaneo activo ni autenticado.
