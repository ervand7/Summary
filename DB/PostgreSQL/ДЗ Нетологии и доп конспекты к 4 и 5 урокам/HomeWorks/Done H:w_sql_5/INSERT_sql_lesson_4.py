# ```````` My problems during performance the home work ````````
# 1) И тут у меня возникла ошибка psycopg2.errors.InsufficientPrivilege: permission denied for table executors.
# Чтобы ее исправить, мне помогло это http://127.0.0.1:55820/help/help/grant_wizard.html


# 2) Потом возникла проблема с пакетной вставкой, но Юрий Батраков мне помог этой статьей
# https://coderoad.ru/7019831/%D0%9C%D0%B0%D1%81%D1%81%D0%BE%D0%B2%D0%BE%D0%B5-%D0%BF%D0%B0%D0%BA%D
# 0%B5%D1%82%D0%BD%D0%BE%D0%B5-%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-upsert-%D0%B2-PostgreSQL


# 3) Коллеги, вопрос такой возник. Выполняю ДЗ 4 по БД.
# Ситуация такая: если я где-то косячу, примеру при заполнении таблицы Albums, я использую
#  my_delete = connection.execute('''DELETE FROM Albums;
# ''')
# print(my_delete)
# чтобы стереть все и начать жизнь с чистого листа.
# Но, насколько я могу догадываться, из-за того, что моя таблица Albums содержит параметр
# id serial, то новые значения которые я записываю в чистую таблицу уже не начинаются с id 1,
# а, к примеру с id 9, если до этого я стер 8 альбомов в моей табличке Albums.
# Вопрос: этот показатель айдишника как-то можно сбросить на ноль?
# ```
# Yuri Batrakov replied:
# Надо дропнуть все таблицы, причём каскадом, так как они связаны. И создать заново,
# тогда айдишники будут с начала. Либо не использовать serial, а вести учёт альбомов
# вручную- их немного поэтому это  не сложно.


# 4) 'A field with precision 2, scale 2 must round to an absolute value less than 1.'
# here is a clarification:
# масштаб(scale) типа numeric — это количество десятичных разрядов в дробной части, справа от
# десятичной точки. Точность (precision) типа numeric — это общее количество значимых разрядов во
# всём числе, т.е. количество разрядов по обе стороны от десятичной точки. Таким образом,
# число 23.5141 имеет точность 6 и масштаб 4. Целые числа могут быть представлены с использованием
# масштаба ноль.


# 5) data insertion the type of 'date'
# Вот эти 2 статьи мне помогли:
# https://stackoverflow.com/questions/6018214/how-to-insert-current-timestamp-into-postgres-via-python
# https://www.postgresqltutorial.com/postgresql-date/
# _______________________________________________________________________________
# _______________________________________________________________________________
# _______________________________________________________________________________
import psycopg2
import sqlalchemy
from pprint import pprint

# создаем engine
# dialect+driver://username:password@host:port/database
engine = sqlalchemy.create_engine('postgresql://task_user:task_user@localhost:5432/lesson_3_database_without excess')
pprint(engine)

# установим соединение
connection = engine.connect()
pprint(connection)

# Посмотрим, какие таблицы есть
pprint(engine.table_names())

# # Insert. Сначала проверим, что у нас находится в таблице executors
checking = connection.execute('''SELECT * FROM executors;
''').fetchmany(10)
pprint(checking)

# _______________________________________________________________________________
# ||||||||||||||||| fill in the main tables |||||||||||||||||
# _______________________________________________________________________________

# # Insert. Добавим не менее 8 исполнителей
# insert_musicians = connection.execute('''INSERT INTO executors(Name_of_executors)
#     VALUES ('musician_1'), ('musician_2'), ('musician_3'), ('musician_4'),
#     ('musician_5'), ('musician_6'), ('musician_7'), ('musician_8');
# ''')
# pprint(insert_musicians)

# # Проверим
insert_musicians_view = connection.execute('''SELECT * FROM executors;
''').fetchall()
pprint(insert_musicians_view)

# _______________________________________________________________________________
# # Insert. Добавим не менее 5 жанров
# insert_genres = connection.execute('''INSERT INTO genres(Name_of_genre)
#     VALUES ('genre_1'), ('genre_2'), ('genre_3'), ('genre_4'), ('genre_5');
# ''')
# pprint(insert_genres)

# Проверим
insert_genres_view = connection.execute('''SELECT * FROM genres;
''').fetchall()
pprint(insert_genres_view)

# _______________________________________________________________________________

# # Insert. Добавим не менее 8 альбомов
# insert_albums = connection.execute(f'''INSERT INTO Albums(Name_of_album, Year_of_issue, Description)
#     VALUES ('Name_of_album_1', '2011-05-16 15:36:38', 'my_regular_loren_ipsum_1'),
#     ('Name_of_album_2', '2015-03-09 15:36:38', 'my_regular_loren_ipsum_2'),
#     ('Name_of_album_3', '2012-01-16 15:36:38', 'my_regular_loren_ipsum_3'),
#     ('Name_of_album_4', '2014-05-07 15:36:38', 'my_regular_loren_ipsum_4'),
#     ('Name_of_album_5', '2013-11-16 15:36:38', 'my_regular_loren_ipsum_5'),
#     ('Name_of_album_6', '2012-01-06 15:36:38', 'my_regular_loren_ipsum_6'),
#     ('Name_of_album_7', '2014-05-07 15:36:38', 'my_regular_loren_ipsum_7'),
#     ('Name_of_album_8', '2019-11-16 15:36:38', 'my_regular_loren_ipsum_8');
# ''')
# pprint(insert_albums)

