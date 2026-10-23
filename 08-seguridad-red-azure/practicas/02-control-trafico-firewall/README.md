# 02 | Control centralizado de tráfico con Azure Firewall

La segmentación de la práctica 01 cierra la entrada, pero deja la salida de las subredes con las reglas predeterminadas de Azure. Un firewall en el perímetro convertiría esa salida en una decisión explícita: qué destinos puede alcanzar la API y cuáles no.

**Referencias:** MCSB NS-3 · CIS Azure 6.x

| Qué se plantea | Cómo se probaría | Estado |
|---|---|---|
| Firewall con política de egreso | Crear el recurso y asociar una route table a `snet-app` | Pendiente: coste y disponibilidad regional sin confirmar |
| Destino permitido | Petición a un destino incluido en la política | Pendiente: requiere despliegue |
| Destino denegado | Petición a un destino excluido, con el mismo cliente | Pendiente: requiere despliegue |
| Ruta efectiva | Revisar la ruta de salida desde la subred | Pendiente: requiere despliegue |

No hay Bicep de firewall. El diseño pide una política con destinos justificados y una route table que solo afecte a las subredes del laboratorio; añadirlo antes de confirmar precio y región sería escribir una configuración que no se puede probar.

No desplegarlo no es un aprobado: la práctica está en diseño y el control sigue pendiente en la matriz. Sin firewall, un NSG de entrada no limita el egreso; una route table mal asociada puede desviar tráfico ajeno al laboratorio; y el coste del servicio obliga a separar el diseño de la ejecución.
