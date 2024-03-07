-- List shows in database RIGHT JOIN
SELECT a.title, b.genre_id 
FROM tv_show_genres a
RIGHT JOIN tv_shows b
ON b.show_id = a.id
ORDER BY a.title, b.genre_id ASC;