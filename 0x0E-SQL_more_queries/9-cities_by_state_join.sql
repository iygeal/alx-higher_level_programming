-- This script lists all cities contained in the hbtn_0d_usa database
-- along with their respective state names using JOIN
-- It retrieves the city id and name from the cities table,
-- and the corresponding state name from the states table using JOIN
-- Results are sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
