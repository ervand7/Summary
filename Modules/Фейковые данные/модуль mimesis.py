# прекрасная документация: https://mimesis.readthedocs.io/getting_started.html>>> from mimesis import Person
from mimesis import Person
from mimesis.enums import Gender
from mimesis import Generic

person = Person('ru')
print(person.full_name(gender=Gender.FEMALE))
print(person.full_name(gender=Gender.MALE))

g = Generic('ru')
print(g.datetime.month())
print(g.code.imei())
print(g.food.fruit())
print(g.science.rna_sequence())
