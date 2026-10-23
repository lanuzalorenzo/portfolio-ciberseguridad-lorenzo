# 13 | Defender CNAPP

> **Estado:** Diseño. CNAPP no se contrata: resulta de activar CSPM y las protecciones de carga, y ninguna de esas piezas está desplegada.
>
> **Referencias:** MCSB DS-1 · EP-1 · PV-2.

CNAPP no es un producto que se encienda. Es lo que aparece cuando la postura del cloud, las imágenes, los clústeres y las cargas en ejecución miran el mismo entorno y se pueden unir en una sola vista. Si las piezas no están, el nombre no significa nada.

Por eso esta práctica es la que más se malinterpreta en una compra: se pide CNAPP como se pide una licencia y se recibe un panel vacío.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Cobertura conjunta | Comprobar que CSPM y las protecciones de carga están activas a la vez | Los planes de 05, 06, 07, 11 y 12 |
| Enlace de un fallo | Seguir un hallazgo desde la plantilla hasta el recurso en ejecución | IaC conectado y workload desplegado |
| Ruta de ataque | Revisar si el explorador une postura y runtime | CSPM con datos suficientes |
| Priorización | Comparar dos hallazgos y justificar cuál va primero | Contexto de exposición real |

Dependen de todas las anteriores, así que ninguna se ha ejecutado.

## Lecciones

- CNAPP es la suma, no otra licencia. Comprarlo como producto suelto es el error más caro del módulo.
- La gracia es seguir un fallo desde la plantilla hasta el runtime. Sin ese enlace es otro panel con otro nombre.
- Un CNAPP sin cargas desplegadas no demuestra nada: la cobertura se mide por lo que ve, no por lo que tiene contratado.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
