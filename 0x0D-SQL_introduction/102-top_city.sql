-- Filtering for July and August
-- Grouping data by city to calculate average temperature
-- Ordering by average temperature in descending order
-- Limiting displayed results to the top 3 cities
-- This script retrieves and analyzes temperature data from the 'temperatures' table.
-- It focuses on data from the months of July (7) and August (8).

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 OR month=8  -- Filter for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
