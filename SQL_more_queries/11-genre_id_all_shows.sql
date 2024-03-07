-- List shows in database RIGHT JOIN
SELECT a.title, b.genre_id
FROM tv_show_genres b
RIGHT JOIN tv_shows a
ON b.show_id = a.id
ORDER BY a.title, b.genre_id ASC;