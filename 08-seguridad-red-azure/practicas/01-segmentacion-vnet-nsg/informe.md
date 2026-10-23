# Informe técnico — Segmentación con VNet y Network Security Groups

## Estado del documento

Diseño de laboratorio pendiente de ejecución. No representa una configuración desplegada ni resultados observados.

## Escenario y objetivo

Se propone diseñar una red virtual de laboratorio con componentes separados por función. El objetivo es limitar los flujos entre capas a las comunicaciones necesarias y comprobar que las reglas de red permiten esos flujos y bloquean los no autorizados.

## Diseño propuesto

1. Definir las capas que realmente necesita el escenario y asignar una subred a cada una.
2. Elaborar una matriz de flujos con origen, destino, propósito, protocolo, puerto y resultado esperado. Dejar sin especificar los puertos que dependan de una carga de trabajo todavía no seleccionada.
3. Determinar dónde se asociarán los NSG y revisar las reglas predeterminadas antes de añadir reglas propias.
4. Añadir únicamente las reglas justificadas por la matriz, con prioridades que no oculten ni contradigan el objetivo de seguridad.
5. Revisar las reglas efectivas y comprobar conectividad desde los componentes de prueba elegidos.

## Validación planificada

| Caso | Evidencia a recoger | Resultado esperado | Estado |
|---|---|---|---|
| Comunicación necesaria entre capas | Resultado de la prueba de conectividad y regla aplicable | Comunicación permitida | Pendiente de ejecución |
| Comunicación no autorizada | Resultado de la prueba y regla que la bloquea | Comunicación denegada | Pendiente de ejecución |
| Revisión de reglas | Matriz de flujos comparada con reglas efectivas | Sin permisos innecesarios ni conflictos no documentados | Pendiente de ejecución |

No se han ejecutado estas pruebas. Registrar el método y el resultado real al completar el laboratorio; no incluir capturas con información sensible.

## Referencias y límites

La selección de controles MCSB queda pendiente de contrastar con la versión vigente y con el diseño final. Los puertos, cargas de trabajo y reglas concretas también dependen del escenario que se apruebe para el laboratorio.