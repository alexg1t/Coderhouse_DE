# DataWarehouse_ETLs :)
#Thoughts about the content provided

Data Warehouse:
Almancenan grandes cantidades de datos (Datos estructurados) Base de datos relaciones y multiples fuentes.
Poseen herramientas para hacer consultas eficientes
No esta optimizado para hacer consultas de registros especificos ni para la escritura de registros unicos, solo en batch.
Optimizado para el Analytics

Data Mart - Data Lakes
Set de tablas de datos ya sumarizados en general.
En finanzas, pueden ser de datos especiales como devoluciones o reembolsos. Conviven en un data warehouse.
Datos sumarizados o resumidos.

Data Lakes
Repositorio de datos previo al warehouse.
Si pensamos a los data marts como una botella de agua limpia y purificada. El data lake es un gran oceano en su estado natural. Los datos pueden ser datos crudos, no estructurados, semiestructurados o estructurados. No son relacionales. .txt, json , etc.

ETL.
Alimentan el data warehouse.
Extract-Transform-Load
Extract- Extraccion de datos desde la fuente cruda. De los datalakes.
Transform- Transformacion de los datos crudos a estructurados para datawarehouse. API envia json, transformacion a tabla seria necesario. 
Load- Transportar los datos a data warehouse.


ELT.
El datawarehouse hace todo el trabajo de transformacion.

Beneficios.
ELT es mas rapido.Menor mantenimiento.
Posee tanto datos crudos como transformados.
Permite localizar los recursos.

Batch processing- Stream processing

Batch- Grandes volumenes de datos a procesar en un periodo de tiempo.
Stream- Se procesan datos en tiempo real continuamente.



