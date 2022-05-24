from models_3 import *

create_schema()
session = Session()
genre = session.query(Genre).get(1)
[session.add(Track(name=f'Track {i}', duration=i, genres=[genre])) for i in range(10)]
session.commit()


print(genre)  # <Genre (1): Поп | Тестовое описание>
print(genre.tracks[0])  # <Genre (1): Track 0 | 0>
print(genre.tracks[0].genres)  # [<Genre (1): Поп | Тестовое описание>]

