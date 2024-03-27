-- This script retrieves the maximum temperature recorded
-- for each state in the 'temperatures' table.
-- It groups data by the 'state' column to
-- identify the maximum temperature within each state.

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state

-- Orders the results by the 'state' column in ascending order (A-Z)
-- to display states alphabetically.
ORDER BY state ASC;
