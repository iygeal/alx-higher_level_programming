-- This script lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each
-- It retrieves the genre from the tv_genres table and counts the number of shows linked to each genre from the tv_show_genres table
-- Only genres with at least one linked show are included in the result
-- Results are sorted in descending order by the number of shows linked to each genre

 SELECT g.name AS genre,
       COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t ON g.id = t.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;