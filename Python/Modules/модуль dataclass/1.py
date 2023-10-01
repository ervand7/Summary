# основная статья: https://habr.com/ru/post/415829/
from dataclasses import dataclass
from pprint import pprint


#  с помощью декоратора dataclass можно вот такой вот код:
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


# заменить на:
@dataclass
class PersonData:
    name: str
    surname: str
    age: int


a = Person(name='Ivan', surname='Petrov', age=15)
print(a)  # <__main__.Person object at 0x7f7fa80ebee0>

b = PersonData(name="Ivan", surname="Petrov", age=15)
print(b)  # Person(name='Ivan', surname='Petrov', age=15)
print(b.__annotations__)  # {'name': <class 'str'>, 'surname': <class 'str'>, 'age': <class 'int'>}

pprint(PersonData.__dict__)
# mappingproxy({'__annotations__': {'age': <class 'int'>,
#                                   'name': <class 'str'>,
#                                   'surname': <class 'str'>},
#               '__dataclass_fields__': {'age': Field(name='age',type=<class 'int'>,default=<dataclasses._MISSING_TYPE object at 0x7f8218193a00>,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8218193a00>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD),
#                                        'name': Field(name='name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x7f8218193a00>,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8218193a00>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD),
#                                        'surname': Field(name='surname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x7f8218193a00>,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8218193a00>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)},
#               '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
#               '__dict__': <attribute '__dict__' of 'PersonData' objects>,
#               '__doc__': 'PersonData(name: str, surname: str, age: int)',
#               '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f8218282a60>,
#               '__hash__': None,
#               '__init__': <function __create_fn__.<locals>.__init__ at 0x7f82182828b0>,
#               '__module__': '__main__',
#               '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f8218282820>,
#               '__weakref__': <attribute '__weakref__' of 'PersonData' objects>})