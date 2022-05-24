import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# What is DSN: https://en.wikipedia.org/wiki/Data_source_name
DSN = 'postgresql://db_orm:db_orm@localhost:5432/db_orm'
engine = sq.create_engine(DSN)
Base = declarative_base()  # Base - общепринятое название схемы
# declarative_base - это функция, которая нам генерирует класс
Session = sessionmaker(bind=engine)


class Genre(Base):
    __tablename__ = 'genre'

    id = sq.Column(sq.Integer, primary_key=True)  # если указываем Integer, то sqlalchemy авт. сделает его serial
    name = sq.Column(sq.String(length=50))
    description = sq.Column(sq.String)

    def __str__(self):
        return f'<Genre ({self.id}): {self.name} | {self.description}>'

    def __repr__(self):
        return str(self)


# создание связи m2m
# это промежуточная таблица. Она реализовывается не в виде класса, а как переменная
genres_tracks = sq.Table(
    'genres_tracks',  # название промежуточной таблицы желательно давать такое же как и у переменной
    Base.metadata,  # Base.metadata - указание, что данная промежут. таблица принадлежит к схеме Base
    sq.Column('genre_id', sq.Integer, sq.ForeignKey('genre.id')),  # указываем именно названия таблицы.id
    sq.Column('track_id', sq.Integer, sq.ForeignKey('track.id'))  # указываем именно названия таблицы.id
)


class Track(Base):
    __tablename__ = 'track'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50))
    duration = sq.Column(sq.Integer)
    genres = relationship(
        Genre,
        secondary=genres_tracks,  # secondary указывает на промежуточную таблицу genres_tracks
        backref='tracks'  # для того, чтобы в табличке жанров создалось поле tracks
    )

    # Внимание! Тут мы могли бы вместо backref указать back_populates. Но тогда
    # back_populates пришлось бы указывать с обеих сторон (то есть и в таблицу tracks)

    def __str__(self):
        return f'<Genre ({self.id}): {self.name} | {self.duration}>'

    def __repr__(self):
        return str(self)


def create_schema():
    """
    Эта функция будет создавать все таблички.
    """
    Base.metadata.create_all(bind=engine)
