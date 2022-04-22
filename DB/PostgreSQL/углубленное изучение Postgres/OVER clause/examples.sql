--=============== МОДУЛЬ 5. РАБОТА С POSTGRESQL =======================================
--======== ОСНОВНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--Сделайте запрос к таблице payment и с помощью оконных функций добавьте вычисляемые колонки согласно условиям:
--Пронумеруйте все платежи от 1 до N по дате
select customer.customer_id,
       payment.payment_id,
       payment.payment_date,
       row_number() over (order by payment.payment_date ) as column_1
from customer
         left outer join payment on customer.customer_id = payment.customer_id
limit 20
;

--Пронумеруйте платежи для каждого покупателя, сортировка платежей должна быть по дате
select customer.customer_id,
       payment.payment_id,
       payment.payment_date,
       row_number() over (partition by customer.customer_id  order by payment.payment_date) as column_2
from customer
         left outer join payment on customer.customer_id = payment.customer_id
limit 200
;

--Посчитайте нарастающим итогом сумму всех платежей для каждого покупателя, сортировка должна
--быть сперва по дате платежа, а затем по сумме платежа от наименьшей к большей
-- ДЛЯ ОТЛАДКИ:
----- -- select customer.customer_id, sum(payment.amount) from customer
----- -- left join payment on customer.customer_id = payment.customer_id
----- -- group by customer.customer_id
----- -- ;
----- --
----- -- select * from payment where payment_id = '19399'
----- -- ;
select customer.customer_id,
       payment.payment_id,
       payment.payment_date,
       sum(payment.amount) over (partition by customer.customer_id) as column_3
from customer
         left join payment on customer.customer_id = payment.customer_id
order by payment.payment_date, column_3
;

--Пронумеруйте платежи для каждого покупателя по стоимости платежа от наибольших к меньшим
--так, чтобы платежи с одинаковым значением имели одинаковое значение номера.
--Можно составить на каждый пункт отдельный SQL-запрос, а можно объединить все колонки в одном запросе.
select customer.customer_id,
       payment.payment_id,
       payment.payment_date,
       payment.amount,
       rank() over (partition by customer.customer_id  order by payment.amount desc ) as column_4
from customer
         left join payment on customer.customer_id = payment.customer_id
;


--ЗАДАНИЕ №2
--С помощью оконной функции выведите для каждого покупателя стоимость платежа и стоимость
--платежа из предыдущей строки со значением по умолчанию 0.0 с сортировкой по дате.
-- НАГЛЯДНО БУДЕТ С СОРТИРОВКОЙ ПО customer.customer_id
select customer.customer_id,
       payment.payment_date,
       payment.amount as "стоимость платежа",
       lag(payment.amount, 1, 0.0) over () as "Стоимость предыдущего платежа"
from customer
         left join payment on customer.customer_id = payment.customer_id
order by payment.payment_date
;


--ЗАДАНИЕ №3
--С помощью оконной функции определите, на сколько каждый следующий платеж покупателя больше или меньше текущего.
select customer.customer_id,
       payment.amount as "Стоимость платежа",
       lag(payment.amount, 1, 0.0) over () as "Стоимость предыдущего платежа",
       payment.amount - lag(payment.amount, 1, 0.0) over () as "Текущий > предыдущего на"
from customer
         left join payment on customer.customer_id = payment.customer_id
order by customer.customer_id
;

--ЗАДАНИЕ №4
--С помощью оконной функции для каждого покупателя выведите данные о его последней оплате аренды.
select customer.customer_id,
       rental.rental_id,
       max(rental.rental_date)  over (partition by customer.customer_id)
from customer
left join rental on customer.customer_id = rental.customer_id
order by customer_id
;


--======== ДОПОЛНИТЕЛЬНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--С помощью оконной функции выведите для каждого сотрудника сумму продаж за август 2005 года
--с нарастающим итогом по каждому сотруднику и по каждой дате продажи (без учёта времени)
--с сортировкой по дате.


--ЗАДАНИЕ №2
--20 августа 2005 года в магазинах проходила акция: покупатель каждого сотого платежа получал
--дополнительную скидку на следующую аренду. С помощью оконной функции выведите всех покупателей,
--которые в день проведения акции получили скидку


--ЗАДАНИЕ №3
--Для каждой страны определите и выведите одним SQL-запросом покупателей, которые попадают под условия:
-- 1. покупатель, арендовавший наибольшее количество фильмов
-- 2. покупатель, арендовавший фильмов на самую большую сумму
-- 3. покупатель, который последним арендовал фильм



