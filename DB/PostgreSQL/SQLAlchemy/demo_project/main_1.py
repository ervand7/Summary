from models_1 import *

create_schema()  # создаст только 1 раз, так как действует принцип <create table if not exists>

session = Session()

pop_music = Genre(name='Поп')
rock_music = Genre(name='Рок')
# нужно понимать, что все, что у нас сейчас есть - это объекты в памяти Python
# но в БД эти объекты еще не добавлены
print(pop_music.id, rock_music.id)  # None None

# вот так мы добавляем их в БД. Сначала накапливаем данные (через add), затем добавляем (через commit)
session.add(pop_music)
session.add(rock_music)
session.commit()

print(pop_music.id, rock_music.id)  # 1 2
print(session.query(Genre).all())  # [<models.Genre object at 0x7fb9ea1d9400>, <models.Genre object at 0x7fb9e89fc1f0>]
print(session.query(Genre).first())  # <Genre (1): Поп | None>


