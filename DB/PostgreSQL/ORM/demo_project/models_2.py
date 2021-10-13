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


def create_schema():
    """
    Эта функция будет создавать все таблички.
    """
    Base.metadata.create_all(bind=engine)
