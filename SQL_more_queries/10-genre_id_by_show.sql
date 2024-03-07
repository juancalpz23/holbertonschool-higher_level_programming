--Show liked genres Left Join
SELECT a.title, b.genre_id 
FROM tv_show_genres b
LEFT JOIN tv_shows a
ON b.show_id = a.id 
ORDER BY a.title, b.genre_id ASC;