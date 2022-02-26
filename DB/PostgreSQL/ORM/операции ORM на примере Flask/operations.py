#  В библиотеке все методы находятся по этому адресу:
# Desktop/env для всего/venv/lib/python3.8/site-packages/sqlalchemy/orm/query.py

from app import db, User, Ad

# получение всех пользователей. Есть 2 варианта
all_users = User.query.all()
all_users2 = db.session.query(User).all()
comparison = all_users == all_users2

# получение первой записи
first = User.query.first()

# фильтрация через filter_by
filter_by_product = User.query.filter_by(id=2).all()

# фильтрация через filter
filter_query = User.query.filter(User.id == 1).all()
filter_query2 = User.query.filter(User.id > 1).all()

# лимит
limit_query = User.query.limit(2).all()

# сортировка
sort_query = User.query.order_by(User.email).all()

# сортировка по убыванию
sort_query_desc = User.query.order_by(User.email.desc()).all()

# получение по первичному ключу через метод get
get_query = User.query.get(1)

# запрос с присоединением таблиц. Запрашиваем пары автор-объявление
# в данном примере таблица User будет главной, а Ad вспомогательной
join_query = db.session.query(User, Ad).join(Ad, User.id == Ad.author).all()

a = 0
