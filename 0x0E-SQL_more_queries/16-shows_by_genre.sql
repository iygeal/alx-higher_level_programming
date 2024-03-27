-- This script lists all shows and their linked genres from the hbtn_0d_tvshows database
-- It retrieves the title of each show from the tv_shows table and the genre name from the tv_genres table
-- Shows without linked genres are displayed as NULL in the genre column
-- Results are sorted in ascending order by the show title and genre name

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
