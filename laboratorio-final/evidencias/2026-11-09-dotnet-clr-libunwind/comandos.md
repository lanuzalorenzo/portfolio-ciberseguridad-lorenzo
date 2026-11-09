# Comandos — caída intermitente del CLR por libunwind

Las rutas de la solución y de los volcados se sustituyen por `$SOLUCION` y `$DUMP`. No se publica el nombre del repositorio ni la ruta del equipo.

## 1. Entorno

`RUNTIME` es la raíz del runtime que muestra `dotnet --info`; en este equipo, la del paquete de Ubuntu.

```bash
RUNTIME="<raíz del runtime que muestra dotnet --info>"

uname -sr
. /etc/os-release && echo "$PRETTY_NAME"
getconf GNU_LIBC_VERSION
dotnet --version
dotnet --info
snap list dotnet-sdk-100
dpkg-query -W -f='${Package} ${Version}\n' 'libunwind*'
ldd "$RUNTIME/shared/Microsoft.NETCore.App/10.0.14/libcoreclr.so" | grep -i unwind
```

Salida saneada:

```text
Linux 7.0.0-38-generic
Ubuntu 26.04.1 LTS
glibc 2.43
10.0.114

Host:
  Version:      10.0.14
  Architecture: x64

.NET SDKs installed:
  10.0.114 [ruta del SDK empaquetado por Ubuntu]

.NET runtimes installed:
  Microsoft.AspNetCore.App 10.0.14 [ruta del runtime empaquetado por Ubuntu]
  Microsoft.NETCore.App 10.0.14 [ruta del runtime empaquetado por Ubuntu]

dotnet-sdk-100  10.0.114  40  latest/stable  canonical**

libunwind8 1.8.3-0ubuntu1

libunwind-x86_64.so.8 => /usr/lib/x86_64-linux-gnu/libunwind-x86_64.so.8
libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8
```

El detalle completo está en [`artefactos/entorno.txt`](artefactos/entorno.txt).

## 2. Verificación con paralelismo por defecto

Diez tandas secuenciales; en cada una, una build y un test. La variable `MSBUILDDISABLENODEREUSE=1` evita reutilizar nodos, no impide crearlos durante la tanda.

```bash
cd "$SOLUCION"
export MSBUILDDISABLENODEREUSE=1

for i in $(seq 1 10); do
  dotnet build "$SOLUCION" -c Release --no-restore
  dotnet test  "$SOLUCION" -c Release --no-build --no-restore
done
```

Resultado saneado:

```text
tanda 01 build=0   test=0   OK
tanda 02 build=0   test=0   OK
tanda 03 build=0   test=134 FALLO
tanda 04 build=0   test=0   OK
tanda 05 build=0   test=0   OK
tanda 06 build=0   test=0   OK
tanda 07 build=0   test=134 FALLO
tanda 08 build=0   test=0   OK
tanda 09 build=0   test=0   OK
tanda 10 build=0   test=0   OK

RESULTADO: 2 de 10 tandas con fallo del CLR
```

Salida de una tanda fallida:

```text
Fatal error.
Internal CLR error. (0x80131506)
```

## 3. Verificación con un solo nodo

```bash
cd "$SOLUCION"
export MSBUILDDISABLENODEREUSE=1

for i in $(seq 1 10); do
  dotnet build "$SOLUCION" -c Release --no-restore -m:1
  dotnet test  "$SOLUCION" -c Release --no-build --no-restore -m:1
done
```

Resultado saneado:

```text
tanda 01 build=0 test=0 OK
tanda 02 build=0 test=0 OK
tanda 03 build=0 test=0 OK
tanda 04 build=0 test=0 OK
tanda 05 build=0 test=0 OK
tanda 06 build=0 test=0 OK
tanda 07 build=0 test=0 OK
tanda 08 build=0 test=0 OK
tanda 09 build=0 test=0 OK
tanda 10 build=0 test=0 OK

RESULTADO: 0 de 10 tandas con fallo del CLR
```

## 4. Lectura del volcado

```bash
export DOTNET_ROOT="$RUNTIME"
dotnet-dump analyze "$DUMP" -c "setthread 8" -c "pe" -c "threads"
dotnet-dump analyze "$DUMP" -c "clrstack -all"
```

Salida saneada del volcado de las 10:55:

```text
> setthread 8
> pe
Exception object: 00007d064cc00178
Exception type:   System.ExecutionEngineException
Message:          <none>
InnerException:   <none>
StackTrace (generated):
<none>
StackTraceString: <none>
HResult: 80131506

*8 0xD0F5
```

En el volcado de las 10:30 se fijó el hilo 19 (`0x5AB6`) y la firma fue la misma. `clrstack -all` devolvió cuatro hilos en `StartNewNode` en el primero y cinco en el segundo.

## 5. Limpieza

No se crearon recursos cloud ni contenedores. Los volcados y las transcripciones se guardaron fuera del repositorio; el repositorio solo conserva los extractos saneados.
