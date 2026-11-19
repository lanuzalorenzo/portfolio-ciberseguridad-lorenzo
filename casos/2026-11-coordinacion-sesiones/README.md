# Repartir una cola de trabajo entre varias sesiones sin que se pisen

Una mesa de taller con un solo juego de llaves se atasca en cuanto dos personas lo cogen a la vez: una de las dos trabaja sin saber que la otra ya está dentro. Algo parecido ocurre cuando varias sesiones de agente —programas que ejecutan tareas sobre los repositorios por su cuenta— comparten una sola cola de trabajo. Sin una regla, dos cogen el mismo ítem (la misma tarea de la cola) y las dos escriben el mismo fichero; el resultado no es más rápido, es un cambio que se pierde.

**In English.** A workshop bench with a single set of keys jams as soon as two people grab it at the same time: one of them works without knowing the other is already inside. Something similar happens when several agent sessions — programs that carry out tasks on the repositories on their own — share a single work queue. Without a rule, two of them pick the same item (the same task in the queue) and both write the same file; the result is not faster, it is a change that gets lost.

> **Estado:** Parcial (2026-11-19). Los invariantes y los mecanismos están descritos y el reparto se ha ejecutado con sesiones simuladas; falta el latido real que refresca un complemento del cliente, el cierre con permiso exclusivo, la prueba con agentes, las carreras de tope e ítem único y la prueba con dos máquinas. El detalle y los artefactos están en el [experimento del 2026-11-19](https://github.com/lanuzalorenzo/lab-ia-aprendizaje/blob/main/docs/experimentos/2026-11-coordinacion-sesiones/README.md).

## 1. La situación

Trabajo con varias sesiones de agente abiertas sobre el mismo espacio de trabajo personal. Cada una puede leer los repositorios, ejecutar comandos y escribir ficheros. La cola de trabajo es única: una lista de ítems que hay que sacar adelante, repartidos por frentes.

El problema aparece en cuanto hay dos sesiones y un solo ítem. La primera lo lee, decide y empieza a escribir. La segunda hace lo mismo porque nada le dice que está ocupado. Al final hay dos versiones del mismo cambio, una encima de la otra, y ninguna sabe que ha pisado a la otra. El fichero queda con lo que escribió la última, no con lo que decidió la persona.

No es un problema de modelos. Es un problema de reparto: quién toca qué y desde cuándo.

## 2. Los invariantes

Las reglas que no se negocian: si una se rompe, el resto no compensa.

1. **Un ítem por sesión.** Una sesión tiene un ítem abierto como máximo. Para cambiar de ítem, suelta el primero.
2. **Se reclama antes de trabajar.** Ninguna sesión lee, decide ni escribe sobre un ítem que no ha reclamado.
3. **El reclamo es atómico.** Se toma creando un directorio: el sistema de archivos crea el nombre o responde que ya existe, sin término medio. No hay un cerrojo global (un único permiso para toda la cola).
4. **El reclamo dice quién y cuándo.** Guarda sesión, ítem, repo, instante y rol.
5. **El rol se fija al tomarlo.** El primero es principal; los demás cierran con un delta (un cambio pequeño que el principal aplica).
6. **Tope de tres sesiones.** No es una estimación de capacidad: es un límite explícito para que el reparto siga siendo legible.
7. **Nadie escribe al arrancar.** Solo el cierre escribe, con un permiso exclusivo; las sesiones secundarias dejan un delta y el cierre principal lo aplica.
8. **El backlog (la lista que ordena el trabajo) no es el cerrojo.** Guarda el punto donde se quedó la última sesión y la bandeja; las colas de ítems viven una por frente.
9. **Nadie deja escrito el siguiente ítem.** El orden se decide al retomar, con la persona.
10. **Un hecho, un dueño.** Cada ítem vive en un solo fichero; los mapas solo enlazan.

Los invariantes 1 a 6 son los que se pueden probar sin un agente. Los demás describen cómo se escribe el trabajo, y esa parte todavía es diseño.

## 3. Los mecanismos

**El reclamo.** Un directorio por ítem en una caché local (el estado que cada sesión guarda en su equipo), fuera de Git. Crearlo es la operación que decide el dueño: si dos sesiones lo intentan a la vez, una lo crea y la otra recibe que ya existe. No hace falta preguntar a nadie más ni mantener un contador compartido. Dentro queda un fichero con los cinco datos del reclamo.

La caché está fuera del historial a propósito: un reclamo es estado de la sesión, no un cambio del repositorio. Git guarda lo que se decide; la caché, quién lo está haciendo ahora.

**El rol.** Quien toma el ítem por primera vez es principal: abre y cierra. Los que llegan después de una liberación cierran con delta, que el principal aplica en su cierre. Así hay un solo cierre por ítem y los demás no compiten por el mismo fichero.

**El latido.** Cada sesión tiene un fichero de latido que un plugin (un complemento que se engancha al cliente y se ejecuta con él) refresca en cada llamada a herramienta. No es un «sigo vivo» que alguien tenga que recordar escribir: se actualiza como efecto de trabajar. Si pasan 45 minutos sin latido, el reclamo se enseña como «sin señal».

**La caducidad no libera.** A los 45 minutos el ítem no vuelve a la cola solo. Se muestra el aviso y decide la persona. Es deliberado: una sesión puede estar esperando una respuesta larga, y liberar el ítem por tiempo entregaría a otra sesión un trabajo a medias. Prefiero un ítem bloqueado y visible a un ítem reclamado por dos.

**El tope.** Tres sesiones como máximo. Al reclamar se cuenta cuántas sesiones distintas tienen un ítem; si ya hay tres, la cuarta no entra. El tope no protege al sistema de caerse: protege la lectura.

**El cierre.** Al terminar, la sesión que cierra toma el cerrojo de cierre, aplica los deltas y escribe el estado. Las demás no escriben: dejan su delta. El cerrojo es lo único global, y solo cubre el momento de escribir, no toda la sesión.

**El orden del día siguiente.** El cierre no deja el siguiente ítem elegido. El orden se decide al retomar, con la persona. Escribirlo antes convertiría una decisión de prioridad en una herencia.

## 4. Modos de fallo y qué evita cada pieza

| Fallo | Qué lo evita | Qué queda sin cubrir |
|---|---|---|
| Dos sesiones cogen el mismo ítem | El directorio se crea una sola vez; la segunda recibe «ocupado» | Si la primitiva (la operación básica del reclamo) no es atómica, las dos creen haberlo creado |
| Dos sesiones escriben el mismo fichero | Un ítem por sesión y un dueño por fichero | Dos ítems distintos que tocan el mismo fichero |
| Una sesión acapara la cola | Tope de tres y un ítem por sesión | Que una sesión haga ítems muy largos |
| Una sesión muere a mitad | El latido deja de refrescarse y el ítem se ve «sin señal» | Nada lo libera solo: hace falta una persona |
| Dos cierres a la vez | Un solo cierre bajo cerrojo; los demás dejan delta | El delta mal descrito por una secundaria |
| El reclamo se pierde en un reinicio | La caché es local y se puede reconstruir | No está probado con la caché vacía a mitad de sesión |
| El orden se hereda sin decidir | Nadie deja escrito el siguiente ítem | Que la persona no retome y la cola se enfríe |

Cada pieza evita un fallo concreto y deja otro abierto; ninguna promete más de lo que hace.

## 5. Verificación y estado

Lo ejecutado está en el experimento enlazado, con fecha, arnés (el guion que ejecuta los casos) y artefactos. Allí se simulan las sesiones con procesos de shell (el intérprete de comandos) y se prueban seis casos y un control: dos sesiones compitiendo por el mismo ítem, el tope de tres, una sesión que intenta coger dos ítems, soltar y volver a coger, un latido de 46 minutos y una sesión que muere con `SIGKILL` después de reclamar. La pasada se repite idéntica.

El experimento también mide la primitiva antes de usarla, porque el diseño descansa en ella. En ese equipo, el `mkdir` del sistema no fue atómico en todas las rondas y el arnés se negó a empezar; con otro binario, la competición se comportó como el diseño espera. La cifra y el detalle están en el experimento: aquí no se copian.

Lo que **no** está medido, y por eso este caso es **Parcial** y no Validado:

- El latido real de un plugin durante llamadas a herramienta de un agente.
- El cierre bajo cerrojo y la aplicación de deltas.
- Dos sesiones de agente reales, no dos procesos de shell.
- El tope y el ítem único cuando dos sesiones llegan exactamente a la vez.
- La caché en red, con dos máquinas.

Un caso de estudio no sube el estado de lo que cuenta. Si el experimento es Parcial, el caso es Parcial y lo dice.

## 6. Lecciones

**La garantía está en la primitiva, no en su nombre.** «Crear un directorio es atómico» es una propiedad del sistema de archivos y del programa que la ejecuta, no una verdad por llamarse `mkdir`. Medirla costó una pasada y evitó publicar un reparto que fallaba en algunas rondas.

**Un cerrojo pequeño por ítem escala mejor que uno global.** El global solo aparece al cerrar, cuando hay que escribir. Todo lo demás se decide con una operación local que no espera a nadie.

**No liberar solo es una propiedad, no un descuido.** Un ítem «sin señal» obliga a mirar. Un ítem liberado por tiempo finge que el trabajo está libre cuando puede estar a medias. La diferencia entre las dos cosas es la que hay entre un aviso y una decisión.

**Fijar el rol al reclamar evita dos cierres.** Si el rol se decidiera al cerrar, dos sesiones podrían creerse principales al mismo tiempo. Fijarlo antes cuesta un campo y ahorra una conversación.

**Escribir solo al cerrar reduce la superficie del conflicto.** Mientras se trabaja, el estado compartido no se toca. El momento delicado es uno, y está protegido.

**Un hecho, un dueño.** Un ítem en un solo fichero, y los mapas que solo enlazan, evitan la pregunta de cuál de las dos copias manda.

Un reparto se puede describir con pocas reglas, pero ninguna vale nada si no se prueba la pieza de la que depende.
