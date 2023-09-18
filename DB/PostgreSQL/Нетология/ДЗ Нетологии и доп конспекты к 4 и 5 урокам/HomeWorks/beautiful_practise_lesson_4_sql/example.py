import psycopg2
import sqlalchemy
from pprint import pprint

# создаем engine
# dialect+driver://username:password@host:port/database
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
# pprint(engine)

# установим соединение
connection = engine.connect()

# Посмотрим, какие таблицы есть
# pprint(engine.table_names())

# SELECT
# выбираем все поля из таблицы film и выводим первую строчку
sel = connection.execute('''SELECT * FROM film;
''').fetchone()
# pprint(sel)
# pprint(type(sel))

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

# BETWEEN. Найдем фильмы с ценой проката между 0.99 и 2.99
sel18 = connection.execute('''SELECT title, rental_rate FROM film
WHERE rental_rate BETWEEN 0.99 AND 2.99; 
''').fetchmany(10)
# pprint(sel18)

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
# pprint(sel24)

# LIMIT. Выведем первые 15 записей
sel25 = connection.execute('''SELECT title, length, rental_rate FROM film
WHERE rental_rate > 2.99
ORDER BY length DESC, rental_rate
LIMIT 15; 
''').fetchall()
# pprint(sel25)

# Insert. Сначала проверим, что у нас находится в таблице rental
sel26 = connection.execute('''SELECT * FROM rental
''').fetchmany(10)
# pprint(sel26)

# Insert. Добавим новый прокат
sel27 = connection.execute('''INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
    VALUES(NOW(), 1, 3, 2);
''')
# pprint(sel27)
# Проверим
sel28 = connection.execute('''SELECT * FROM rental
    WHERE staff_id = 2 AND inventory_id =1;
''').fetchall()
# pprint(sel28)

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
