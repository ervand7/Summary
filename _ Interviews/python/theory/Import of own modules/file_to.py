import file_from
from file_from import my_num_1, my_num_2
import sys
from pprint import pprint

print(file_from.factorial(10))
print(f'{my_num_1}\n{my_num_2}')

print(file_from.sqrt(33))  # we can do this thanks to importing module 'sqrt' in file file_from

# so, thanks to importing library 'sys', we can see the way, where
# python finds file file_from
pprint(sys.path)

# we can also reload library we need
import importlib
importlib.reload(file_from)
