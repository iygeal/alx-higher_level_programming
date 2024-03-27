-- This script lists all cities of California from the hbtn_0d_usa database
-- It retrieves the state_id for California from the states table using a subquery
-- Then, it selects all cities from the cities table where state_id matches the one for California
-- Results are sorted in ascending order by cities.id

SELECT id, name FROM cities;
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
