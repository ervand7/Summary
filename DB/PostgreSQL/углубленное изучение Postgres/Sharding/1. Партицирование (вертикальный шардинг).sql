-- 1) create base table
create table news
(
    id          bigint            not null,
    category_id int               not null,
    author      character varying not null,
    rate        int               not null,
    title       character varying
)
;
create rule news_insert_to_1 as on insert to news
where (category_id = 1)
do instead insert into news_1 values (NEW.*)
;
create rule news_insert_to_2 as on insert to news
where (category_id = 2)
do instead insert into news_2 values (NEW.*)
;

-- 2 ) inherit
create table news_1
(
)
    inherits (news)
;
-- эта таблица будет иметь все колонки родителя + свои колонки
-- не будит иметь ограничений (constraint), индексов и триггеров

-- или
create table news_1
(
    check (category_id = 1)
    -- можно проставить ограничение.
    -- То есть в эту таблицу будут попадать только данные с таким признаком
)
    inherits (news)
;
create table news_2
(
    check (category_id = 2)
)
    inherits (news)
;

-- 3) insert
insert into news (id, category_id, title, author, rate) values (1, 1, 'моя новость #1', 'Ivan', 1)
;
insert into news (id, category_id, title, author, rate) values (2, 2, 'моя новость #2', 'Oleg', 1)
;