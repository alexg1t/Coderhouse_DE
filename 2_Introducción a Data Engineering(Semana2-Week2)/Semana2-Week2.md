# Acerca de Data Engineering Semana 2 :)
#Thoughts about the content provided

-Big data: desarrollar e implementar soluciones que permitan procesar datos de forma rápida eficaz y fácil.
Se empezó a usar desde los años 90.
Requerimientos de big data: Volumen, Velocidad, Variedad

Data Engineer?
Ingeniero enfocado en la resolución de problemas que involucran grandes cantidades de datos.

Enfoque del data Engineering:
	- Estructura de datos
	- Warehousing
	- Data Mining
	- Modelado de datos
	- Seguridad de los datos

Almacenar, administrar y convertir datos crudos. El producto es dirigido hacia los Data Analyst.

Data Engineering <-> Data Analyst
				 <-> Data Scientist 

Data Engineer -> Ayuda y brinda información, automatiza el flujo de datos.
Data Analyst -> Analítica de datos y genera métricas de los datos.
Data Scientist -> Elabora modelos predictivos con los datos que le proveen.


Sistemas OLTP (Online Transaction Processing) - OLAP (Online Analytical Processing)

OLTP:
Se enfocan en la escritura de transaccion y lectura de datos especificos.
Ejemplo: Sistema bancario, clientes cuentas bancarias y transacciones.
Operaciones comunes: Crear cuenta, mandados de dinero, pagos en general.

En base de datos: Inserts y demás- Lecturas para datos en específico. No registran informacion analítica ya que no es relevante.

OLAP:
Se enfocan en lectura de datos en forma de gran escala o masiva para realizar consultas analíticas.
Ejemplo: Promedio de edad de los clientes del banco, promedio de cuentas por cliente.
Usado para segmentación de clientes.

En base de datos: Si son utilizados por Data Analyst y Data Scientist. Operaciones de tipo SELECT son predominantes.


