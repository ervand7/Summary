# 1) Class.__dir__(): list of available magic methods
# 2) instance.__dir__(): list of  available magic methods +
# class attributes + methods of class


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
# the same addr
print(hex(id(Ivan.__dir__(Ivan))))  # 0x7fca98165ec0
print(hex(id(ivan.__dir__())))  # 0x7fb5d803ac40

pprint(Ivan.__dir__(Ivan))
['__repr__',
 '__call__',
 '__getattribute__',
 '__setattr__',
 '__delattr__',
 '__init__',
 '__new__',
 'mro',
 '__subclasses__',
 '__prepare__',
 '__instancecheck__',
 '__subclasscheck__',
 '__dir__',
 '__sizeof__',
 '__basicsize__',
 '__itemsize__',
 '__flags__',
 '__weakrefoffset__',
 '__base__',
 '__dictoffset__',
 '__mro__',
 '__name__',
 '__qualname__',
 '__bases__',
 '__module__',
 '__abstractmethods__',
 '__dict__',
 '__doc__',
 '__text_signature__',
 '__hash__',
 '__str__',
 '__lt__',
 '__le__',
 '__eq__',
 '__ne__',
 '__gt__',
 '__ge__',
 '__reduce_ex__',
 '__reduce__',
 '__subclasshook__',
 '__init_subclass__',
 '__format__',
 '__class__']

print()
pprint(ivan.__dir__())
['__module__',
 'attr1',
 'attr2',
 '_Ivan__init_',
 'say',
 '__dict__',
 '__weakref__',
 '__doc__',
 '__repr__',
 '__hash__',
 '__str__',
 '__getattribute__',
 '__setattr__',
 '__delattr__',
 '__lt__',
 '__le__',
 '__eq__',
 '__ne__',
 '__gt__',
 '__ge__',
 '__init__',
 '__new__',
 '__reduce_ex__',
 '__reduce__',
 '__subclasshook__',
 '__init_subclass__',
 '__format__',
 '__sizeof__',
 '__dir__',
 '__class__']
