# 07 | DevSecOps y gobernanza del software

> **Estado:** **Validado en CI**. La pipeline completa —build, formato, las pruebas, Gitleaks, CodeQL, Trivy SCA, contenedor no-root, Trivy image y Trivy config sobre Bicep— terminó en verde el 2026-10-19 y ha vuelto a pasar desde entonces; la última ejecución es del 2026-11-12 y ya genera el SBOM (el inventario de lo que contiene la imagen). OIDC con Azure y despliegue siguen fuera de alcance; la firma keyless y la atestación del SBOM se validaron en el run [43314295991](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/43314295991).

La seguridad del desarrollo no se demuestra con una política escrita, sino con un cambio que no puede entrar si no pasa las pruebas. Este módulo aplica ese criterio sobre EcommerceApi: la rama protegida obliga a pasar por pull request y por los checks, el escaneo de secretos tumba la integración si aparece una credencial, los análisis bloquean el merge y el contenedor se ejecuta sin privilegios. La credencial que restaura los paquetes es de solo lectura y distinta de la identidad con la que se revisa y aprueba.

## Carga de trabajo

Los controles se aplican sobre [EcommerceApi (lab-api-local-azure)](https://github.com/lanuzalorenzo/lab-api-local-azure), el mismo workload del resto del portfolio. El código, el workflow y las plantillas Bicep viven allí; aquí se documenta qué se aplicó y qué se observó.

## Las cinco prácticas

| # | Práctica | Qué controla | Estado |
|---|---|---|---|
| 01 | [Protección de ramas](practicas/01-proteccion-ramas/README.md) | Que ningún cambio entre sin pasar por pull request y por los checks | **Validado** |
| 02 | [Detección de secretos](practicas/02-secret-scanning/README.md) | Que una credencial no salga de la máquina ni se quede en el historial | **Validado** |
| 03 | [SAST, SCA e IaC](practicas/03-sast-sca-iac/README.md) | Que código, dependencias e infraestructura pasen el análisis | **Validado** |
| 04 | [Pipeline segura](practicas/04-pipeline-security/README.md) | Que cada job tenga el permiso mínimo y los gates bloqueen | **Parcial** |
| 05 | [Credenciales de mínimo privilegio](practicas/05-credenciales-minimo-privilegio/README.md) | Que el build use una credencial que solo lea paquetes, separada de la identidad interactiva | **Validado** |

## Un caso de remediación, de principio a fin

La cabecera `Server: Kestrel` salía en todas las respuestas y ningún check la miraba. El [caso de remediación](../laboratorio-final/evidencias/2026-11-09-07-remediacion-server-header/README.md) recorre las cinco piezas que separan un hallazgo de un arreglo: la observación contra el contenedor, la causa en la opción por defecto de Kestrel, el cambio, que hoy vive en `LL.Security 0.3.0` y el consumidor hereda sin línea propia, una prueba de regresión que falla antes y pasa después, y un run de CI fechado que impide que la cabecera vuelva. Lo que no cubre está escrito allí: la capa que pueda ir delante de Kestrel.

### Severidad del hallazgo `Server`

El hallazgo se puntuó con CVSS 3.1 el 2026-11-12: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` → **5,3 (Media)**. El vector describe una divulgación de información de reconocimiento explotable por red, sin autenticación ni interacción: la respuesta revela el producto (`Kestrel`), no su versión. No hay impacto en integridad ni disponibilidad. La justificación, el vector y la puntuación están en la [evidencia del caso](../laboratorio-final/evidencias/2026-11-09-07-remediacion-server-header/README.md#8-severidad-cvss-31).

## Lo que la pipeline no detecta

Los gates cubren lo mecánico: secretos, vulnerabilidades, infraestructura, formato y pruebas. Un mal diseño no deja firma en ningún escaneo y pasa en verde igual. Estos criterios se revisan a mano en cada cambio:

- **Instancias estáticas con estado.** Las dependencias salen del contenedor en `Program.cs`; `TimeProvider` y la factoría de conexiones son singleton porque no guardan estado. Una instancia estática mutable rompería el aislamiento de las pruebas y ningún escaneo la señalaría.
- **Acoplamiento entre capas.** Aquí sí hay gate: `LayerDependencyTests` rompe la compilación si una capa referencia la que no debe.
- **Código que no se puede probar.** Las pruebas arrancan la API real con `WebApplicationFactory`, una base SQLite temporal y un esquema de autenticación de prueba. Si un caso exigiera un servicio externo vivo, el problema está en el diseño, no en la prueba.
- **Optimización prematura y duplicación.** CQRS ligero y outbox entraron con ADR y motivo escrito; sin medición que lo justifique, no entra. `dotnet format` vigila el estilo, no la claridad del código ni la duplicación.
- **Runtime del sistema distinto del de CI.** La pipeline instala el SDK con `actions/setup-dotnet` ([workflow](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)), no con el paquete de Ubuntu; por eso no ejecuta los binarios que enlazan la `libunwind` del sistema. Una condición de carrera en esa biblioteca puede abortar `dotnet build` y `dotnet test` con `0x80131506` sin que ningún gate identifique la causa. La [evidencia del caso](../laboratorio-final/evidencias/2026-11-09-dotnet-clr-libunwind/README.md) reproduce la firma, descarta dos hipótesis y mide la mitigación con `-m:1`.

Nada de esto es un control validado: son criterios de revisión de pull request. El estado **Validado en CI** del módulo se apoya en los gates, no en estas comprobaciones.

## Lo que no está

Cada push a `main` construye la imagen, la publica en GHCR (el registro de imágenes de GitHub) y escanea ese mismo digest (la huella que la identifica) con syft. El `.cdx.json` se genera y se adjunta a la ejecución —[la del 2026-11-12](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/43245455930), 3 842 componentes, imagen `sha256:593a1dde…` y fichero `sha256:abd50ba9…`— y el job que lo genera solo tiene permiso de lectura. Con la firma y la atestación, el inventario queda ligado al digest y a la identidad del workflow; el run [43314295991](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/43314295991) verificó ambas.

La autenticación OIDC con Azure está diseñada pero no activa y no hay workflow de despliegue. Son las dos deudas del módulo, escritas como tales. El propietario tampoco tiene atajo: el ruleset `main` no define actores de bypass, así que pasa por pull request y por los siete checks; la revisión humana no es obligatoria porque nadie puede aprobar su propio cambio.

No hay bitácora. El trabajo quedó en las páginas y en el workflow, y la entrada que había contaba una reorganización de carpetas que ya no existe.
