-- This script lists all genres not linked to
-- the show "Dexter" from the hbtn_0d_tvshows database
-- It retrieves the genres linked to the show "Dexter"
-- and then selects the genres not included in that list
-- Results are sorted in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY tv_genres.name;

SELECT name
FROM tv_genres
WHERE name NOT IN (
    SELECT tv_genres.name
    FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = shows.id
    WHERE tv_shows.title = 'Dexter'
);
