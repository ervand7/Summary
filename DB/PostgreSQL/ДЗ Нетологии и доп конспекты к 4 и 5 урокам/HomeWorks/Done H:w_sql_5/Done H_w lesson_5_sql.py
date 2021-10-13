import psycopg2
import sqlalchemy
from pprint import pprint

# создаем engine
# dialect+driver://username:password@host:port/database
engine = sqlalchemy.create_engine('postgresql://task_user:task_user@localhost:5432/lesson_3_database_without excess')
# pprint(engine)

# установим соединение
connection = engine.connect()
# pprint(connection)

# Посмотрим, какие таблицы есть
# pprint(engine.table_names())

#  ____________________________________________________________
# |||||||||| SOLVING ||||||||||
#  ____________________________________________________________

# Найдем количество исполнителей в каждом жанре
# VARIANT 1:
sel_1_variant_1 = connection.execute("""
select id_of_genre, count(id_of_executor) from executors_genres
group by id_of_genre
order by id_of_genre;
""").fetchall()
# pprint(sel_1_variant_1)
# VARIANT 2:
sel_1_variant_2 = connection.execute("""
select name_of_genre, count(e_g.id_of_executor) from genres
join executors_genres e_g on e_g.id_of_genre = genres.id
group by name_of_genre
order by count desc;
""").fetchall()
# pprint(sel_1_variant_2)


# Найдем количество треков, вошедших в альбомы 2019-2020 годов
sel_2 = connection.execute("""
select count(t.id), a.name_of_album from tracks t
join albums a on t.id_of_album = a.id
group by a.id
having year_of_issue between '2019-01-01' and '2020-12-31';
""").fetchall()
# pprint(sel_2)


# # Найдем среднюю продолжительность треков по каждому альбому;
sel_3 = connection.execute("""
select a.name_of_album, avg(t.duration) from albums a
join tracks t on a.id = t.id_of_album
group by a.name_of_album
order by a.name_of_album
""").fetchall()
# pprint(sel_3)


# # Найдем всех исполнителей, которые не выпустили альбомы в 2020 году
sel_4 = connection.execute("""
select name_of_executors from executors e
join executors_albums e_a on e.id = e_a.id_of_executor
join albums a on e_a.id_of_album = a.id
group by e.name_of_executors, a.year_of_issue
having a.year_of_issue not between '2020-01-01' and '2020-12-31';
""").fetchall()
# pprint(sel_4)

# # Найдем названия сборников, в которых присутствует исполнитель 'musician_5'
sel_5 = connection.execute("""
select col.name_of_collection, e.name_of_executors from executors e
join executors_albums e_a on e.id = e_a.id_of_executor
join albums a on e_a.id_of_album = a.id
join tracks t on a.id = t.id_of_album
join tracks_collections t_c on t.id = t_c.id_of_track
join collections col on t_c.id_of_collection = col.id
group by col.name_of_collection, e.name_of_executors
having e.name_of_executors like '%%musician_5%%';
""").fetchall()
# pprint(sel_5)


# # Найдем название альбомов, в которых присутствуют исполнители более 1 жанра
sel_6_my_variant = connection.execute("""
select a.name_of_album, e.name_of_executors, g.name_of_genre from albums a
left join executors_albums e_a on a.id = e_a.id_of_album
left join executors e on e.id = e_a.id_of_executor
left join executors_genres e_g on e_g.id_of_executor = e.id
left join genres as g on g.id = e_g.id_of_genre
group by a.name_of_album, e.name_of_executors, g.name_of_genre
having count(g.id) > 1;
""").fetchall()
# pprint(sel_6_my_variant)
# # variant of Oleg_Bulygin
sel_6_variant_of_Oleg_Bulygin = connection.execute("""
SELECT a.name_of_album FROM executors_genres e_g
JOIN genres g ON e_g.id_of_genre = g.id
JOIN executors e ON e_g.id_of_executor = e.id
JOIN executors_albums e_a ON e_a.id_of_executor = e.id
JOIN albums a ON e_a.id_of_album = a.id
GROUP BY a.name_of_album
HAVING COUNT(g.name_of_genre) > 1;
""").fetchall()
pprint(sel_6_variant_of_Oleg_Bulygin)


# # Найдем названия альбомов, содержащих наименьшее количество треков
sel_7 = connection.execute("""
select distinct a.name_of_album from albums a
join tracks t on t.id_of_album = a.id
where t.id_of_album in (
    select id_of_album from tracks
    group by id_of_album
    having count(tracks.id) = (
        select count(tracks.id) from tracks
        group by id_of_album
        limit 1
    )
);
""").fetchall()
# pprint(sel_7)


# # Найдем исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько);
sel_8 = connection.execute("""
select e.name_of_executors, min(t.duration) from tracks as t
left join albums a on a.id = t.id_of_album
left join executors_albums e_a on e_a.id_of_album = a.id
left join executors e on e.id = e_a.id_of_executor
group by e.name_of_executors, t.duration
having t.duration = (
    select min(duration) from tracks
    );
""").fetchall()
# pprint(sel_8)


# # Найдем наименование треков, которые не входят в сборники
sel_9 = connection.execute("""
select t.name_of_track from tracks t
left join tracks_collections t_c on t_c.id_of_track = t.id
where t_c.id_of_track is null;
""").fetchall()
# pprint(sel_9)
