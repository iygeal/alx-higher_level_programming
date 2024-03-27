-- This script lists all shows contained in the hbtn_0d_tvshows database
-- that have at least one genre linked
-- It retrieves the title of each show from the tv_shows
-- table and the genre_id from the tv_show_genres table
-- Results are sorted in ascending order by tv_shows.title
-- and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
