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
# Оператор WHERE. Найдем название и год выхода альбомов, вышедших в 2018 году;
select_1 = connection.execute('''SELECT  Name_of_album, Year_of_issue FROM Albums
WHERE Year_of_issue BETWEEN '2018-01-01' AND '2018-12-31';
''').fetchall()
pprint(select_1)

# Найдем название и продолжительность самого длительного трека
select_2 = connection.execute('''SELECT Duration, Name_of_track FROM Tracks
WHERE Duration = (
   SELECT MAX (Duration)
   FROM Tracks
);
''').fetchall()
pprint(select_2)

# Найдем название треков, продолжительность которых не менее 3,5 минуты
select_3 = connection.execute('''SELECT  Name_of_track, Duration FROM Tracks
WHERE Duration >= 03.50;
''').fetchall()
pprint(select_3)

# Найдем названия сборников, вышедших в период с 2018 по 2020 год включительно
select_4 = connection.execute('''SELECT  Name_of_collection FROM Collections
WHERE collect_year_of_issue BETWEEN '2018-01-01' AND '2020-12-31';
''').fetchall()
pprint(select_4)

# Найдем названия исполнителей, чье имя состоит из 1 слова
select_5 = connection.execute('''SELECT Name_of_executors FROM executors
WHERE Name_of_executors NOT LIKE '%% %%';
''').fetchall()
pprint(select_5)

# Найдем название треков, которые содержат слово "мой"/"my"
select_6 = connection.execute('''SELECT Name_of_track FROM Tracks
WHERE Name_of_track LIKE '%%my%%';
''').fetchall()
pprint(select_6)