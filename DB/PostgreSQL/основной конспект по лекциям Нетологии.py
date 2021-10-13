~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Инструкции по установке PostgreSQL на MAC
ЧЕРЕЗ ТЕРМИНАЛ.

Ссылка на видеоинструкцию: https://videos-bb5ddb7a.cdn.integros.com/videos/5x1n2qgzvEhGTeG71vhmBE/mp4/1080.mp4

Ссылка на скачивание pgadmin для MAC:
https://www.pgadmin.org/download/pgadmin-4-macos/

Открываем терминал:
1) Так brew нет по умолчанию в маке.
На оф.сайте (https://brew.sh/index_ru) прям сверху есть команда для его установки:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

2) brew install postgres

3) postgres -V

4) pg_ctl -D /usr/local/var/postgres start

5) createuser -P -s postgres


```````````````````````````````````````````````
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
```````````````````````````````````````````````
lessons 1, 2
````````````````````````````````````````````
Инструкция по настройке и работе с PostgreSQL
ЧЕРЕЗ ТЕРМИНАЛ.
Работаем по принципу: 1 БД - 1 пользователь.

• psql -U postgres   - пишем, что пользователем у нас будет суперпользователь. В моем компе далее пароль воодить не требуется, все происхдит автоматически. postgres=# - означает, что мы попали в управление

• \? - справка

• \l - показывает все базы данных, которые сейас созданы

• \d - показывает все таблички, которые созданы

• \q - выход из управление БД

• psql -U postgres    - снова заходим в управление от имени postgres

• create user test_user with password 'test_user';       - создаем пользователя. Где create user (создай пользователя) (по имени)test_user with password (с паролем) 'test_user' (пароль обязательно только в одинарные ковычки); (точка с запятой обязательна в конце)

• create database test_database with owner test_user;        - создаем БД, владельцем которой будет наш выше созданный пользователь test_user

• \l - проверяем и видим в списке баз данных только что созданную нами БД test_database

• alter database test_database owner to postgres;      - если вдруг мы хотим сменить владельца. В данном случае мы вернули нашу БД test_database старому владельцу, то есть postgres

• \l - затем снова проверяем и видим, что в списке баз данных изменился владелец базы данных test_database

• alter database test_database owner to test_user;       - опять меняем владельца, теперь снова на test_user







````````````````````````````````````````````
Инструкция по настройке и работе с PostgreSQL
ЧЕРЕЗ GUI.

• Правой кнопкой мыши нажимаем на Login/Group Roles - далее Create - далее Login/Group Role

• Где Genersl прописываем имя нового пользователя (сейчас я прописываю test_user_10)

• Где Definition прописываем свой пароль

• Где Privileges, там "Can login" указываем Yes

• Правой кнопкой мыши нажимаем на Databases - далее Create - далее Database

• Где Genersl прописываем название новой БД (сейчас я прописываю test_db). И в owner выбираем из выпадающего списка выше созданного пользователя test_user_10







````````````````````````````````````````````
Теперь попробуем управлять нашими БД от лица созданного нами test_user
ЧЕРЕЗ ТЕРМИНАЛ.

(ВНИМАНИЕ! ЭТО НЕ СРАБОТАЕТ, ТАК КАК МЫ НЕ ПРОПИСАЛИ БД, В КОТОРУЮ ВХОДИМ)
• psql -U test_user   - входим как test_user,
нас просят ввести пароль от test_user. Мы помним, что у нас пароль от него 'test_user' (только без кавычек), так как ранее мы задавали ему пароль create user test_user with password 'test_user'

• psql -U test_user -d test_database      - входим как определенный пользователь в определенную БД. Мой комп пароль автоматически записывает, у меня не спрашивает.

!!! Обратите внимание, что теперь в начале строки терминала написано test_database=> - такая стрелка (=>) означает, что мы уже не суперпользователь, а обычный пользователь. Суперпользователь у нас с вами раньше обозначался как postgres=# (=# - означает признак суперпользователя)!!!

• \l - покажет все базы данных, которые сейас созданы, но уже всеми мы управлять не можем, так как мы больше не суперпользователь

