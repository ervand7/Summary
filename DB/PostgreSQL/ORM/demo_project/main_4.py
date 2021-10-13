from models_4 import *

create_schema()
session = Session()

track = session.query(Track).get(7)
genres = session.query(Genre).all()
new_genre = Genre(name='Техно')
session.add(new_genre)
# делаем так, чтобы трек №7 содержал помимо всех существующих жанров, еще и new_genre
track.genres.extend(genres + [new_genre])
session.add(track)
session.commit()
