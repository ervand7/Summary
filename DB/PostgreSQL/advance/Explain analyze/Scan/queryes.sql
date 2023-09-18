CREATE TABLE demotable (num numeric, id int);
CREATE INDEX demoidx ON demotable(num);
INSERT INTO demotable SELECT random() * 1000,  generate_series(1, 1000000);

-- Sequential Scan:
explain analyze SELECT * FROM demotable WHERE num < 21000;

-- Index Scan:
explain SELECT * FROM demotable WHERE num = 21000;

-- Index Only Scan:
explain SELECT num FROM demotable WHERE num = 21000;
explain SELECT num FROM demotable WHERE num < 210;

-- Bitmap Heap Scan:
explain SELECT * FROM demotable WHERE num < 210;

-- TID Scan
explain select * from demotable where ctid=(
    select ctid from demotable where id=21000
    );