--a)
/*Extraer agentes cuyo nombre empieza por M o termine por O.*/
SELECT * from agents
WHERE name LIKE 'M%' OR name LIKE '%O';

--b)
/*Escribir una consulta que produzca una lista en orden alfabético, de todas las ocupaciones que
lleven la palabra Engineer.*/
SELECT * FROM 


--c)
/*Escribir una consulta que devuelva el ID del cliente, su nombre y una columna nueva llamada mayor30
cuyo valor es "si" si es mayor de 30años. caso contrario "no"*/
SELECT * FROM 
--d)
/*Escribir una consulta que devuelva todas las llamadas a clientes con profesión Ingeniería y si 
son mayores de 30, así como también si realizaron una compra.*/
SELECT * FROM 
--e)
/* Escribir dos consultas.
	-Una calcula las ventas totales y llamadas totales realizadas a los clientes de profesión de Ingeniería.
	-Otro que calcule lo mismo para todos los clientes.*/
SELECT * FROM 
--f)
/*Escribir consulta:
	-Para cada agente: el nombre del agente, la cantidad de llamadas, sus llamadas más largas y las más cortas,
	el promedio de todas sus llamadas y cuantos productos vendió.
	-Nombre de cada columna: AgentName,NCalls,Longest,Shortest,AvgDuration y TotalSales
	-Ordenar tabla en orden alfabético.*/
SELECT * FROM 
--g)
/*Escribir consulta:
	-Para cada agente:Cuántos segundos les toma vender un producto cuanto tienen éxito.
	-Cuántos segundos toman en darse cuenta que no tendrán éxito (asumo que es cuando no concretan una venta).*/
SELECT * FROM 