запуск postgres контейнера с именем my-postgres-db и паролем my-password:
docker run --name my-postgres-db -e POSTGRES_PASSWORD=my-password -d postgres

собираем образ flask-приложения:
docker build -t ad_api .

запуск контейнера ad_api c переменными среды окружения:
docker run --name my-app -d -p 8080:80 -e DB_NAME=my_name -e DB_PASSWORD=my-password ad_api

создание сети с именем my-network:
docker network create --driver=overlay --attachable my-network

подключение к сети контейнеров:
docker network connect my-network my-postgres-db
docker network connect my-network my-app

команда пинга между контейнерами:
docker exec -ti my-app ping my-postgres-db

результат пинга:
64 bytes from my-postgres-db.my-network (10.0.1.2): icmp_seq=1 ttl=64 time=0.302 ms
64 bytes from my-postgres-db.my-network (10.0.1.2): icmp_seq=2 ttl=64 time=0.128 ms
64 bytes from my-postgres-db.my-network (10.0.1.2): icmp_seq=3 ttl=64 time=0.138 ms
64 bytes from my-postgres-db.my-network (10.0.1.2): icmp_seq=4 ttl=64 time=0.149 ms
64 bytes from my-postgres-db.my-network (10.0.1.2): icmp_seq=5 ttl=64 time=0.143 ms
64 bytes from my-postgres-db.my-network (10.0.1.2): icmp_seq=6 ttl=64 time=0.127 ms

