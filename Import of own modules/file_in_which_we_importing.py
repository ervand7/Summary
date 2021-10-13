import file_from_which_we_make_import
from file_from_which_we_make_import import my_num_1, my_num_2
import sys
from pprint import pprint

print(file_from_which_we_make_import.factorial(10))
print(f'{my_num_1}\n{my_num_2}')

print(file_from_which_we_make_import.sqrt(33))  # me can do this thanks to importing
# module 'sqrt' in file file_from_which_we_make_import

# so, thanks to importing library 'sys', we can see the way, where
# python finds file file_from_which_we_make_import
pprint(sys.path)

# we can also reload library we need
import importlib
importlib.reload(file_from_which_we_make_import)
