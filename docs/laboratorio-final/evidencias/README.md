# Índice de evidencias

> **Estado:** 1 evidencia registrada.

Este directorio centraliza las evidencias de ejecución del laboratorio final. Cada entrada debe poder rastrearse hasta un runbook y un entorno concreto. No es un repositorio de capturas sueltas.

## Convención de nombres

```text
YYYY-MM-DD-modulo-practica/
  README.md          # resumen, resultado y limitaciones
  comandos.md        # comandos ejecutados y salida redactada
  artefactos/        # capturas, consultas, JSON o logs redactados
```

Ejemplo:

```text
2026-10-19-10-elk-ingesta/
```

## Contenido mínimo de una evidencia

- Fecha y responsable.
- Runbook utilizado.
- Entorno y alcance.
- Comandos ejecutados.
- Resultado observado: PASS, FAIL o parcial.
- Prueba negativa o de control, si aplica.
- Limpieza realizada.
- Coste, si hubo recursos cloud.
- Limitaciones y lo que no se ha ejecutado.
- Enlaces a artefactos redactados.

## Reglas de redacción

- Sin secretos, tokens, claves ni cadenas de conexión.
- Sin direcciones IP internas, nombres de máquinas ni identificadores reales.
- Sin datos personales.
- Sin capturas que muestren información fuera del alcance.
- Si un dato es necesario para entender la evidencia, se sustituye por un placeholder explícito.

## Índice

| Fecha | Módulo | Práctica | Resultado | Enlace |
|---|---|---|---|---|
| 2026-10-19 | 10 — ELK Stack Security | 01 — Ingestión y normalización · 02 — Kibana | Validado en local | [Ver evidencia](2026-10-19-10-elk-ingesta/README.md) |

Cuando se añada una evidencia, actualiza esta tabla y el README del módulo correspondiente.

## Plantilla

Usa la [plantilla de evidencia](../../../plantillas/evidencia-template.md) como punto de partida.
