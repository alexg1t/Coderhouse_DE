--a)
/*Extraer agentes cuyo nombre empieza por M o termine por O.*/
SELECT * from agents
WHERE name LIKE 'M%' OR name LIKE '%O';

--b)
/*Escribir una consulta de la tabla customer que produzca una lista en orden alfabético, de todas las ocupaciones que
lleven la palabra Engineer.*/
SELECT occupation FROM customers
WHERE occupation LIKE '%Engineer%'
ORDER BY occupation;


--c)
/*Escribir una consulta que devuelva el ID del cliente, su nombre y una columna nueva llamada mayor30
cuyo valor es "si" si es mayor de 30años. caso contrario "no"*/
SELECT customerid,name,
CASE WHEN Age>=30 THEN 'Yes'
	 ELSE 'No'
END AS Over30
FROM customers
ORDER BY customerid;
--d)
/*Escribir una consulta que devuelva todas las llamadas a clientes con profesión Ingeniería y si 
son mayores de 30, así como también si realizaron una compra.*/
SELECT c.callid, c.productsold, c.customerid,cust.Age,cust.occupation,
CASE WHEN cust.Age>=30 THEN 'Yes'
	 ELSE 'No'
END AS Over30
FROM calls AS c
INNER JOIN customers AS cust ON c.customerid=cust.customerid
WHERE cust.occupation LIKE'%Engineer%';

--e)
/* Escribir dos consultas.
	-Una calcula las ventas totales y llamadas totales realizadas a los clientes de profesión de Ingeniería.
	-Otro que calcule lo mismo para todos los clientes.*/
SELECT SUM(productsold) AS TotalSales, COUNT(*) AS NCalls
FROM customers AS cust
JOIN calls AS c ON c.customerid =cust.customerid
WHERE cust.occupation LIKE '%Engineer%';

SELECT SUM(productsold) AS TotalSales, COUNT(*) AS NCalls
FROM customers AS cust
JOIN calls AS c ON c.customerid =cust.customerid;

--f)
/*Escribir consulta:
	-Para cada agente: el nombre del agente, la cantidad de llamadas, sus llamadas más largas y las más cortas,
	el promedio de todas sus llamadas y cuantos productos vendió.
	-Nombre de cada columna: AgentName,NCalls,Longest,Shortest,AvgDuration y TotalSales
	-Ordenar tabla en orden alfabético.*/
SELECT name AS AgentName,COUNT(*) AS NCalls,MIN(duration)AS Shortest,MAX(duration) AS
Longest, ROUND(AVG(duration),2) AS AvgDuration, SUM(productsold) AS TotalSales
FROM calls as c 
JOIN agents as A ON c.agentid =A.agentid
WHERE pickedup =1
GROUP BY name;
ORDER BY name;
--g)
/*Escribir consulta:
	-Para cada agente:Cuántos segundos les toma vender un producto cuanto tienen éxito.
	-Cuántos segundos toman en darse cuenta que no tendrán éxito (asumo que es cuando no concretan una venta).*/
