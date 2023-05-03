# В качестве альтернативы есть функция make_dataclass,
# которая работает аналогично созданию именованных кортежей.
from dataclasses import make_dataclass

Book = make_dataclass("Book", ["title", "author"])
book = Book("Fahrenheit 451", "Bradbury")
