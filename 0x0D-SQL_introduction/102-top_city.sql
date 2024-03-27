-- Displays the top 3 cities' temperatures during July and August, ordered by temperature (descending)
SELECT city, MAX(value) AS max_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- Filters the data for July and August
GROUP BY city
ORDER BY max_temp DESC  -- Orders the results by maximum temperature in descending order
LIMIT 3;  -- Limits the output to the top 3 records
