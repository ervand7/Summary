create table customer(
id serial primary key,
name varchar(255),
phone varchar(30),
email varchar(255)
);

create table product(
id serial primary key,
name varchar(255),
description text,
price integer
);

create table product_photo(
id serial primary key,
url varchar(255),
product_id integer references product(id)
);

create table cart(
id serial primary key,
customer_id integer references customer(id)
);

create table cart_product(
cart_id integer references cart(id),
product_id integer references product(id)
);


insert into customer(name, phone, email) values ('Василий', '02', 'vac@gmail.com');
insert into customer(name, phone, email) values ('Петр', '03', 'petr@gmail.com');
-- select * from customer;

insert into product(name, description, price) values ('iPhone', 'крутой телефон', '100000');
insert into product(name, description, price) values ('Apple watch', 'крутые часы', '50000');
-- select * from product;

insert into product_photo(url, product_id) values ('iphone_photo', 1);
-- select * from product_photo;


alter table product_photo drop constraint product_photo_product_id_fkey;
insert into product_photo (url, product_id) values ('unknown_photo', 100);


select pp.*, p.name from product_photo pp
left join product p on p.id=pp.product_id;

select pp.*, p.name from product_photo pp
right join product p on p.id=pp.product_id;

select pp.*, p.name from product_photo pp
inner join product p on p.id=pp.product_id;

select pp.*, p.name from product_photo pp
full outer join product p on p.id=pp.product_id;

select pp.*, p.name from product_photo pp
full outer join product p on p.id=pp.product_id
where p.name = 'Apple watch'
;