!!! Вопрос от одногрупника. Как подключиться к postgres, если он не локально стоит, а на виртуалке? Есть флаг -h, в котором прописываете адрем сервера. То такие вещи лучше делать через GUI
Пример выполнения через терминал:
psql -h 172.12.40.12 -U test_user -d test_database
!!!







````````````````````````````````````````````
Создадим таблицы
ЧЕРЕЗ ТЕРМИНАЛ. Но лучше этого не делать, а делать сразу в GUI.

• psql -U test_user -d test_database     - входим

Начинаем создавать табличку "Категория". Осуществляем ввод в несколько строк, после ввода каждой строки нажимаем Enter:
• create table if not exists Category (
  Id serial primary key,
  Name varchar(60) not null unique
  );

• \d - видим, что у нвс создалась новая таблица







````````````````````````````````````````````
Создадим таблицы
ЧЕРЕЗ GUI.

• Нажимаем правой кнопкой мыши на нажу БД test_database и выбираем Query Tool

• create table if not exists Product_44 (
    Id serial primary key,
    Name varchar(100) not null,
    Prise numeric not null,
    CategoryId integer references Category(Id)
    );

  create table if not exists review (
    Id serial primary key,
    Author varchar(60) not null,
    Rating integer not null check(Rating >= 1 and Rating <= 5),
    Text text,
    ProductId integer references Product_44(Id)
    );

• drop table <name of table> - удалить таблицу. Может не получиться удалить таблицу, если на нее уже ссылается другая таблица

• alter table <name of table> <Действия, которые можно совершить (см. в презентации)> - произвести различные изменения с таблицей

```````````````````````````````````````````````
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
```````````````````````````````````````````````
lesson 3 - см. презентацию
````````````````````````````````````````````
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
````````````````````````````````````````````
lesson 4
````````````````````````````````````````````
Attention!!! The most better variant of realization the code practice of this lesson is here. My special summary with working code examples:
```
https://github.com/ervand7/sql_lessons_1-5_my_summary/blob/master/beautiful_summary_lesson_4.py
```
````````````````````````````````````````````

#____
During the lection we will use this materials:
1)  https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/pagila/pagila/

2)
https://dataedo.com/samples/html/Pagila/doc/Pagila_10/modules/Paglia_database_diagram_103/module.html

3) installing next libraries: psycopg2, SQLAlchemy. If you have any problems with installing psycopg2, use this command:
pip install psycopg2-binary
#____

#____
Инструкция по импорту данных в pgAdmin.

Все импортированные даные по умолчанию импортируются в public. Для урока лучше всего использовать БД суперпользователя postgres, а то будет проблема с доступом к таблицам
```
psycopg2.errors.InsufficientPrivilege: permission denied for table.
```
Важно еще подключиться к нужной БД через питон и все параметры правильно ввести.
Вот как у меня выглядит правильный коннект к базе, где пользователь - суперпользователь:
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
pprint(engine)
Где:
1) engine = sqlalchemy.create_engine - это создание экземпляра класса engine с помощью функции .create_engine из библиотеки sqlalchemy
2) postgresql - это программа, которая у меня на маке стоит, с помощью которой я пользуюсь pgAdmin. В презентации этот элемент называется как dialect+driver
3) postgres:postgres - это суперпользователь и его пароль
4) localhost:5432 - так и прописываем
5) последний postgres - это название нашей БД, владельцем которой является суперпользователь
Ну и в итоге получается:
```
dialect+driver://username:password@host:port/database
```

Юрий Батраков дал мне ссылку
```
https://github.com/devrimgunduz/pagila/raw/master/pagila-insert-data.sql
```
чтобы не по одному файлу скачивать а мгновенно все импортировать.
#____

#____
||||| SQLAlchemy |||||
SQLAlchemy – это программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM.
Для подключения к базе данных нужно создать экземпляр класса Engine с помощью create_engine(),которая в качестве аргумента принимает адрес в виде:
dialect+driver://username:password@host:port/database
Потом инициализировать подключение к базе при помощи метода connect().
Например:
db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
#____

#____
||||| Запросы через библиотеку SQLAlchemy |||||
Для выполнение SQL запросов к подключенной БД используется метод execute(). Для получения результатов  можно использовать один из fetch методов, которые возвращают список объектов RowProxy (значений строк таблицы)
fetchone() – извлечение 1 строки,
fetchall() – извлечение всех строк,
fetchmany(n) – извлечение заданного количества строк

