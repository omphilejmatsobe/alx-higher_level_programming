-- import the database dump from hbtn_0d_tvshows_rate to the MySQL server
SELECT name, SUM(rate) AS rating
  FROM tv_genres AS genres
       INNER JOIN tv_show_genres AS show_genres
	   ON genres.id = show_genres.genre_id
	   INNER JOIN tv_show_ratings AS ratings
	   ON show_genres.show_id = ratings.show_id
 GROUP BY name ORDER BY rating DESC;
