Инструкция по запуску задания №1:

Вариант 1, через Dockerfile:
```
$ cd task_1
$ docker build . -t nginx_change_greetings
$ docker run -d -p 81:80 nginx_change_greetings
```

```
http://localhost:81
```

Вариант 2, через volume:
```
$ docker run -v <абсолютный путь до task_1/html>:/usr/share/nginx/html -d --name nginx_change_greetings -p 81:80 nginx
```
```
http://localhost:81
```
 <hr />
Инструкция по запуску задания №2:

```
$ cd Project-shop/project_shop
$ python manage.py migrate
$ python manage.py loaddata fixtures.json
$ cd ..
$ docker build . -t my_shop
$ docker run -d --name=shop_container -p 7777:7777 my_shop
```
```
http://0.0.0.0:7777/api/v1/
```