Например:
connection.execute("SELECT * FROM database;").fetchmany(10)
#____

#____
||||| SELECT-запросы |||||

SELECT-запросы предназначены для отбора необходимых строк или столбцов из одной или нескольких таблиц. Общий вид структуры select-запроса:
 - Обязательные элементы запроса:
SELECT [DISTINCT | ALL] table_columns
FROM table
 - Необязательные элементы запроса в строгой последовательности:
[WHERE condition]
[GROUP BY table_columns]
[HAVING condition]
[ORDER BY table_columns [ASC | DESC]]
[LIMIT number]
#____

#____
||||| SELECT-запросы, DISTINCT |||||

SELECT * FROM table;
* – выбор всех столбцов таблицы;
table – имя нужной таблицы.

Через запятую можно перечислить имена необходимых столбцов:
SELECT title, release_year FROM film;

Оператор DISTINCT позволяет выбирать только уникальные значения из базы данных —  он отсеивает дубли:
SELECT DISTINCT rating FROM film;
#____

#____
||||| Теперь попробуем все это реализовать в коде |||||
Attention!!! The most better variant of realization the code practice of this lesson is here. My special summary with working code examples:
```
https://github.com/ervand7/beauiful_practice_lesson_4_sql/blob/master/example.py
```

import psycopg2
import sqlalchemy
from pprint import pprint

# создаем engine
# dialect+driver://username:password@host:port/database
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
pprint(engine)

# установим соединение
connection = engine.connect()

# Посмотрим, какие таблицы есть
# pprint(engine.table_names())

# SELECT
# выбираем все поля из таблицы film и выводим первую строчку
sel = connection.execute('''SELECT * FROM film;
''').fetchone()
# pprint(sel)
# print(type(sel))

# Выберем столбец title таблицы film
sel2 = connection.execute('''SELECT title FROM film;
''').fetchmany(10)
# pprint(sel2)

# Выберем 2 столбца из таблицы film
sel3 = connection.execute('''SELECT title, release_year FROM film;
''').fetchmany(10)
# pprint(sel3)

# Выведем имена и фамилии актеров
sel4 = connection.execute('''SELECT first_name, last_name FROM actor;
''').fetchall()
# pprint(sel4)

# Как работает DISTINCT
# Выведем столбик rating из film
sel5 = connection.execute('''SELECT rating FROM film;
''').fetchmany(10)
# print(sel5)
# Найдем, какие уникальные рейтинги бывают с помощью DISTINCT
sel6 = connection.execute('''SELECT DISTINCT rating FROM film;
''').fetchall()
# print(sel6)
#____

#____
Арифметические операторы
Можно использовать различные арифметические операторы
для данных, хранящихся в таблицах:
● + сложение
● - вычитание
● / деление
● * умножение
● % взятие остатка от деления

# Примеры с арифметикой
# Переведем цены в условные рубли. Попробуем умножить столбец amount на число
sel7 = connection.execute('''SELECT amount * 70 FROM payment;
''').fetchmany(10)
# pprint(sel7)

# Мы можем делать операции не только над числами, но и между столбцами
# Узнаем время аренды по позициям
sel8 = connection.execute('''SELECT rental_date - return_date FROM rental;
''').fetchmany(10)
# pprint(sel8)
#____

#____
||||| Оператор WHERE |||||

Оператор WHERE нужен для фильтрации таблиц по условиям. В качестве условий можно использовать:
● сравнения (=, >, <, >=, <=, !=)

С условиями можно применять логические операторы and, or и not:
● Оператор AND отображает запись, если оба операнда истинны
● Оператор OR отображает запись, если хотя бы один операнд истинен
● Оператор NOT инвертирует исходный операнд

Примеры запросов с отбором по сравнению:
SELECT title, release_year FROM film
    WHERE release_year >= 2000;

SELECT first_name, last_name, active FROM staff
    WHERE NOT active = true;

SELECT title, rental_rate, replacement_cost FROM film
    WHERE rental_rate <= 0.99 AND replacement_cost <= 9.99;

# Оператор WHERE. Найдем фильмы, вышедшие после 2000 года
sel9 = connection.execute('''SELECT title, release_year FROM film
WHERE release_year >= 2000;
''').fetchall()
# pprint(sel9)

