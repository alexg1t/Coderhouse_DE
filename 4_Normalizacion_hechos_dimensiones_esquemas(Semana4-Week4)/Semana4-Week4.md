# Normalización, hechos,dimnsiones y tipos de esquemas :)
#Thoughts about the content provided

Normalización - Denormalización (técnica de diseño de base de datos)

-Normalización:
Se hace para evitar redundancia en los datos
Almacenamiento de forma óptima
Sistemas OLTP

Formas de Normalización:
1era
Cada celda de la tabla debe contener un solo valor
Cada registro debe ser único
2da
Satisfacer la 1ra
Clave principal(primary key) es solo una columna
3ra
Dependencia transitoria- Todas las columnas dependen de la llave primaria
Satisfacer la 2da.
No tener dependencias transitorias



-Denormalización:
Optimizar queries
Sistemas OLAP
Almacenamiento histórico

Modelo dimensional:

Dimensiones
Contexto de los hechos
Qué? Cómo? Cuándo? Quién? Dónde=
Cualitativos

Hechos
Indicadores
Valores numericos
KPIs
Cuantitativos

Preguntas al construir un modelo dimensional.
1.A que proceso de negocio hacemos referencia?
2.Granularidad(Nivel de detalle)
3.Definir dimensiones
4.Definir hechos

Pregunta de negocio- Quiero saber mi rentabilidad mensual
rptas.
1.Rentas y costos
2.Considerar mes a mes, año, trimestre.
3.Productos-que?, Sedes físicas o virtuales-como?, calendario- cuando?,vendedore o cliente - quienes?
4.Ventas,costos

a.Valor de la cantidad - Hechos
b.Fecha - Dimension
c. Taxes en cada orden - Hecho
d. Empleado - Dimension
e. Costo total de la orden - Hecho
f. Cliente - Dimension
g. Tienda-Dimension
h. Producto -Dimension


Tipos de esquema-
Estrella.
1 o mas tabla de hechos en el centro
dimensiones como aristas-Dimensiones denormalizadas

Copo de nieve.
1 o mas tablas de hechos en el centro
dimensiones normalizadas

Clusters y MPP
Big Data: Se procesan grandes cantidades de datos

Una query en un sistema legacy, 100 millones de datos

Procesamiento en paralelo: Una tarea grande se divide en tareas pequeñas que son procesados en paralelo
Particionar tablas: fragmenta, particiones

Cluster: arquitectura consistente de un main ( maestro) y nodos esclavos










