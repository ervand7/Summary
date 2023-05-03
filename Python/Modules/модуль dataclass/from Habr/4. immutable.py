from dataclasses import dataclass


# let's make a semblance of namedtuple
@dataclass(frozen=True)
class Book:
    title: str
    author: str


book = Book("Fahrenheit 451", "Bradbury")
# book.title = "1984" - dataclasses.FrozenInstanceError: cannot assign to field 'title'
