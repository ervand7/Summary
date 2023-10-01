from dataclasses import dataclass


# Одна из полезных особенностей — легкость добавления к полям
# значений по умолчанию. Все ещё не требуется переопределять
# метод __init__, достаточно указать значения прямо в классе.
@dataclass
class Book:
    title: str = "Unknown"
    author: str = "Unknown author"


print(Book())  # Book(title='Unknown', author='Unknown author')
print(Book("Fahrenheit 451"))  # Book(title='Fahrenheit 451', author='Unknown author')
