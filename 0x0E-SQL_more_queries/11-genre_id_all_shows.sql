-- This script lists all shows contained in the hbtn_0d_tvshows database along with their respective genre IDs
-- It retrieves the title of each show from the tv_shows table and the corresponding genre ID from the tv_show_genres table
-- If a show doesn't have a genre, NULL is displayed
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
