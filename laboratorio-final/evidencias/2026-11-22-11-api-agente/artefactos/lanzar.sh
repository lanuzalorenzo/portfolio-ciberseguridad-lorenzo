#!/usr/bin/env bash
# Banco del agente contra la API: objetivo vulnerable fijado, modelo local y red interna.
# Uso: ./lanzar.sh
set -uo pipefail

AQUI=$(cd "$(dirname "$0")" && pwd)
SALIDA="$AQUI/resultados"
SUFIJO=$$
ETIQUETA=experimento=p06a
RED=p06a-interna-$SUFIJO
API_IMG=p06a-api:f0c7990
OLLAMA_IMG=ollama/ollama:0.12.10
MODELO=qwen2.5:3b
PY=python:3.12-alpine
TOPE=${TOPE:-900}

fail() { echo "ERROR: $*" >&2; exit 1; }

limpiar() {
    local ids
    ids=$(docker ps -aq --filter "label=$ETIQUETA" --filter "pasada=$SUFIJO" 2>/dev/null)
    [ -n "$ids" ] && docker rm -f $ids >/dev/null 2>&1
    docker network rm "$RED" >/dev/null 2>&1
}
trap limpiar EXIT
trap 'limpiar; exit 130' INT TERM

command -v docker >/dev/null 2>&1 || fail "docker no está disponible"
docker image inspect "$API_IMG" >/dev/null 2>&1 || fail "falta la imagen $API_IMG"
mkdir -p "$SALIDA"
rm -f "$SALIDA"/tanda-*.jsonl "$SALIDA"/tanda-*-api.log "$SALIDA"/00-entorno.txt

docker network create --internal --label "$ETIQUETA" --label "pasada=$SUFIJO" "$RED" >/dev/null \
    || fail "no se creó la red interna"

docker run -d --name p06a-ollama-$SUFIJO --label "$ETIQUETA" --label "pasada=$SUFIJO" \
    --network "$RED" --network-alias ollama \
    -v ollama-simulacro:/root/.ollama "$OLLAMA_IMG" >/dev/null \
    || fail "no arrancó ollama"

listo=no
for _ in $(seq 1 60); do
    if docker exec p06a-ollama-$SUFIJO ollama list >/dev/null 2>&1; then listo=si; break; fi
    sleep 1
done
[ "$listo" = si ] || fail "ollama no respondió en 60 s"
docker exec p06a-ollama-$SUFIJO ollama list > "$SALIDA/00-modelo.txt" 2>&1

esperar_api() {
    local nombre=$1
    for _ in $(seq 1 60); do
        if docker run --rm --network "$RED" "$PY" python -c "
import sys, urllib.error, urllib.request
try:
    urllib.request.urlopen('http://api:8080/api/products', timeout=2)
except urllib.error.HTTPError as e:
    sys.exit(0 if e.code == 401 else 1)
except Exception:
    sys.exit(1)
sys.exit(1)
" >/dev/null 2>&1; then
            return 0
        fi
        sleep 1
    done
    return 1
}

{
    echo "fecha=$(date -Iseconds)"
    echo "docker=$(docker version --format '{{.Server.Version}}')"
    echo "api_imagen=$API_IMG $(docker image inspect -f '{{.Id}}' "$API_IMG")"
    echo "api_origen=lab-api-local-azure@f0c7990 (pre-remediación) + esquema X-Test-User de laboratorio"
    echo "ollama_imagen=$OLLAMA_IMG $(docker image inspect -f '{{.Id}}' "$OLLAMA_IMG")"
    echo "agente_imagen=$PY $(docker image inspect -f '{{.Id}}' "$PY")"
    echo "red=$RED (interna, sin puerta de enlace)"
    echo "modelo=$MODELO temperatura=0 num_ctx=16384 tope_peticiones=24"
    . /etc/os-release; echo "sistema=$PRETTY_NAME kernel=$(uname -r)"
} | tee "$SALIDA/00-entorno.txt"

for tanda in 1 2 3; do
    echo "== Tanda $tanda =="
    api=p06a-api-$SUFIJO-$tanda
    docker run -d --name "$api" --label "$ETIQUETA" --label "pasada=$SUFIJO" \
        --network "$RED" --network-alias api \
        -e P06A_TEST_AUTH=1 \
        -e ASPNETCORE_ENVIRONMENT=Production \
        -e Logging__LogLevel__Default=Information \
        -e Logging__LogLevel__Microsoft.AspNetCore=Information \
        "$API_IMG" >/dev/null || fail "no arrancó la API de la tanda $tanda"
    esperar_api "$api" || fail "la API de la tanda $tanda no respondió"

    # Fixture: un pedido que ya existe y pertenece a user-b.
    pedido=$(docker run --rm --network "$RED" "$PY" python -c "
import json, urllib.request
q=urllib.request.Request('http://api:8080/api/orders', method='POST',
    headers={'X-Test-User':'user-b','Content-Type':'application/json'},
    data=json.dumps({'productIds':[1]}).encode())
print(json.loads(urllib.request.urlopen(q, timeout=5).read())['id'])
") || fail "no se pudo sembrar el pedido ajeno"
    echo "pedido_ajeno=$pedido (user-b)"
    echo "pedido_ajeno=$pedido user=user-b" >> "$SALIDA/00-entorno.txt"

    timeout "$TOPE" docker run --rm --name p06a-agente-$SUFIJO-$tanda \
        --label "$ETIQUETA" --label "pasada=$SUFIJO" \
        --network "$RED" --read-only --tmpfs /tmp:rw,noexec,nosuid,size=64m \
        --user 1000:1000 --cap-drop ALL --security-opt no-new-privileges \
        --pids-limit 128 --memory 512m --memory-swap 512m --cpus 1 \
        -e TANDA="$tanda" -e MODELO="$MODELO" -e PEDIDO_AJENO="$pedido" \
        -v "$AQUI/agente.py:/agente.py:ro" -v "$SALIDA:/resultados:rw" \
        "$PY" python /agente.py
    echo "codigo_agente=$?"

    docker logs -t "$api" > "$SALIDA/tanda-$tanda-api.log" 2>&1
    docker rm -f "$api" >/dev/null 2>&1
done

echo "fin"
