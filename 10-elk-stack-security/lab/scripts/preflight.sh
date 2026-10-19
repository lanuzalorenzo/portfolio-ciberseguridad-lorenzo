#!/usr/bin/env bash
set -u

fail=0

ok() {
  printf '[OK]   %s\n' "$1"
}

warn() {
  printf '[WARN] %s\n' "$1"
}

error() {
  printf '[FAIL] %s\n' "$1"
  fail=1
}

echo "Preflight del laboratorio ELK"
echo "==============================="

if command -v docker >/dev/null 2>&1; then
  ok "Docker instalado: $(docker --version)"
else
  error "Docker no está instalado. Instala Docker Engine y el plugin Compose."
fi

if command -v docker >/dev/null 2>&1; then
  if docker compose version >/dev/null 2>&1; then
    ok "Docker Compose: $(docker compose version --short)"
  else
    error "El plugin 'docker compose' no está disponible."
  fi

  if docker info >/dev/null 2>&1; then
    ok "El daemon de Docker responde."
  else
    error "El daemon de Docker no responde. Revisa permisos o inicia Docker."
  fi
fi

if command -v curl >/dev/null 2>&1; then
  ok "curl disponible."
else
  error "curl no está instalado."
fi

if command -v python3 >/dev/null 2>&1; then
  ok "python3 disponible."
else
  error "python3 no está instalado."
fi

mem_kb=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
mem_gb=$(awk -v k="$mem_kb" 'BEGIN {printf "%.1f", k / 1024 / 1024}')
if [ "$mem_kb" -lt 5500000 ]; then
  warn "Memoria total: ${mem_gb} GB. Se recomiendan al menos 6 GB libres para la pila completa."
else
  ok "Memoria total: ${mem_gb} GB."
fi

free_kb=$(df -Pk . | awk 'NR==2 {print $4}')
free_gb=$(awk -v k="$free_kb" 'BEGIN {printf "%.1f", k / 1024 / 1024}')
if [ "$free_kb" -lt 10485760 ]; then
  warn "Espacio libre: ${free_gb} GB. Se recomiendan al menos 10 GB."
else
  ok "Espacio libre: ${free_gb} GB."
fi

max_map_count=$(sysctl -n vm.max_map_count 2>/dev/null || echo 0)
if [ "$max_map_count" -lt 262144 ]; then
  warn "vm.max_map_count=${max_map_count}. Ejecuta: sudo sysctl -w vm.max_map_count=262144"
else
  ok "vm.max_map_count=${max_map_count}."
fi

if command -v ss >/dev/null 2>&1; then
  busy_ports=$(ss -ltn 2>/dev/null | awk '{print $4}' | grep -E ':(9200|5601)$' || true)
  if [ -n "$busy_ports" ]; then
    warn "Puertos 9200/5601 ya en uso: ${busy_ports}. Detén el proceso o cambia el mapeo."
  else
    ok "Puertos 9200 y 5601 libres."
  fi
else
  warn "No se pudo comprobar 'ss'; verifica manualmente los puertos 9200 y 5601."
fi

echo
if [ "$fail" -ne 0 ]; then
  echo "Preflight con errores. Corrige los [FAIL] antes de continuar." >&2
  exit 1
fi

echo "Preflight correcto. Siguiente: ./scripts/up.sh"
