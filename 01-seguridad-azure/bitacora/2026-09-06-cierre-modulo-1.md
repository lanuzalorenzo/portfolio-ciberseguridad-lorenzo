# Bitácora — 2026-09-06: Cierre del Módulo 01

**Objetivo:** Consolidar el módulo, organizar el trabajo y dar por cerrado el bloque inicial de identidad.

Hoy me he dedicado a tareas de organización y reflexión. He vuelto a entrar al tenant de Entra ID para revisar que el App Registration quedó limpio, asegurándome de que los redirect URIs y scopes estaban correctamente definidos y no había basura de mis primeras pruebas fallidas.

Tomé una decisión importante de arquitectura para el portfolio: el código de la API (.NET) y los scripts de prueba del laboratorio "ensuciaban" este repositorio, cuyo objetivo es ser un portfolio de alto nivel y arquitectura cloud. Por tanto, he empaquetado todo el código práctico en un nuevo repositorio externo (`lab-api-local-azure`) y he dejado este repositorio exclusivamente para la documentación técnica, los diagramas y el registro de bitácoras.

El módulo 1 queda cerrado. He logrado el objetivo: comprender y probar un flujo completo y seguro de identidad en Azure. Listo para avanzar.
