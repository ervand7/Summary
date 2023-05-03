from dataclasses import InitVar, dataclass


@dataclass
class Book:
    title: str
    author: str
    gen_desc: InitVar[bool] = True
    desc: str = None

    def __post_init__(self, gen_desc: str):
        if gen_desc and self.desc is None:
            self.desc = "`%s` by %s" % (self.title, self.author)


print(Book("Fareneheit 481", "Bradbury"))
#  Book(title='Fareneheit 481', author='Bradbury', desc='`Fareneheit 481` by Bradbury')
print(Book("Fareneheit 481", "Bradbury", gen_desc=False))
#  Book(title='Fareneheit 481', author='Bradbury', desc=None)
