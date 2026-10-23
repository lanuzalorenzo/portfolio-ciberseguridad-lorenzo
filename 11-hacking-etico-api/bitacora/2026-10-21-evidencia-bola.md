# Bitácora — Evidencia local de BOLA/BFLA (módulo 11)

## Objetivo

Cerrar la validación local del módulo 11 con una evidencia registrada, reutilizable y enlazada desde el índice del laboratorio final, sin ampliar el alcance a Azure.

## Contexto y alcance

- Repositorio del workload: `lab-api-local-azure`, commit `b66028a`.
- Entorno: Ubuntu 26.04.1 LTS y .NET SDK 10.0.113, sin recursos cloud.
- Pruebas: `WebApplicationFactory` con dos identidades de test (`X-Test-User`).
- Fuera de alcance: tokens reales de Entra ID, APIM, WAF y pentest desplegado.

## Trabajo realizado

- Revisión del alcance y de la autorización del módulo antes de ejecutar.
- Ejecución de la suite completa (10 pruebas) y de la suite filtrada de pedidos (4 pruebas).
- Revisión de la superficie administrativa con `grep` sobre los controladores.
- Redacción de un `runbook.md` con prerrequisitos, comandos, validación, limpieza y limitaciones.
- Creación de la evidencia `laboratorio-final/evidencias/2026-10-21-11-api-bola/` con salidas redactadas.
- Actualización del índice de evidencias, del README del módulo y de los estados del laboratorio.

## Resultados

- 10 de 10 pruebas superadas; 4 de 4 en el filtro de pedidos.
- BOLA: el propietario obtiene `200` y otro usuario `404` sobre el mismo pedido.
- Listado: A ve 1 pedido y B ve 0.
- Mass assignment: el `id` enviado por el cliente se ignora.
- BFLA: no hay endpoints administrativos ni políticas de rol.
- Control: productos sin token devuelve `401`.

## Pendientes o riesgos

- El esquema de test no valida firma, emisor, audiencia ni expiración del JWT.
- Rate limiting y consumo de recursos siguen sin prueba manual.
- Falta repetir la validación contra un despliegue autorizado con dos usuarios delegados.
- `POST /api/products` solo exige autenticación: cualquier usuario válido puede alterar el catálogo. Se declara en H-03 del informe final.
- La evidencia caduca si cambia el commit del workload; hay que repetir el runbook.

## Aprendizaje

Una prueba de autorización vale lo que vale su evidencia: el nombre de la prueba y la aserción no bastan si no se registran el commit, el entorno y la salida. También quedó visible una imprecisión previa: la tabla de la práctica declaraba una prueba de «pedido inexistente» que no existía; se corrigió a «no ejecutado» en lugar de mantener un PASS sin respaldo.

## Siguiente paso

Convertir el tabletop forense del módulo 12 en runbook ejecutable y registrar su acta para cerrar el gate de la Fase 0 con tres evidencias locales.