# # Проверим
insert_albums_view = connection.execute('''SELECT * FROM Albums;
''').fetchall()
pprint(insert_albums_view)

# _______________________________________________________________________________
# # Insert. Добавим не менее 15 треков
# insert_tracks = connection.execute('''INSERT INTO Tracks(Name_of_track, Duration, Id_of_album)
#     VALUES ('Track_1', 02.02, 26),
#     ('Track_2', 03.02, 26), ('Track_3', 01.23, 27), ('Track_4', 01.13, 27),
#     ('Track_5', 02.02, 27), ('Track_6', 01.43, 28), ('Track_7', 01.15, 29),
#     ('Track_8', 01.02, 29), ('Track_9', 01.54, 30), ('Track_10', 01.46, 30),
#     ('Track_11', 03.02, 31), ('Track_12', 01.34, 31), ('Track_13', 01.33, 32),
#     ('Track_14', 01.02, 32), ('Track_15', 01.23, 33), ('Track_16', 01.27, 33);
# ''')
# pprint(insert_tracks)

# # Проверим
insert_tracks_view = connection.execute('''SELECT * FROM Tracks;
''').fetchall()
pprint(insert_tracks_view)

# _______________________________________________________________________________
# # Insert. Добавим не менее 8 сборников
# insert_collections = connection.execute('''INSERT INTO
#     Collections(Name_of_collection, collect_year_of_issue)
#     VALUES ('Name_of_collection_1', '2011-05-16 15:36:38'),
#     ('Name_of_collection_2', '2019-03-23 15:36:38'),
#     ('Name_of_collection_3', '2020-01-24 15:36:38'),
#     ('Name_of_collection_4', '2019-05-25 15:36:38'),
#     ('Name_of_collection_5', '2020-11-26 15:36:38'),
#     ('Name_of_collection_6', '2019-01-28 15:36:38'),
#     ('Name_of_collection_7', '2020-05-21 15:36:38'),
#     ('Name_of_collection_8', '2019-11-21 15:36:38');
# ''')
# pprint(insert_collections)

# # Проверим
insert_collections_view = connection.execute('''SELECT * FROM Collections;
''').fetchall()
pprint(insert_collections_view)

# _______________________________________________________________________________
# ||||||||||||||||| fill in the link tables |||||||||||||||||
# _______________________________________________________________________________
# # Insert. заполним таблицу связей Executors_Genres
# insert_executors_genres = connection.execute('''INSERT INTO
#     Executors_Genres(id_of_executor, id_of_genre)
#     VALUES (58, 2),
#     (59, 5),
#     (60, 5),
#     (61, 4),
#     (62, 2),
#     (63, 1),
#     (64, 3),
#     (65, 1);
# ''')
# pprint(insert_executors_genres)

# # Проверим
insert_executors_genres_view = connection.execute('''SELECT * FROM Executors_Genres;
''').fetchall()
pprint(insert_executors_genres_view)

# _______________________________________________________________________________
# # Insert. заполним таблицу связей Executors_Albums
# insert_executors_albums = connection.execute('''INSERT INTO
#     Executors_Albums(Id_of_executor, Id_of_album)
#     VALUES (58, 33),
#     (59, 26),
#     (60, 29),
#     (61, 28),
#     (62, 27),
#     (63, 30),
#     (64, 31),
#     (65, 32);
# ''')
# pprint(insert_executors_albums)

# # Проверим
insert_executors_albums_view = connection.execute('''SELECT * FROM Executors_Albums;
''').fetchall()
pprint(insert_executors_albums_view)

# _______________________________________________________________________________
# # Insert. заполним таблицу связей Tracks_Collections
# insert_executors_albums = connection.execute('''INSERT INTO
#     Tracks_Collections(Id_of_track, Id_of_collection)
#     VALUES (36, 8), (37, 7), (38, 7), (39, 5), (40, 1), (41, 2), (42, 3), (43, 4),
#     (44, 5), (45, 3), (46, 6), (47, 7), (48, 8), (49, 3), (50, 2), (51, 2);
# ''')
# pprint(insert_executors_albums)

# # Проверим
insert_tracks_collections_view = connection.execute('''SELECT * FROM Tracks_Collections;
''').fetchall()
pprint(insert_tracks_collections_view)


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # Insert. Добавим сверху еще 2 альбома для задания №2 (SELECT)
# insert_albums_additionally = connection.execute(f'''INSERT INTO Albums(Name_of_album, Year_of_issue, Description)
#     VALUES ('Name_of_album_1', '2011-05-16 15:36:38', 'my_regular_loren_ipsum_1'),
#     ('Name_of_album_xx', '2018-03-09 15:36:38', 'my_regular_loren_ipsum_xx'),
#     ('Name_of_album_yy', '2018-01-16 15:36:38', 'my_regular_loren_ipsum_yy');
# ''')
# print(insert_albums_additionally)


# # Insert. Добавим сверху еще 2 трека для задания №2 (SELECT)
# insert_tracks_additionally = connection.execute('''INSERT INTO Tracks(Name_of_track, Duration, Id_of_album)
#     VALUES ('Track_n', 05.01, 26), ('Track_m', 04.22, 26);
# ''')
# pprint(insert_tracks_additionally)


# # Insert. Добавим сверху еще 2 трека с 'my' для задания №2 (SELECT)
# insert_tracks_additionally_my = connection.execute('''INSERT INTO Tracks(Name_of_track, Duration, Id_of_album)
#     VALUES ('mymymymymymymymymy', 06.01, 28), ('Track_my', 04.52, 29);
# ''')
# pprint(insert_tracks_additionally_my)

