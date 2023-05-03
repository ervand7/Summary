from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    desc: str = None

    def __post_init__(self):
        self.desc = self.desc or "`%s` by %s" % (self.title, self.author)


print(Book("Fareneheit 481", "Bradbury"))
# Book(title='Fareneheit 481', author='Bradbury', desc='`Fareneheit 481` by Bradbury')
