-- This script uses the 'hbtn_0d_tvshows' database to list all genres of the show 'Dexter'
SELECT tg.name FROM tv_shows ts INNER JOIN tv_show_genres tsg ON ts.id = tsg.show_id INNER JOIN tv_genres tg ON tsg.genre_id = tg.id WHERE ts.title = 'Dexter' ORDER BY tg.name;
