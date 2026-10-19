# NN | Nombre de la práctica

<!-- Badges solo si reflejan estados reales y verificados. -->

> **Uso:** copia esta plantilla en `NN-modulo/practicas/NN-practica/README.md`; los enlaces de la sección final son relativos a esa carpeta.
>
> **Estado:** Validado / Parcial / Runbook preparado / Diseño / Pendiente
>
> **Última revisión:** YYYY-MM-DD

## 1. Descripción del escenario y objetivo de seguridad

**Escenario:** [Entorno, rol de la API o servicio y necesidad técnica.]

**Objetivo de seguridad y vectores de riesgo:** [Riesgo mitigado según OWASP, MITRE ATT&CK o CIS.]

**Alcance:** [Componentes incluidos, límites del laboratorio y prerrequisitos.]

> [!NOTE]
> Laboratorio realizado en entorno controlado. La información sensible ha sido redactada.

## 2. Arquitectura, componentes y flujo de datos

| Componente | Rol en la arquitectura | Configuración de seguridad clave |
|---|---|---|
| [API .NET, Entra ID, VNet, Key Vault] | [Responsabilidad en el flujo] | [Control implementado: OIDC, JWT, TLS, RBAC] |

**Diagrama:** [Enlace a `diagrams/arquitectura.mmd`, si existe.]

## 3. Implementación de controles DevSecOps y Cloud Security

| Control | Implementación | Nivel de automatización | Referencia / Estándar |
|---|---|---|---|
| [Control aplicado] | [Detalle técnico o fragmento de código/política] | [CI/CD, Azure Policy, IaC o manual] | [OWASP / MCSB / CIS / ENS] |

**Artefactos relacionados:** [Enlaces a scripts, código, workflows o informes técnicos.]

## 4. Validación o pruebas de seguridad realizadas

| Prueba | Herramienta / Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| [Prueba ejecutada] | [Comando, test automatizado o curl] | [Comportamiento esperado] | [PASS / FAIL / Pendiente de entorno] |

> [!WARNING]
> No des por superada ninguna comprobación que no se haya ejecutado y verificado.

## 5. Lecciones aprendidas, buenas prácticas y alineación normativa

| Marco o estándar | Dominio o control | Aplicación y lección aprendida |
|---|---|---|
| [MCSB / ENS / OWASP API / NIST] | [Identificador de control] | [Conclusión práctica respaldada por la prueba] |

- **Decisión arquitectónica clave:** [Razón técnica de la solución adoptada frente a alternativas.]
- **Perspectiva DevSecOps:** [Cómo se equilibra la seguridad del control con la velocidad de desarrollo y entrega.]
- **Mejora identificada:** [Limitación actual o siguiente paso de evolución.]

## Enlaces

- Runbook: [runbook.md](runbook.md)
- Evidencias: [evidencias/](evidencias/)
- Bitácora: [bitacora/](bitacora/) (si aplica)
