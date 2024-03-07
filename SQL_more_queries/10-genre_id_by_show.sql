--Show liked genres INNER JOIN
SELECT a.`title`, b.`genre_id`
FROM `tv_shows` AS a
INNER JOIN `tv_show_genres` AS b
ON a.`id` = b.`show_id`
ORDER BY a.`title`, b.`genre_id`;