# 07 | DevSecOps y gobernanza del software

> **Estado:** **Validado en CI**. La pipeline completa —build, formato, 10 pruebas, Gitleaks, CodeQL, Trivy SCA, contenedor no-root, Trivy image y Trivy config sobre Bicep— terminó en verde el 2026-10-19 y ha vuelto a pasar desde entonces; la última ejecución es del 2026-10-23. OIDC y despliegue siguen fuera de alcance.

La seguridad del desarrollo no se demuestra con una política escrita, sino con un cambio que no puede entrar si no pasa las pruebas. Este módulo aplica ese criterio sobre EcommerceApi: la rama protegida obliga a revisar, el escaneo de secretos tumba la integración si aparece una credencial, los análisis bloquean el merge y el contenedor se ejecuta sin privilegios.

## Carga de trabajo

Los controles se aplican sobre [EcommerceApi (lab-api-local-azure)](https://github.com/lanuzalorenzo/lab-api-local-azure), el mismo workload del resto del portfolio. El código, el workflow y las plantillas Bicep viven allí; aquí se documenta qué se aplicó y qué se observó.

## Las cuatro prácticas

| # | Práctica | Qué controla | Estado |
|---|---|---|---|
| 01 | [Protección de ramas](practicas/01-proteccion-ramas/README.md) | Que ningún cambio entre sin revisión | **Validado** |
| 02 | [Detección de secretos](practicas/02-secret-scanning/README.md) | Que una credencial no se quede en el historial | **Validado** |
| 03 | [SAST, SCA e IaC](practicas/03-sast-sca-iac/README.md) | Que código, dependencias e infraestructura pasen el análisis | **Validado** |
| 04 | [Pipeline segura](practicas/04-pipeline-security/README.md) | Que cada job tenga el permiso mínimo y los gates bloqueen | **Parcial** |

## Lo que la pipeline no detecta

Los gates cubren lo mecánico: secretos, vulnerabilidades, infraestructura, formato y pruebas. Un mal diseño no deja firma en ningún escaneo y pasa en verde igual. Estos criterios se revisan a mano en cada cambio:

- **Instancias estáticas con estado.** Las dependencias salen del contenedor en `Program.cs`; `TimeProvider` y la factoría de conexiones son singleton porque no guardan estado. Una instancia estática mutable rompería el aislamiento de las pruebas y ningún escaneo la señalaría.
- **Acoplamiento entre capas.** Aquí sí hay gate: `LayerDependencyTests` rompe la compilación si una capa referencia la que no debe.
- **Código que no se puede probar.** Las pruebas arrancan la API real con `WebApplicationFactory`, una base SQLite temporal y un esquema de autenticación de prueba. Si un caso exigiera un servicio externo vivo, el problema está en el diseño, no en la prueba.
- **Optimización prematura y duplicación.** CQRS ligero y outbox entraron con ADR y motivo escrito; sin medición que lo justifique, no entra. `dotnet format` vigila el estilo, no la claridad del código ni la duplicación.

Nada de esto es un control validado: son criterios de revisión de pull request. El estado **Validado en CI** del módulo se apoya en los gates, no en estas comprobaciones.

## Lo que no está

El propietario administrador puede saltarse la protección de rama, y la regla no lo impide: harían falta `enforce_admins` y una cuenta de servicio para las automatizaciones. La autenticación OIDC con Azure está diseñada pero no activa, no hay workflow de despliegue y la pipeline no firma artefactos ni genera SBOM. Son las tres deudas del módulo, escritas como tales.

No hay bitácora. El trabajo quedó en las páginas y en el workflow, y la entrada que había contaba una reorganización de carpetas que ya no existe.
