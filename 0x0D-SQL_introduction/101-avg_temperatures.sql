-- Calculate the average temperature (Fahrenheit)
-- by city and order by temperature (descending)

SELECT city, AVG(temperature) AS average_temperature_fahrenheit
FROM table_name
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
