-- This script lists all genres in the hbtn_0d_tvshows_rate
-- database by their rating sum
-- It retrieves the name of each genre from the tv_genres table
-- and calculates the sum of ratings from the tv_show_ratings table
-- for shows belonging to each genre
-- Results are sorted in descending order by the rating sum

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
