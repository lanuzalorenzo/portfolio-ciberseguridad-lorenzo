# Evidencia — inventario del binario publicado

> **Identificador:** `2026-11-12-05-api-binary`
>
> **Tipo:** ejecución (local)
>
> **Resultado:** **Validado en local**
>
> **Runbook:** no aplica; es un inventario antes/después del artefacto de publicación.

Un binario publicado es como una maleta que se entrega en destino: no basta con que lleve lo necesario; también hay que mirar que no lleve las instrucciones de montaje ni una nota con la contraseña. Esta evidencia compara el `dotnet publish` antes y después de retirar los símbolos de depuración y revisa el código descompilado en busca de secretos.

**In English.** A published binary is like a suitcase delivered to its destination: it is not enough that it carries what is needed; it should not carry the assembly instructions or a note with the password. This evidence compares `dotnet publish` before and after removing debug symbols and inspects the decompiled code for secrets.

## 1. Contexto

- **Fecha:** 2026-11-12.
- **Entorno:** Ubuntu 26.04.1 LTS, .NET SDK 10.0.115, `ilspycmd` 11.2.0.10050.
- **Objetivo:** `EcommerceApi`, publicación Release del host.
- **Alcance:** contenido del directorio de publicación, PDB y cadenas del ensamblado principal.
- **Fuera de alcance:** análisis de todas las dependencias, binarios nativos, imagen de contenedor y despliegue.

## 2. Antes

`dotnet publish` copiaba cinco PDB al directorio de publicación: el del host y los de los cuatro proyectos referenciados. Los PDB no son secretos, pero revelan rutas, nombres de tipos y números de línea, y no hacen falta para ejecutar la API.

El listado está en [`artefactos/pdb-antes.txt`](artefactos/pdb-antes.txt). El inventario del código anterior y la búsqueda de cadenas están en [`artefactos/inventario.txt`](artefactos/inventario.txt) y se reproducen en [`comandos.md`](comandos.md).

## 3. Cambio

`Directory.Build.props` fija `DebugType=none` y `DebugSymbols=false` solo para `Release`. La decisión se aplica a todos los proyectos de la solución y evita repetir la propiedad en cada `.csproj`, como pide el [ADR-0008](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/adr/0008-configuracion-de-compilacion-y-paquetes-centralizada.md). Las compilaciones `Debug` conservan sus símbolos para depurar. El cambio está en el [PR #65 de lab-api](https://github.com/lanuzalorenzo/lab-api-local-azure/pull/65), commit `768c440`.

## 4. Después

| Comprobación | Antes | Después |
|---|---|---|
| PDB en el publish | 5 | 0 |
| Archivos descompilados del host | 20 | 20 (medido en ambos) |
| Secretos o cadenas de conexión reales | 0 (grep sobre el código descompilado) | 0 (grep sobre el código descompilado) |
| `appsettings.json` | Placeholders `YOUR_*` (leído) | Placeholders `YOUR_*` (leído) |

El inventario del código descompilado está en [`artefactos/inventario.txt`](artefactos/inventario.txt) y el listado de PDB en [`artefactos/pdb-despues.txt`](artefactos/pdb-despues.txt). Los placeholders de configuración no son credenciales; la configuración real se inyecta por entorno o gestor de secretos.

## 5. Reproducción

```bash
dotnet publish EcommerceApi/EcommerceApi.csproj -c Release \
  -o /tmp/publish /p:UseAppHost=false
find /tmp/publish -name '*.pdb'
```

La segunda orden no debe imprimir nada. Para el inventario:

```bash
dotnet tool install --tool-path /tmp/tools --version 11.2.0.10050 ilspycmd
/tmp/tools/ilspycmd -p -o /tmp/decompiled /tmp/publish/EcommerceApi.dll
```

## 6. Límites

- El inventario se limita al ensamblado del host; las dependencias de terceros no se descompilaron.
- La evidencia es local y de la publicación desde el árbol de trabajo; no se construyó la imagen ni se desplegó.
- La ausencia de PDB reduce la información del artefacto, pero no impide la ingeniería inversa: el código IL sigue siendo legible.
- No se encontraron secretos en el host; eso no sustituye a Gitleaks ni al escaneo de la imagen.
