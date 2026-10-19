#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [ "${1:-}" != "--yes" ]; then
  echo "Este comando elimina los contenedores y el volumen 'esdata' con todos los datos del laboratorio." >&2
  echo "Ejecuta: ./scripts/down.sh --yes" >&2
  exit 1
fi

docker compose down -v --remove-orphans
echo "Laboratorio eliminado. El volumen 'esdata' ya no existe."
