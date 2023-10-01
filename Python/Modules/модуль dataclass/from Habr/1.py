from dataclasses import dataclass


# regular class
class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# we will change to dataclass
@dataclass
class Book:
    """
    Вы автоматически получаете класс, с
    реализованными методами __init__, __repr__, __str__ и __eq__
    """
    title: str
    author: str


book = Book(title="Fahrenheit 451", author="Bradbury")
print(book)  # Book(title='Fahrenheit 451', author='Bradbury')
print(book.author)  # Bradbury
other = Book("Fahrenheit 451", "Bradbury")

print(hex(id(book)))  # 0x7fbe60086400
print(hex(id(other)))  # 0x7fbe6009c130
# comparison by value
print(book == other)  # True
