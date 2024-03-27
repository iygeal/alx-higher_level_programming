-- This script retrieves and analyzes temperature data from the 'temperatures' table.
-- It focuses on data from the months of July (7) and August (8), using the 'MONTH' function
-- to extract the month number from the 'date' column for filtering.
-- It then calculates the average temperature for each city during those months and displays
-- the top 3 cities with the highest average temperatures in descending order.

-- Filtering for July and August
-- Grouping data by city to calculate average temperature
-- Ordering by average temperature in descending order
-- Limiting displayed results to the top 3 cities

SELECT city, AVG(value) AS average_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY average_temp DESC
LIMIT 3;
