-- This script lists all shows contained in the hbtn_0d_tvshows database that do not have a genre linked
-- It retrieves the title of each show from the tv_shows table and the genre_id from the tv_show_genres table
-- Only shows without a genre linked are included in the result
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
