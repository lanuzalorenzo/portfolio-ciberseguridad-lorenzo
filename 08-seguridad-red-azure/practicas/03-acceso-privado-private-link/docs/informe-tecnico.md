# Informe técnico — Acceso privado a servicios con Private Link

## Estado del documento

Diseño de laboratorio pendiente de ejecución. No se ha seleccionado ni configurado un servicio PaaS.

## Escenario y objetivo

Se propone conectar un servicio PaaS elegido para el laboratorio mediante un Private Endpoint. La práctica debe validar que el nombre del servicio se resuelve y que la conexión funciona desde la red prevista antes de modificar o restringir el acceso público.

## Condiciones previas

- Seleccionar un servicio PaaS disponible y confirmar sus requisitos de Private Link y DNS.
- Definir la VNet y la subred que alojarán el punto de conexión.
- Revisar dependencias de consumidores legítimos antes de restringir el acceso público.
- Confirmar presupuesto, permisos y procedimiento de limpieza antes de aprovisionar recursos.

## Diseño y procedimiento propuesto

1. Documentar el acceso actual y los consumidores previstos, sin incluir identificadores sensibles.
2. Crear el diseño del Private Endpoint y confirmar la zona DNS privada específica del servicio.
3. Configurar la resolución DNS para la red de laboratorio y verificar la ruta de acceso desde un cliente autorizado.
4. Probar nombre, resolución y conectividad privada antes de cambiar el acceso público.
5. Si el servicio y el escenario lo permiten, restringir el acceso público después de validar dependencias; repetir las pruebas desde redes autorizadas y no autorizadas.
6. Registrar resultados y retirar los recursos temporales al terminar.

## Validación planificada

| Caso | Evidencia a recoger | Resultado esperado | Estado |
|---|---|---|---|
| Resolución DNS desde la VNet | Resultado de resolución desde el cliente de prueba | Respuesta coherente con el diseño privado | Pendiente de ejecución |
| Conectividad privada | Prueba desde un cliente autorizado | Servicio accesible por el endpoint privado | Pendiente de ejecución |
| Acceso fuera del alcance | Prueba controlada desde un origen no autorizado, si el escenario lo permite | Acceso conforme a la política elegida | Pendiente de ejecución |
| Restricción del acceso público | Configuración y pruebas antes/después | Sin interrupción de consumidores autorizados | Pendiente de ejecución |

## Referencias y límites

El nombre de la zona DNS y el comportamiento de acceso público dependen del servicio PaaS elegido. Deben verificarse antes de implementar. La asignación MCSB queda pendiente de contrastar con la versión vigente y el control efectivamente probado.