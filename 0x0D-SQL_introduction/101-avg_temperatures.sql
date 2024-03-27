-- Calculate the average temperature (Fahrenheit) by city and order by temperature (descending)
-- Selects the city and calculates the average temperature, assigning it an alias avg_temp
-- Specifies the table name (temperatures) from which to retrieve data
-- Groups the results by city
-- Orders the results by avg_temp (average temperature) in descending order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