# Найдем сотрудников, которые сейчас работают. Внимание критерий отбора (в данном случае active
# не обязательно должен входить в выборку. И без этого все будет работать
sel10 = connection.execute('''SELECT first_name, last_name, active FROM staff
WHERE active = true;
''').fetchall()
# pprint(sel10)

# Найдем id, имена, фамилии актеров которых зовут JOE
sel11 = connection.execute('''SELECT actor_id, first_name, last_name FROM actor
WHERE first_name = 'JOE';
''').fetchmany(10)
# pprint(sel11)

# Найдем всех сотрудников, которые работают не во втором магазине
sel12 = connection.execute('''SELECT first_name, last_name FROM staff
WHERE store_id != 2;
''').fetchmany(10)
# pprint(sel12)

# Найдем только работающих сотрудников из всех магазинов кроме 1
sel13 = connection.execute('''SELECT first_name, last_name FROM staff
WHERE active = true AND NOT store_id = 1; 
''').fetchmany(10)  # тут равносильно можно было написать WHERE active = true AND store_id != 1;
# pprint(sel13)

# Найдем фильмы, цена проката которых меньше 0,99, а цена возмещения меньше 9,99
sel14 = connection.execute('''SELECT title, rental_rate, replacement_cost FROM film
WHERE rental_rate <= 0.99 AND replacement_cost <= 9.99; 
''').fetchmany(10)
# pprint(sel14)

# Найдем фильмы, аналогичные предыдущему примеру или продолжительностью менее 30 минут
sel15 = connection.execute('''SELECT title, length, rental_rate, replacement_cost FROM film
WHERE length <= 30 OR rental_rate <= 0.99 AND replacement_cost <= 9.99; 
''').fetchmany(10)
# pprint(sel15)
#____

#____
||||| Оператор IN |||||

Оператор IN отбирает строки, в которых есть перечисленные значения. Если значений много — они перечисляются через запятую. Например:
SELECT title, description, rating FROM film
     WHERE rating IN ('R', 'NC-17');

SELECT title, description, rating FROM film
    WHERE rating NOT IN ('G', 'PG');

# IN. Найдем все фильмы с рейтингом R, NC-17
sel16 = connection.execute('''SELECT title, description, rating FROM film
WHERE rating IN ('R', 'NC-17'); 
''').fetchmany(10)
# pprint(sel16)

# NOT IN. Найдем фильмы недетского рейтинга, которых нет в 'G' и 'PG'
sel17 = connection.execute('''SELECT title, description, rating FROM film
WHERE rating NOT IN ('G', 'PG'); 
''').fetchmany(10)
# pprint(sel17)
#____

#____
||||| Оператор BETWEEN |||||
Оператор BETWEEN позволяет проверить, находится ли выражение в диапазоне значений. Крайние значения включаются в диапазон.
Например:
SELECT title, rental_rate FROM film
    WHERE rental_rate BETWEEN 0.99 AND 1.99;

SELECT title, rental_rate FROM film
    WHERE rental_rate NOT BETWEEN 0.99 AND 1.99;

# BETWEEN. Найдем фильмы с ценой проката между 0.99 и 2.99
sel18 = connection.execute('''SELECT title, rental_rate FROM film
WHERE rental_rate BETWEEN 0.99 AND 2.99; 
''').fetchmany(10)
# pprint(sel18)
#____

#____
||||| Оператор LIKE |||||

Оператор LIKE позволяет проверить, находится ли в значении заданный текстовый шаблон.
В шаблонах кроме обычных символов могут использоваться два служебных:
● '%' – ноль, один или несколько любых символов
● '_' – один любой символ.

Важно. В python знак % зарезервирован, поэтому необходимо использовать %%
Например:
SELECT title, description FROM film
    WHERE description LIKE '%%Scientist%%';

# LIKE. Найдем фильмы, в описании которых есть слово 'Scientist'
sel19 = connection.execute('''SELECT title, description FROM film
WHERE description LIKE '%%Scientist%%'; 
''').fetchmany(10)
# pprint(sel19)

# Найдем id, имена, фамилии актеров, фамилия которых начинается с GEN
sel20 = connection.execute('''SELECT actor_id, first_name, last_name FROM actor
WHERE last_name LIKE '%%GEN%%'; 
''').fetchmany(10)
# pprint(sel20)
#____

