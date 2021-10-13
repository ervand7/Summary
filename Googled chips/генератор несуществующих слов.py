# Генератор несуществующих слов
from random import choice, randint
import string

nonsense = ["".join(choice(string.ascii_lowercase) for i in range(randint(5, 10)))]
print(nonsense[0])
