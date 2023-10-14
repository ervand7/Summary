-- 1) create base table
create table news
(
    id          bigint            not null,
    category_id int               not null,
--     добавляем constraint
    constraint category_id_check check (category_id = 1),
    author      character varying not null,
    rate        int               not null,
    title       character varying
)
;
create index news_category_id_idx on news using btree (category_id)
;

-- далее все делаем в консоли:
-- psql -U postgres -d learn_sharding -c "create extension postgres_fdw;"
-- alter database learn_sharding owner to postgres;
create server news_1_server
    foreign data wrapper postgres_fdw
    options (host '127.0.0.1', port '5432', dbname 'news_1')
;

create user mapping for postgres
    server news_1_server
    options (user 'postgres', password 'postgres')
;

create foreign table news_1
    (
        id bigint not null,
        category_id int not null,
        author character varying not null,
        rate int not null,
        title character varying
        )
    server news_1_server
    options (schema_name 'public', table_name 'news')
;

create view news as
select *
from news_1
union all
select *
from news_2
;