#____
||||| Сортировка при помощи ORDER BY |||||
ORDER BY используется для сортировки таблицы по указанным столбцам.

Внимание. Если в запросе есть WHERE, то ORDER BY в запросе всегда будет идти после WHERE
Например:
по умолчанию сортировка всегда идет по возрастанию
SELECT title, rental_rate FROM film
    ORDER BY rental_rate;

если добавим вконце оператор DESC, то сортировка будет идти по убыванию
SELECT title, rental_rate FROM film
    ORDER BY rental_rate DESC;

и можно сортировать по двум столбцам одновременно, если, к примеру, по первому есть совпадения
SELECT title, length, rental_rate FROM film
    ORDER BY length DESC, rental_rate;

# ORDER BY. Отсортируем фильмы по цене проката
sel21 = connection.execute('''SELECT title, rental_rate FROM film
ORDER BY rental_rate; 
''').fetchall()
# pprint(sel21)

# Все то же самое, только добавим DESC и просортируем по убыванию
sel22 = connection.execute('''SELECT title, rental_rate FROM film
ORDER BY rental_rate DESC; 
''').fetchall()
# pprint(sel22)

# Сортируем по нескольким столбцам. По продолжительности и по цене проката
# Там где продолжительность одинаковая, будем сортировать по цене проката
sel23 = connection.execute('''SELECT title, length, rental_rate FROM film
ORDER BY length DESC, rental_rate DESC; 
''').fetchall()
# pprint(sel23)

# Найдем id, имена, фамилии актеров, чья фамилия содержит 'LI', отсортируем в алфавитном
# порядке по фамилии, затем по имени
sel24 = connection.execute('''SELECT actor_id, first_name, last_name FROM actor
WHERE last_name LIKE '%%LI%%'
ORDER BY last_name, first_name; 
''').fetchall()
pprint(sel24)
#____

#____
||||| Оператор LIMIT |||||

Если в питоне мы ставили ограничения благодаря методу fetch, который входит в библиотеку sqlalchemy, то в чистом sql мы будем использовать для этого оператор LIMIT

LIMIT используется, чтобы ограничивать количество возвращаемых записей изодной или нескольких таблиц.
Например:
SELECT title, length, rental_rate FROM film
    WHERE rental_rate > 2.99
    ORDER BY length DESC, rental_rate
    LIMIT 15;

# LIMIT. Выведем первые 15 записей
sel25 = connection.execute('''SELECT title, length, rental_rate FROM film
WHERE rental_rate > 2.99
ORDER BY length DESC, rental_rate
LIMIT 15; 
''').fetchall()
pprint(sel25)
#____

#____
``````````````````````````````````````````````````````````
            INSERT/UPDATE/DELETE запросы

||||| INSERT INTO |||||
Инструкция INSERT INTO используется для вставки новых записей в таблицу.

Если необходимо вставить значения только для части полей, то используется следующий синтаксис:
INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
    VALUES(NOW(), 1, 3, 2);

Если необходимо вставить значения для всех полей, то нужно убедиться, что они все перечислены и их порядок соответствуют порядку полей:
INSERT INTO inventory
    VALUES(999, 999, 999);

# Insert. Сначала проверим, что у нас находится в таблице rental
sel26 = connection.execute('''SELECT * FROM rental
''').fetchmany(10)
# pprint(sel26)

# Добавим новый прокат
sel27 = connection.execute('''INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
    VALUES(NOW(), 1, 3, 2);
''')
# pprint(sel27)
# Проверим
sel28 = connection.execute('''SELECT * FROM rental
    WHERE staff_id = 2 AND inventory_id =1;
''').fetchall()
# pprint(sel28)
#____

#____
||||| UPDATE |||||
UPDATE используется для изменения существующих записей в одной илинескольких таблицах.
Внимание. Можно изменять одновременно несколько полей. Без указания WHERE будут изменены все записи в столбце.

После оператора SET указывается изменяемый столбец, принеобходимости можно добавить изменения по условиям:
UPDATE rental
  SET return_date = NOW()
  WHERE rental_id = 16053;

