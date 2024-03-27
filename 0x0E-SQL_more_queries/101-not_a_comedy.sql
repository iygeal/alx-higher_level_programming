-- This script lists all shows without the genre Comedy
-- from the hbtn_0d_tvshows database
-- It retrieves the titles of shows without the genre Comedy
-- by excluding shows with the Comedy genre
-- Results are sorted in ascending order by the show title

USE hbtn_0d_tvshows;

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
