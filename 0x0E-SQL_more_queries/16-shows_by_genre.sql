-- List all shows, and all genres linked to that show from `hbtn_0d_tvshows` database.
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS 'name'
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY tv_shows.title ASC, name ASC;
