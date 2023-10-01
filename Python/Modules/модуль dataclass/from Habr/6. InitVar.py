# Одна из возможностей, связанных с методом __post_init__ — параметры,
# используемые только для инициализации. Если при объявлении поля указать в
# качестве его типа InitVar, его значение будет передано как параметр метода
# __post_init__. Никак по-другому такие поля не используются в классе данных.


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


print(Book("Fahrenheit 481", "Bradbury"))
#  Book(title='Fahrenheit 481', author='Bradbury', desc='`Fahrenheit 481` by Bradbury')
print(Book("Fahrenheit 481", "Bradbury", gen_desc=False))
#  Book(title='Fahrenheit 481', author='Bradbury', desc=None)
