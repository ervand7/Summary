# прекраснейший туториал со ссылками на углубленную документацию (источник этого конспекта):
# https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient, ASCENDING
import datetime
from pprint import pprint
from bson.objectid import ObjectId

# устанавливаем соединение
client = MongoClient('localhost', 27017)  # or: client = MongoClient('mongodb://localhost:27017/')
# создаем БД
my_db = client.test_database  # or: my_db = client['test-database']
# создаем коллекцию (таблицу)
collection = my_db.test_collection  # collection - это аналог таблице реляционной БД
# print(collection)
# создаем запись, которую потом будем вставлять в коллекцию
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# создаем коллекцию (таблицу)
my_posts = my_db.my_posts
# вставляем в нее поля со значениями и сразу возвращаем _id
post_id = my_posts.insert_one(post).inserted_id

print(post_id)
print(my_db.list_collection_names())  # получаем название коллекции
pprint(my_posts.find_one())  # получаем первую коллекцию
pprint(my_posts.find_one({"author": "Mike"}))  # получаем первую запись, где в ключе author значение Mike
pprint(my_posts.find_one({"author": "Eliot"}))  # None
print(post_id)  # получаем _id
pprint(my_posts.find_one({"_id": post_id}))  # получаем первую запись по _id


# _____________________________________________________________________
# Напишем функцию для конвертации from string to ObjectId
def convert(our_post_id):
    document = my_posts.find_one({'_id': ObjectId(our_post_id)})
    return document


# print(convert(post_id))
# _____________________________________________________________________

# Вставим за раз несколько коллекций
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = my_posts.insert_many(new_posts)
print(result.inserted_ids)

# _____________________________________________________________________
# Поитерируемся
for post in my_posts.find():
    pprint(post)

for post in posts.find({"author": "Mike"}):
    pprint(post)

print(my_posts.count_documents({}))  # получаем общее кол-во полей в коллекции
print(my_posts.count_documents({"author": "Eliot"}))  # получаем общ. кол-во полей где у ключа "author" значение "Eliot"

certain_date = datetime.datetime(2009, 11, 12, 12)
for post in my_posts.find({"date": {"$lt": certain_date}}).sort("author"):
    pprint(post)

# _____________________________________________________________________
# Создаем индексы
res = my_db.my_posts.create_index([('user_id', ASCENDING)],
                                  unique=True)
print(res)
print(sorted(list(my_db.my_posts.index_information())))

user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
resultat = my_db.my_posts.insert_many(user_profiles)
print(resultat)
