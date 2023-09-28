from pprint import pprint


class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name: str, base: tuple, attrs: dict):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'


w = Women()
pprint(w.__dict__)
# {'__module__': '__main__',
#  '__qualname__': 'Women',
#  'content': 'контент',
#  'photo': 'путь к фото',
#  'title': 'заголовок'}
