# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"

# CREATE TABLES

time_table_create = ("""CREATE TABLE IF NOT EXISTS time ( start_time timestamp PRIMARY KEY,
                                                        hour int, 
                                                        day int,
                                                        week int,
                                                        month int,
                                                        Year int,
                                                        weekday varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (   user_id text PRIMARY KEY,
                                                           first_name varchar,
                                                           last_name varchar,
                                                           gender varchar,
                                                           level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(   song_id text PRIMARY KEY,
                                                          title varchar,
                                                          artist_id text,
                                                          year int,
                                                          duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists ( artist_id text PRIMARY KEY,
                                                             name varchar NOT NULL,
                                                             location varchar,
                                                             latitude float,
                                                             longitude float);""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY,
                                                                start_time timestamp REFERENCES time(start_time),
                                                                user_id text REFERENCES users(user_id),
                                                                level varchar,
                                                                song_id text REFERENCES songs(song_id),
                                                                artist_id text REFERENCES artists(artist_id),
                                                                session_id text,
                                                                location varchar,
                                                                user_agent varchar);""")


# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(songplay_id,start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            ON CONFLICT (songplay_id) DO NOTHING;""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) 
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) 
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) 
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT (artist_id) DO NOTHING;""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) 
                        VALUES(%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id 
                  FROM songs s 
                  INNER JOIN artists a on s.artist_id = a.artist_id 
                  WHERE s.title = %s AND a.name = %s AND s.duration = %s """)

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, song_table_create,artist_table_create, songplay_table_create ]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]