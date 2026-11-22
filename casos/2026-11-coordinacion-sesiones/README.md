# Repartir una cola de trabajo entre varias sesiones sin que se pisen

Una mesa de taller con un solo juego de llaves se atasca en cuanto dos personas lo cogen a la vez: una de las dos trabaja sin saber que la otra ya está dentro. Algo parecido ocurre cuando varias sesiones de agente —programas que ejecutan tareas sobre los repositorios por su cuenta— comparten una sola cola de trabajo. Sin una regla, dos cogen el mismo ítem (la misma tarea de la cola) y las dos escriben el mismo fichero; el resultado no es más rápido, es un cambio que se pierde.

**In English.** A workshop bench with a single set of keys jams as soon as two people grab it at the same time: one of them works without knowing the other is already inside. Something similar happens when several agent sessions — programs that carry out tasks on the repositories on their own — share a single work queue. Without a rule, two of them pick the same item (the same task in the queue) and both write the same file; the result is not faster, it is a change that gets lost.

> **Estado:** Parcial (2026-11-19). Los invariantes y los mecanismos están descritos; el reparto se ejecutó con sesiones simuladas. Falta el latido real del plugin, el cierre bajo cerrojo medido con un guion de casos, la prueba con agentes, las carreras de tope e ítem único y dos máquinas. El detalle y los artefactos están en el [experimento del 2026-11-19](https://github.com/lanuzalorenzo/lab-ia-aprendizaje/blob/main/docs/experimentos/2026-11-coordinacion-sesiones/README.md).

## 1. La situación

Trabajo con varias sesiones de agente abiertas sobre el mismo espacio de trabajo personal. Cada una puede leer los repositorios, ejecutar comandos y escribir ficheros. La cola de trabajo es única: una lista de ítems que hay que sacar adelante, repartidos por frentes.

El problema aparece en cuanto hay dos sesiones y un solo ítem. La primera lo lee, decide y empieza a escribir. La segunda hace lo mismo porque nada le dice que está ocupado. Al final hay dos versiones del mismo cambio, una encima de la otra, y ninguna sabe que ha pisado a la otra. El fichero queda con lo que escribió la última, no con lo que decidió la persona.

No es un problema de modelos. Es un problema de reparto: quién toca qué y desde cuándo.

## 2. Los invariantes

Las reglas que no se negocian: si una se rompe, el resto no compensa.

1. **Un ítem por sesión.** Una sesión tiene un ítem abierto como máximo. Para cambiar de ítem, suelta el primero.
2. **Se reclama antes de trabajar.** Ninguna sesión lee, decide ni escribe sobre un ítem que no ha reclamado.
3. **El reclamo es atómico.** Se toma creando un directorio: el sistema de archivos crea el nombre o responde que ya existe, sin término medio. Ningún cerrojo cubre el trabajo sobre el ítem.
4. **El reclamo dice quién y cuándo.** Guarda sesión, ítem, repo e instante.
5. **Tope de tres sesiones.** No es una estimación de capacidad: es un límite explícito para que el reparto siga siendo legible.
6. **Nadie escribe el estado compartido mientras trabaja.** Solo se escribe al cerrar, y un cierre a la vez, bajo el cerrojo de cierre.
7. **El backlog (la lista que ordena el trabajo) no es el cerrojo.** Guarda el punto donde se quedó la última sesión y la bandeja; las colas de ítems viven una por frente.
8. **Nadie deja escrito el siguiente ítem.** El orden se decide al retomar, con la persona.
9. **Un hecho, un dueño.** Cada ítem vive en un solo fichero; los mapas solo enlazan.

Los cinco primeros son los que se pueden probar sin un agente. El resto describe cómo se escribe el trabajo: el cerrojo de cierre se usa en cada cierre, pero no está medido con un arnés (el guion que ejecuta los casos).

## 3. Los mecanismos

**El reclamo.** Un directorio por ítem en una caché local (el estado que cada sesión guarda en su equipo), fuera de Git. Crearlo decide al dueño: si dos lo intentan a la vez, una lo crea y la otra recibe que ya existe. Solo al contar y crear se toma un cerrojo breve, que no cubre trabajo. Dentro quedan sesión, repo e instante; el ítem es el nombre del directorio.

La caché está fuera del historial a propósito: un reclamo es estado de la sesión, no un cambio del repositorio. Git guarda lo que se decide; la caché, quién lo está haciendo ahora.

**El latido.** Cada sesión tiene un fichero de latido que un plugin (un complemento que se engancha al cliente y se ejecuta con él) refresca en cada llamada a herramienta. No es un «sigo vivo» que alguien tenga que recordar escribir: se actualiza como efecto de trabajar. Si pasan 45 minutos sin latido, el reclamo se enseña como «sin señal».

**La caducidad no libera.** A los 45 minutos el ítem no vuelve a la cola solo. Se muestra el aviso y decide la persona. Es deliberado: una sesión puede estar esperando una respuesta larga, y liberar el ítem por tiempo entregaría a otra sesión un trabajo a medias. Prefiero un ítem bloqueado y visible a un ítem reclamado por dos.

**El tope.** Tres sesiones como máximo. Al reclamar se cuentan las sesiones con un ítem y señal reciente; si ya hay tres, la cuarta no entra. El tope no protege al sistema de caerse: protege la lectura.

**El cierre.** Al terminar, la sesión toma el cerrojo de cierre, escribe lo suyo —su ítem, su línea del diario y el estado que le toque— y lo suelta. Las demás esperan. El único que hay que soltar a mano es este, y cubre el cierre entero —estado, poda y comprobaciones—, no toda la sesión. Cada sesión cierra su propio ítem: no hay un cierre principal que absorba el de otra.

**El dueño del cerrojo.** El cerrojo guarda la sesión que lo tomó y la hora. No se retira por antigüedad mientras esa sesión siga dando señal: un cierre tarda porque incluye puertas y comprobaciones. Pasados 30 minutos con el cerrojo tomado se avisa de huérfano; si el dueño sigue latiendo, no se toca. La persona decide, y el `--force` existe pero se pide. Como en el reclamo, el tiempo mide espera, no abandono.

**El orden del día siguiente.** El cierre no deja el siguiente ítem elegido. El orden se decide al retomar, con la persona. Escribirlo antes convertiría una decisión de prioridad en una herencia.

## 4. Modos de fallo y qué evita cada pieza

| Fallo | Qué lo evita | Qué queda sin cubrir |
|---|---|---|
| Dos sesiones cogen el mismo ítem | El directorio se crea una sola vez; la segunda recibe «ocupado» | Si la primitiva (la operación básica del reclamo) no es atómica, las dos creen haberlo creado |
| Dos sesiones escriben el mismo fichero | Un ítem por sesión y un dueño por fichero | Dos ítems distintos que tocan el mismo fichero |
| Una sesión acapara la cola | Tope de tres y un ítem por sesión | Que una sesión haga ítems muy largos |
| Una sesión muere a mitad | El latido deja de refrescarse y el ítem se ve «sin señal» | Nada lo libera solo: hace falta una persona |
| Dos cierres a la vez | Un solo cierre bajo cerrojo: el segundo espera o pregunta | Que un cierre se quede a medias y haya que soltarlo a mano |
| El reclamo se pierde en un reinicio | La caché es local y se puede reconstruir | No está probado con la caché vacía a mitad de sesión |
| El orden se hereda sin decidir | Nadie deja escrito el siguiente ítem | Que la persona no retome y la cola se enfríe |

Cada pieza evita un fallo concreto y deja otro abierto; ninguna promete más de lo que hace.

## 5. Verificación y estado

Lo ejecutado está en el experimento enlazado: fecha, arnés y artefactos. Allí se simulan las sesiones con procesos de shell (el intérprete de comandos) y se ejecutan seis casos y un control, de la competición por un ítem a la muerte con `SIGKILL`; uno de ellos midió el reparto retirado, y la pasada se repite idéntica.

El experimento mide la primitiva antes de usarla, porque el diseño descansa en ella. En ese equipo, el `mkdir` del sistema no fue atómico en todas las rondas y el arnés se negó a empezar; con otro binario, la competición se comportó como el diseño espera. La cifra y el detalle están en el experimento: aquí no se copian.

Lo que **no** está medido, y por eso este caso es **Parcial** y no Validado:

- El latido real de un plugin en las llamadas a herramienta.
- El cierre bajo cerrojo: se ejecuta en cada cierre, pero ningún arnés lo mide.
- Dos sesiones de agente reales, no procesos de shell.
- El tope y el ítem único cuando dos sesiones llegan exactamente a la vez.
- La caché en red, con dos máquinas.

Un caso de estudio no sube el estado de lo que cuenta. Si el experimento es Parcial, el caso es Parcial y lo dice.

## 6. Lecciones

**La garantía está en la primitiva, no en su nombre.** «Crear un directorio es atómico» es una propiedad del sistema de archivos y del programa que la ejecuta, no una verdad por llamarse `mkdir`. Medirla costó una pasada y evitó publicar un reparto que fallaba en algunas rondas.

**Un cerrojo pequeño por ítem escala mejor que uno global.** El global solo aparece al cerrar, cuando hay que escribir. Todo lo demás se decide con una operación local que no espera a nadie.

**No liberar solo es una propiedad, no un descuido.** Un ítem «sin señal» obliga a mirar. Un ítem liberado por tiempo finge que el trabajo está libre cuando puede estar a medias. La diferencia entre las dos cosas es la que hay entre un aviso y una decisión.

**Un cerrojo no adivina por el reloj.** El cierre no se retira por antigüedad si la sesión dueña sigue viva, y el reclamo sin señal no se libera solo. El tiempo mide espera, no abandono: la diferencia la decide una persona.

**Escribir solo al cerrar reduce la superficie del conflicto.** Mientras se trabaja, el estado compartido no se toca. El momento delicado es uno, y está protegido.

**Un hecho, un dueño.** Un ítem en un solo fichero, y los mapas que solo enlazan, evitan la pregunta de cuál de las dos copias manda.

Un reparto se puede describir con pocas reglas, pero ninguna vale nada si no se prueba la pieza de la que depende.
