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