# UPDATE. Добавим возврат из проката
sel29 = connection.execute('''UPDATE rental
        SET return_date = NOW()
        WHERE rental_id = 16059;
''')
# pprint(sel29)
# Проверим
sel30 = connection.execute('''SELECT * FROM rental
    WHERE staff_id = 2 AND inventory_id =1;
''').fetchall()
# pprint(sel30)

# # INSERT можно комбнировать с SELECT, чтобы скопировать данные из одной таблицы в другую
# INSERT INTO table2
# SELECT * FROM table1
# WHERE condition;
#____

#____
||||| DELETE |||||

DELETE используется для удаления существующих записей в таблице.
Например:
DELETE FROM rental
    WHERE rental_id = 16050;
Внимание. Без указанияWHERE будут удалены все записи в столбце.

# DELETE. Удалим данные
sel31 = connection.execute('''DELETE FROM rental
    WHERE rental_id = 16062;
''')
# pprint(sel31)
# Проверим
sel32 = connection.execute('''SELECT * FROM rental
    WHERE rental_id = 16062;
''').fetchall()
# pprint(sel32)
````````````````````````````````````````````
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
````````````````````````````````````````````
lesson 5
````````````````````````````````````````````
Attention!!! The most better variant of realization the code practice of this lesson is here. My special summary with working code examples:
```
https://github.com/ervand7/sql_lessons_1-5_my_summary/blob/master/beautiful_summary_lesson_5.py
```
````````````````````````````````````````````
import psycopg2
import sqlalchemy
from pprint import pprint

# создаем engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
# print(engine)
con = engine.connect()
# print(con)
# ____

# ____
# Агрегирующие функции
# Агрегирующие функции выполняют вычисления над значениями в столбце.
# Существует 5 таких функций:
# ● SUM() – вычисляет сумму значений
# ● MIN() – вычисляет минимальное значение
# ● MAX() – вычисляет максимальное значение
# ● AVG() – вычисляет среднее значение
# ● COUNT() — вычисляет количество строк в столбце.

# # найдем максимальную стоимость проката
sel_1 = con.execute("""
SELECT MAX(rental_rate) FROM film
""").fetchall()
# pprint(sel_1)

# # посчитаем среднюю продолжительность фильма
sel_2 = con.execute("""
SELECT AVG(length) FROM film
""").fetchall()
# pprint(sel_2)

# # сколько уникальных имен актеров?
sel_3 = con.execute("""
SELECT COUNT(DISTINCT first_name) FROM actor
""").fetchall()
# pprint(sel_3)

# # посчитаем сумму продаж и среднюю продажу по конкретному продавцу
sel_4 = con.execute("""
SELECT SUM(amount), AVG(amount) FROM payment
WHERE staff_id = 1;
""").fetchall()
# pprint(sel_4)
# ____

# ____
# # Вложенные запросы
# # Вложенный запрос – запрос, который используется внутри другого запроса.
# Каждый вложенный запрос так же может содержать один или несколько вложенных запросов.
# Количество вложенных запросов неограничено. Вложенные подзапросы обрабатываются «снизу вверх».
# Сначала обрабатывается вложенный запрос самого нижнего уровня. Далее значения, полученные по
# результату его выполнения, передаются и используются при исполнении подзапроса
# более высокого уровня и т.д.
# Например:
# SELECT title, length  FROM film  -- данный запрос будет выполнен вторым
#   WHERE length >= (
#       SELECT AVG(length) FROM film); -- сначала будет выполнен этот запрос

# # найдем все фильмы с продолжительностью ваше среднего
# # так работать не будет потому что агрегирующие функции должны идти сразу после SELECT,
# иначе мы получим ошибку aggregate functions are not allowed in WHERE. То
# есть агрегатные функции нельзя применять в конструкции WHERE
# sel_5 = con.execute("""
# SELECT title, length  FROM film
# WHERE length >= AVG(length)
# """).fetchall()
# pprint(sel_5)
# поэтому мы делаем вложенный запрос
sel_6 = con.execute("""
SELECT title, length FROM film
WHERE length >= (
    SELECT AVG(length) FROM film)
""").fetchall()
# pprint(sel_6)

