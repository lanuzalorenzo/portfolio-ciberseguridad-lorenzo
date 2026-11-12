# Comandos — inventario del binario publicado

Ejecutado el 2026-11-12 en local.

## 0. Herramienta

```bash
dotnet tool install --tool-path /tmp/tools --version 11.2.0.10050 ilspycmd
/tmp/tools/ilspycmd --version
```

Salida:

```text
ilspycmd: 11.2.0.10050
ICSharpCode.Decompiler: 11.2.0.10050
```

## 1. Publicación antes

```bash
dotnet publish EcommerceApi/EcommerceApi.csproj -c Release \
  -o /tmp/p05-before /p:UseAppHost=false
find /tmp/p05-before -name '*.pdb' -printf '%f %s\n' | sort
```

Salida:

```text
EcommerceApi.Application.pdb 18524
EcommerceApi.Contracts.pdb 12548
EcommerceApi.Domain.pdb 14488
EcommerceApi.Infrastructure.pdb 23780
EcommerceApi.pdb 38732
```

## 2. Publicación después

```bash
dotnet publish EcommerceApi/EcommerceApi.csproj -c Release \
  -o /tmp/p05-after /p:UseAppHost=false
find /tmp/p05-after -name '*.pdb' | wc -l
```

Salida:

```text
0
```

## 3. Descompilación antes

```bash
/tmp/tools/ilspycmd -p -o /tmp/p05-decompiled-before \
  /tmp/p05-before/EcommerceApi.dll
find /tmp/p05-decompiled-before -type f | wc -l
```

Salida:

```text
20
```

Búsqueda de cadenas sobre el código anterior, con el mismo patrón que la de después:

```bash
grep -RIn -Ei 'password|secret|api[_-]?key|connectionstring|YOUR_' \
  /tmp/p05-decompiled-before
```

Salida: solo las comparaciones con el prefijo `YOUR_` de `AzureAdOptions`; no hay
valores de credenciales.

## 4. Descompilación después

```bash
/tmp/tools/ilspycmd -p -o /tmp/p05-decompiled-after \
  /tmp/p05-after/EcommerceApi.dll
find /tmp/p05-decompiled-after -type f | wc -l
```

Salida:

```text
20
```

## 5. Búsqueda de secretos

```bash
grep -RIn -Ei 'password|secret|api[_-]?key|connectionstring|YOUR_' \
  /tmp/p05-decompiled-after
```

Salida: solo las comparaciones de `AzureAdOptions` con el prefijo `YOUR_`, que forman parte de la validación de configuración. No hay valores de credenciales.

## 6. Configuración publicada

```bash
grep -RIn -E 'YOUR_|00000000' /tmp/p05-before/appsettings*.json
grep -RIn -E 'YOUR_|00000000' /tmp/p05-after/appsettings*.json
```

Salida: los mismos placeholders `YOUR_TENANT_ID`, `YOUR_API_CLIENT_ID` y
`YOUR_API_CLIENT_ID` en `appsettings.json`, y los ceros de ejemplo en
`appsettings.Development.example.json`. No hay valores reales en ninguno de los
dos directorios.
