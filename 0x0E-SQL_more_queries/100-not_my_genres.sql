-- List all genres not linked to the show Dexter from `hbtn_0d_tvshows`.
SELECT tv_genres.name
    FROM tv_genres
    WHERE tv_genres.id NOT IN (
        SELECT DISTINCT tv_genres.id
        FROM tv_genres
        JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
        JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id AND tv_shows.title = 'Dexter'
    )
    ORDER BY tv_genres.name ASC;
