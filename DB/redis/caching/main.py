# https://www.youtube.com/watch?v=KMY7uZmpdwA&t=23s
"""
 - docker run --name ervand-redis -d -p 6379:6379 redis
 - pip install redis
create table if not exists friends
(
    id   integer primary key,
    name character varying
);

insert into friends (name)
values ('Ivan'),
       ('Vasya'),
       ('Petya')
;
"""
import json
import sqlite3

import redis


def get_my_friends():
    redis_client = redis.Redis()
    cache_value = redis_client.get("friends")
    if cache_value is not None:
        result = json.loads(cache_value)
        redis_client.close()
        print("Result from redis")
        return result

    connection = sqlite3.connect(database='database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM friends;")
    result = cursor.fetchall()
    redis_client.set("friends", json.dumps(result), ex=10)
    redis_client.close()
    cursor.close()

    print("Result from main db")
    return result


if __name__ == '__main__':
    print(get_my_friends())
