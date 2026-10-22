# Evidencia — [Módulo] / [Práctica]

> **Identificador:** `YYYY-MM-DD-modulo-practica`
>
> **Tipo:** ejecución (ruta A) · decisión (ruta B)
>
> **Resultado:** PASS / FAIL / Parcial
>
> **Runbook:** [enlace]

> **Qué ruta usar.** La **ruta A** registra algo que se ejecutó: comandos, salidas y artefactos. La **ruta B** registra algo que se **decidió**: tabletops, triajes, simulacros y respuestas a incidentes. Las dos comparten contexto, validación, coste, conclusiones y limitaciones; cambia el núcleo (§2–§4). Una evidencia de decisión **no** puede declarar PASS si no tiene acta de decisiones.

## 1. Contexto

- **Fecha:**
- **Responsable:**
- **Entorno:**
- **Alcance:**
- **Datos:** sintéticos / anonimizados
- **Autorización:** [referencia a la autorización de laboratorio, si aplica]

---

# Ruta A — Ejecución

## 2. Comandos ejecutados

```bash
[comando]
```

**Salida observada:**

```text
[salida redactada]
```

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Positiva | [estado] | [estado] | PASS / FAIL |
| Negativa | [estado] | [estado] | PASS / FAIL |

## 4. Artefactos

- [Captura o consulta redactada]
- [Log o JSON redactado]
- [Hash de integridad, si aplica]

---

# Ruta B — Decisión

## 2. El caso

Qué ocurrió, en orden, con hora, fuente y hecho. Separa **hecho observado** de **hipótesis**. Si el ejercicio es un simulacro, dilo aquí y marca las inyecciones del facilitador.

| Hora | Fuente | Hecho |
|---|---|---|
| | | |

## 3. Propuestas y valoración

Cada propuesta se evalúa por separado. No vale «bien» o «mal»: hace falta el motivo y, si falla, la corrección.

| # | Propuesta | Veredicto | Por qué | Corrección |
|---|---|---|---|---|
| 1 | | Válida / Parcial / No válida | | |

**Regla:** una propuesta «parcial» es la más frecuente y la más útil de analizar: suele acertar en el control y fallar en el plano o en el orden.

## 4. Decisión óptima y por qué

La secuencia que el caso pide, con la justificación en cada paso.

| Orden | Acción | Por qué en ese punto |
|---|---|---|
| 1 | | |

**Criterio de contención:** [qué plano se corta primero y por qué].

**Lo que se descartó y por qué:** [alternativas plausibles descartadas].

---

# Común a las dos rutas

## 5. Limpieza

- **Recursos creados:**
- **Recursos eliminados:**
- **Verificación:**

## 6. Coste

- **Estimado:**
- **Real:**
- **Notas:**

## 7. Conclusiones

Qué demuestra la evidencia y qué no.

## 8. Limitaciones y lo no ejecutado

- [Brechas]
- [Dependencias]
- [Trabajo pendiente]

En la ruta B, añade la tabla de **lo que no se hizo y lo que correspondía** (acción · momento · consecuencia). Es la parte que convierte un simulacro en aprendizaje medible.

## 9. Repetición (solo ruta B)

- **¿Se repite?** Sí / No. Cuándo y con qué variable cambiada.
- **Protocolo ciego:** [si el acta previa queda sellada]
- **Métricas de comparación:** [lista corta y medible]

## 10. Revisión de redacción

- [ ] Sin secretos ni tokens.
- [ ] Sin IPs internas ni nombres de máquinas.
- [ ] Sin identificadores reales ni datos personales.
- [ ] Sin capturas fuera de alcance.
- [ ] Enlaces comprobados.
- [ ] Lo no ejecutado está marcado como tal.
