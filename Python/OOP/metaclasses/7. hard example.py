from pprint import pprint


class Meta(type):
    def create_local_attrs(self):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    # must be cls in __init__
    def __init__(cls, name: str, base: tuple, attrs: dict):
        print(hex(id(cls)))  # 0x7f8a7df2f8d0
        super().__init__(name, base, attrs)

        cls.class_attrs = attrs
        # define here cls __init__
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'


print(hex(id(Women)))  # 0x7f8a7df2f8d0
w = Women()
pprint(w.__dict__)
# {'__module__': '__main__',
#  '__qualname__': 'Women',
#  'content': 'контент',
#  'photo': 'путь к фото',
#  'title': 'заголовок'}
