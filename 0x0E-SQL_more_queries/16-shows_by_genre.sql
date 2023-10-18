-- lists all shows with linked genres
SELECT title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv genres.id
ORDER BY title, tv_genres.name;
