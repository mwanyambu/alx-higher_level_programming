-- script joins two tables
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.show_id
GROUP BY tv_show_genres.genre_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY number_of_shows DESC;
