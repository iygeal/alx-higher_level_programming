-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating sum
-- It retrieves the title of each show from the tv_shows table
-- and calculates the sum of ratings from the tv_show_ratings table
-- Results are sorted in descending order by the rating sum

SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
