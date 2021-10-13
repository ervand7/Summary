# хорошая статья: https://python-scripts.com/redis
import redis
import datetime
import random

r = redis.Redis(db=0)
# r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
print(r.get("Bahamas").decode("utf-8"))

today = datetime.date.today().isoformat()
visitors = {"dan", "jon", "alex"}
# r.sadd(today, *visitors)
print(r.smembers(today))
print(r.scard(today))

# создаем другую базу
r1 = redis.Redis(db=1)
random.seed(444)

