# основная статья: https://habr.com/ru/post/415829/
from dataclasses import dataclass


#  с помощью декоратора dataclass можно вот такой вот код:
class APerson:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


# заменить на:
@dataclass
class Person:
    name: str
    surname: str
    age: int

    def __init__(self):
        print(self.__annotations__)


a = Person()
