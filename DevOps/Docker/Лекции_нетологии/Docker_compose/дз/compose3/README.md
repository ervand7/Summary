Запуск с ветки master:
```angular2html
$ cd project_shop
$ docker-compose build --no-cache
$ docker-compose up -d
```
Запуск с ветки uliantcev:
```angular2html
$ docker-compose build --no-cache
$ docker-compose up -d
```

http://localhost/api/v1/

Завершение:
```
$ docker-compose down
$ docker volume prune
$ docker rmi $(docker images -q)
```