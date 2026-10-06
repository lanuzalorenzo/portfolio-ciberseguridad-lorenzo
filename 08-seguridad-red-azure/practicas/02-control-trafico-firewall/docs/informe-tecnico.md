# Informe técnico — Control centralizado de tráfico con Azure Firewall

## Estado del documento

Diseño de laboratorio pendiente de ejecución. Azure Firewall no se ha desplegado y no hay resultados observados.

## Escenario y objetivo

Se propone evaluar el control de salida de una o más subredes mediante Azure Firewall y rutas definidas por el usuario. La práctica debe demostrar una decisión de tráfico permitida y otra denegada, sin aplicar reglas genéricas que no correspondan a una carga de trabajo identificada.

## Condiciones previas

- Confirmar presupuesto, disponibilidad regional, permisos y requisitos del servicio antes de aprovisionar recursos.
- Seleccionar los destinos de prueba y documentar por qué son necesarios o deben bloquearse.
- Definir la topología y las rutas afectadas para evitar desviar tráfico ajeno al laboratorio.
- Acordar el procedimiento de limpieza y comprobar que la configuración no deja recursos facturables activos.

## Diseño y procedimiento propuesto

1. Dibujar el flujo desde la subred de origen hasta el destino de prueba e identificar dónde se aplicará la inspección.
2. Diseñar las políticas de tráfico para los casos permitidos y denegados, con el alcance mínimo necesario.
3. Asociar las rutas únicamente a las subredes incluidas en el laboratorio y revisar el camino efectivo.
4. Aplicar la configuración solo después de aprobar las condiciones previas y el coste.
5. Ejecutar las pruebas controladas, revisar los registros disponibles si se habilitaron y retirar los recursos al finalizar.

## Validación planificada

| Caso | Evidencia a recoger | Resultado esperado | Estado |
|---|---|---|---|
| Tráfico permitido | Prueba de conectividad y regla que coincide | Acceso al destino definido | Pendiente de ejecución |
| Tráfico denegado | Prueba de conectividad y regla que coincide | Acceso bloqueado | Pendiente de ejecución |
| Ruta de salida | Revisión de la ruta efectiva desde la subred | Tráfico dirigido según el diseño | Pendiente de ejecución |
| Limpieza | Inventario de recursos del laboratorio tras finalizar | Recursos temporales retirados | Pendiente de ejecución |

## Referencias y límites

No se asigna todavía un identificador MCSB. La correspondencia se debe verificar frente a la versión vigente y las capacidades finalmente probadas. No se incluyen comandos ni instrucciones de despliegue hasta que se soliciten y se confirme el diseño.