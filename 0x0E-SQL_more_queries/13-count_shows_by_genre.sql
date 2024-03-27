-- This script lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each
-- It retrieves the genre from the tv_genres table and counts the number of shows linked to each genre from the tv_show_genres table
-- Only genres with at least one linked show are included in the result
-- Results are sorted in descending order by the number of shows linked to each genre

SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
ORDER BY number_of_shows DESC;
