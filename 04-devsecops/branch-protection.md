# 🛡️ Protección de la rama `main` en GitHub

## 🧾 Descripción
Esta práctica implementa una medida DevSecOps esencial: proteger la rama `main` en todos los repositorios del portfolio.  
El objetivo es garantizar que ningún cambio llega a producción sin revisión, aprobación y trazabilidad.

La protección de la rama `main` es un control de seguridad que evita errores, malas prácticas y modificaciones accidentales o no autorizadas.

## 🎯 Objetivo de la práctica
- Asegurar integridad en la rama principal.
- Evitar pushes directos que puedan introducir fallos.
- Obligar a que todo cambio pase por Pull Request.
- Garantizar trazabilidad mediante revisiones y aprobaciones.
- Unificar la política de seguridad en todos los repositorios del portfolio.

## 🛠️ Qué se ha hecho
Se han aplicado reglas de protección en GitHub para la rama `main`, incluyendo:

- Bloqueo de push directo.
- Requerir Pull Request para cualquier cambio.
- Requerir al menos una aprobación.
- Impedir borrar la rama `main`.
- Impedir `force-push`.
- Mantener la rama protegida en todos los repositorios del portfolio.

Estas reglas garantizan que el código evoluciona de forma controlada y segura.

## 🧩 Por qué se ha hecho
Esta práctica forma parte del enfoque DevSecOps del portfolio:

- Introduce controles de seguridad en el flujo de trabajo.
- Alinea el desarrollo con buenas prácticas profesionales.
- Evita errores humanos y cambios no revisados.
- Asegura que el código siempre pasa por validación.
- Refuerza la calidad y la trazabilidad del proyecto.

## 🏁 Conclusión
La protección de la rama `main` queda aplicada y validada en todos los repositorios del portfolio.  
Con esta práctica, el módulo 4 se considera **completamente cerrado**, aportando una base sólida de seguridad en el ciclo de vida del código.

## 📜 Licencia
MIT
