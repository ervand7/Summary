-- // user
-- id | firstname | lastname | birth
-- 1  | Ivan      | Petrov   | 1996-05-01
-- 2  | Anna      | Petrova  | 1999-06-01
-- // purchase
-- sku   | price | user_id | date
-- 11111 | 5500  | 1       | 2021-02-15
-- 22222 | 4000  | 1       | 2021-02-14
-- 33333 | 8000  | 2       | 2021-03-01
-- 44444 | 400   | 2       | 2021-03-02
-- // ban_list
-- user_id | date
-- 1       | 2021-03-08
--




-- Список уникальных клиентов, совершивших покупку товаров
-- на сумму больше 5000 и не имеющих бана
create table if not exists "user"
(
    id         serial primary key,
    first_name varchar
)
;

create table if not exists purchase
(
    id      serial primary key,
    price   int,
    user_id int
)
;

create table if not exists ban_list
(
    user_id int
)
;

insert into "user" (id, first_name) values (1, 'ivan');
insert into "user" (id, first_name) values(2, 'vasya');


insert into "purchase" (id, user_id, price) values (1, 1, 123);
insert into "purchase" (id, user_id, price) values (2, 1, 123);
insert into "purchase" (id, user_id, price) values (3, 1, 123);
insert into "purchase" (id, user_id, price) values (4, 2, 3);


insert into "ban_list" (user_id) values (2);


select "user"."id"
from "user"
         join "purchase" on "purchase"."user_id" = "user"."id"
         left outer join "ban_list" on "ban_list"."user_id" = "user"."id"
where "ban_list"."user_id" is null
group by "user"."id"
having sum("price") > 5000
;
