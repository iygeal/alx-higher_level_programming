SELECT city, AVG(value) AS average_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8) -- Filter for July and August
GROUP BY city
ORDER BY average_temp DESC
LIMIT 3;