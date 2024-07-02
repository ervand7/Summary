# 1) Ivan.__dict__: dict of class attributes + methods of class + some service info
# 2) instance.__dict__: dict of instance attributes
from pprint import pprint


class Ivan:
    attr1 = "hello"
    attr2 = "world"

    def __init_(self, a: int, b: int):
        self.a = a
        self.b = b

    def say(self):
        print(self)


ivan = Ivan()
# diff addrs of __dict__
print(hex(id(Ivan.__dict__)))  # 0x7fb5d8152fa0
print(hex(id(ivan.__dict__)))  # 0x7fb5d803ac40

pprint(Ivan.__dict__)
# mappingproxy({'_Ivan__init_': <function Ivan.__init_ at 0x7f86c805aee0>,
#               '__dict__': <attribute '__dict__' of 'Ivan' objects>,
#               '__doc__': None,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'Ivan' objects>,
#               'attr1': 'hello',
#               'attr2': 'world',
#               'say': <function Ivan.say at 0x7f86c8065670>})

ivan.field = 1
print(ivan.__dict__)  # {'field': 1}