# найдем названия фильмов, стоимость проката которых не максимальная
sel_7 = con.execute("""SELECT title, rental_rate FROM film
WHERE rental_rate < (
    SELECT MAX(rental_rate) FROM film)
ORDER BY rental_rate DESC
""").fetchall()  # ORDER BY rental_rate DESC - относится к первому уровню
# pprint(sel_7)
# ____

# ____
# GROUP BY
# GROUP BY – оператор, с помощью которого можно задать агрегацию по нужным столбцам.
# Применяется в связке с агрегирующими функциями.
# SELECT rating, COUNT(title) FROM film
#   GROUP BY rating;

# SELECT rating, AVG(length) FROM film
#   WHERE release_year = 2006
#       GROUP BY rating;
# Группировочные столбцы должны обязательно присутствовать в SELECT

# # посчитаем количество актеров в разрезе фамилий (кол-во актеров у фамилий) (найдем однофамильцев)
sel_8 = con.execute("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name;
""").fetchall()
# pprint(sel_8)

# # посчитаем количество фильмов в разрезе рейтингов (кол-во фильмов у рейтингов)
sel_9 = con.execute("""
SELECT rating, COUNT(title) FROM film
GROUP BY rating;
""").fetchall()
# pprint(sel_9)

# # найдем максимальные продажи в разрезе продавцов (у каждого продавца была макс. продажа)
sel_10 = con.execute("""
SELECT staff_id, MAX(amount) FROM payment
GROUP BY staff_id;
""").fetchall()
# pprint(sel_10)

# # найдем минимальные продажи у каждого продавца каждому покупателю
sel_11 = con.execute("""
SELECT staff_id, customer_id, MIN(amount) FROM payment
GROUP BY staff_id, customer_id;
""").fetchall()
# pprint(sel_11)

# # найдем среднюю продолжительность фильма в разрезе рейтингов в 2006 году
# (сред. прод. фильма у рейтингов только в 2006 году)
sel_12 = con.execute("""
SELECT rating, AVG(length) FROM film
WHERE release_year = 2006
GROUP BY rating;
""").fetchall()
# pprint(sel_12)
# ____

# ____
# # Оператор HAVING
# HAVING – оператор, позволяющий отфильтровать данные после
# группировки (является аналогом WHERE).
# SELECT last_name FROM actor
#   GROUP BY last_name
#       HAVING COUNT(last_name) = 1;
# Не путайте: WHERE фильтрует данные до группировки, а HAVING после.

# # отберем только фамилий актеров, которые не повторяются
sel_13 = con.execute("""
SELECT last_name FROM actor
GROUP BY last_name
HAVING COUNT(last_name) = 1;
""").fetchall()
# pprint(sel_13)

# # отберем и посчитаем только фамилии актеров, которые повторяются
sel_14 = con.execute("""
SELECT last_name, COUNT(last_name) FROM actor
GROUP BY last_name
HAVING count(last_name) > 1;
""").fetchall()
# pprint(sel_14)

# # найдем фильмы, у которых есть SUPER в названии и они сдавались в прокат
# суммарно более, чем на 5 дней
sel_15 = con.execute("""
SELECT title, SUM(rental_duration) FROM film
WHERE title LIKE '%%SUPER%%'
GROUP BY title
HAVING SUM(rental_duration) > 5;
""").fetchall()
# pprint(sel_15)
# ____

# ____
# # ALIAS
# Alias (псевдонимы) используются для временного переименования таблиц и столбцов.
# Это необязательный функционал, но может быть очень полезным и удобным, когда имена длинные
# и сложные или они повторяются много раз в рамках запроса (пригодится при объединении!).
# По этой причине псевдонимы делают максимально краткими.
# SELECT column_name [AS] column_alies
#   FROM table_name [AS] table_alies
# Оператор AS является необязательным.
# При использовании псевдонимов важно знать и помнить о техническом порядке исполнения запросов.
# WHERE и HAVING исполняются до SELECT, поэтому в них псевдонимы использовать не получится.

# # Предыдущий запрос с псевдонимами
sel_16 = con.execute("""
SELECT title t, SUM(rental_duration) sum_t FROM film f
WHERE title LIKE '%%SUPER%%'
GROUP BY t
HAVING SUM(rental_duration) > 5;
""").fetchall()
# pprint(sel_16)
# ____

# ____
# # Объединение таблиц
# См. презентацию
# JOIN – оператор, предназначенный для объединения таблиц по определенному столбцу
# или связке столбцов (как правило, по первичному ключу).
# JOIN записывается после FROM и до WHERE.
# Через оператор ON необходимо явно указывать столбцы, по которым происходит объединение.
# В общем виде структура запросы с JOIN выглядит так:
# SELECT tables_columns FROM table_1
# JOIN table_2 ON table_1.column = table_2.column;

# Основные виды JOIN
# [INNER] JOIN – в выборку попадут только те данные, по которым выполняются условия соединения;
# Своеобразное пересечение множеств &. Слово INNER можно не писать, оно идет по умолчанию

# LEFT [OUTER] JOIN – в выборку попадут все данные из таблицы A и только те данные из
# таблицы B, по которым выполнится условие соединения. Недостающие данные
# вместо строк таблицы B будут представлены NULL.RIGHT

# [OUTER] JOIN – в выборку попадут все данные из таблицы B и только те данные из таблицы А,
# по которым выполнится условие соединения. Недостающие данные вместо строк таблицы A
# будут представлены NULL.

# FULL [OUTER] JOIN – в выборку попадут все строки таблицы A и таблицы B.
# Если для строк таблицы A и таблицы B выполняются условия соединения, то они объединяются в
# одну строку. Если данных в какой-то таблице не имеется, то на соответствующие
# места вставляются NULL. Своеобразное объединение множеств |

# # LEFT JOIN. Выведем имена, фамилии и адреса всех сотрудников
sel_17 = con.execute("""
SELECT first_name, last_name, address FROM staff s
LEFT JOIN address a ON s.address_id = a.address_id;
""").fetchall()
# pprint(sel_17)

# # LEFT JOIN. Определим количество продаж каждого продавца
sel_18 = con.execute("""
SELECT p.staff_id, COUNT(amount) FROM payment p
LEFT JOIN staff s ON p.staff_id = s.staff_id
GROUP BY p.staff_id;
""").fetchall()
# pprint(sel_18)

# # посчитаем, сколько актеров играло в каждом фильме
sel_19 = con.execute("""
SELECT title, COUNT(actor_id) FROM film f
JOIN film_actor a ON f.film_id = a.film_id
GROUP BY f.title;
""").fetchall()
# pprint(sel_19)

# # сколько копии фильмов со словом SUPER в названии есть в наличии
sel_20 = con.execute("""
SELECT title, COUNT(inventory_id) FROM film f
JOIN inventory i ON f.film_id = i.film_id
WHERE f.title LIKE '%%SUPER%%'
GROUP BY title;
""").fetchall()
# pprint(sel_20)

# # выведем список покупателей с количеством их покупок
sel_21 = con.execute("""
SELECT c.last_name, COUNT(p.amount) FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY  c.last_name;
""").fetchall()
# pprint(sel_21)

# # выведем имена и почтовые адреса всех покупателей из России
sel_22 = con.execute("""
SELECT c.last_name, c.first_name, c.email FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ON a.city_id = city.city_id
JOIN country co ON city.country_id = co.country_id
WHERE country = 'Russian Federation';
""").fetchall()
# pprint(sel_22)

# # фильмы, которые берут в прокат чаще всего
sel_23 = con.execute("""
SELECT f.title, COUNT(r.inventory_id) count FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY count DESC;
""").fetchall()
# pprint(sel_23)

# # суммарные доходы магазинов
sel_24 = con.execute("""
SELECT s.store_id, SUM(p.amount) sales FROM store s
JOIN staff st ON s.store_id = st.store_id
JOIN payment p ON st.staff_id = p.staff_id
GROUP BY s.store_id;
""").fetchall()
# pprint(sel_24)

# # найдем города и страны каждого магазина
sel_25 = con.execute("""
SELECT store_id, city, country FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ON a.city_id = city.city_id
JOIN country c ON city.country_id = c.country_id;
""").fetchall()
# pprint(sel_25)

# # выведем топ-5 жанров по доходу
sel_26 = con.execute("""
SELECT c.name, SUM(p.amount) revenue FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY revenue DESC
LIMIT 5;
""").fetchall()
# pprint(sel_26)

# Сайты для практики: sql-ex.ru learndb.ru
````````````````````````````````````````````
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
````````````````````````````````````````````
