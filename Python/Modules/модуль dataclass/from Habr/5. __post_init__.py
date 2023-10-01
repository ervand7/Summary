# __post_init__ runs after initialisation

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    desc: str = None

    def __post_init__(self):
        self.desc = self.desc or "`%s` by %s" % (self.title, self.author)


print(Book("Fahrenheit 481", "Bradbury"))
# Book(title='Fahrenheit 481', author='Bradbury', desc='`Fahrenheit 481` by Bradbury')
