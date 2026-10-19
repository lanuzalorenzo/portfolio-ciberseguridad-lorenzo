# Bitácora — Inicio del módulo 11

## Objetivo

Añadir una capa de validación ofensiva sobre la API de referencia, sin salir del laboratorio propio y sin presentar pruebas no ejecutadas como hallazgos reales.

## Contexto y alcance

- API `EcommerceApi` en .NET 10.
- Pruebas locales con `WebApplicationFactory` y dos identidades de test.
- Sin acceso a un tenant de Entra ID con dos usuarios delegados.
- Sin despliegue en APIM ni WAF.

## Trabajo realizado

- Revisión del OWASP API Security Top 10 2023.
- Pruebas de BOLA en lectura y listado de pedidos.
- Prueba de mass assignment en productos.
- Revisión de la configuración JWT.
- Documentación de rate limit y límites de cuerpo.
- Matriz de hallazgos y estado de remediación.

## Resultados

- BOLA mitigado: B recibe `404` al leer el pedido de A.
- Mass assignment mitigado: el `id` del cliente se ignora.
- Validación de entrada: `400` en casos negativos.
- Persisten pendientes: scopes/roles, tokens reales, rate limit bajo carga y pentest desplegado.

## Pendientes o riesgos

- Ejecutar pruebas con dos usuarios delegados reales.
- Añadir políticas de autorización granular.
- Probar `429` y `413` con carga.
- Repetir contra APIM/WAF.

## Aprendizaje

La diferencia entre “autenticado” y “autorizado” es el núcleo del módulo. Una API puede validar JWT correctamente y seguir siendo vulnerable a BOLA si no comprueba la propiedad del recurso.

## Siguiente paso

Integrar las pruebas en CI y ampliar la matriz de roles cuando exista un endpoint administrativo.
