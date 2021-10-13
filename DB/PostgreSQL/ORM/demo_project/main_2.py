from models_2 import *

session = Session()
# обновляем колонку description
# 1й вариант
print(session.query(Genre).filter(Genre.name == 'Поп').update(
    {'description': 'Тестовое описание'}))  # 1  /1 - кол-во измененных объектов
# Внимание! Тут используется синтаксис питона (==)
session.commit()
# 2й вариант
genre = session.query(Genre).filter(Genre.name == 'Рок').first()
session.add(genre)
genre.description = 'Новое описание'
session.commit()

# мы также можем отдельно сохранять кверисет
queryset = session.query(Genre).filter(Genre.name == 'Поп')
# и распечатать его для того, чтобы посмотреть, как выглядит сырой sql-запрос
print(queryset)
# SELECT genre.id AS genre_id, genre.name AS genre_name, genre.description AS genre_description
# FROM genre
# WHERE genre.name = %(name_1)s

print()
# также можно применять двойную фильтрацию
queryset = session.query(Genre).filter(Genre.name == 'Поп').filter(Genre.description == None)
print(queryset)
