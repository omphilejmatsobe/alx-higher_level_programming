-- import the database dump from hbtn_0d_tvshows to the MySQL server
SELECT shows.title
  FROM tv_shows AS shows
	 INNER JOIN tv_show_genres AS show_genres
	     ON shows.id = show_genres.show_id
	     INNER JOIN tv_genres AS tv_g
	     ON tv_g.id = show_genres.genre_id
	     WHERE tv_g.name = 'Comedy'
 ORDER BY shows.title;

