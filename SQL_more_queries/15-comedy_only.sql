-- List all Comedy shows Left Join
SELECT a.title
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
LEFT JOIN tv_genres c
ON b.genre_id = c.id
WHERE c.name = 'Comedy'
ORDER BY 1 ASC;