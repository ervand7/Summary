import pprint
from functools import *  #

pprint.pprint(locals())
# {'WRAPPER_ASSIGNMENTS': ('__module__',
#                          '__name__',
#                          '__qualname__',
#                          '__doc__',
#                          '__annotations__'),
#  'WRAPPER_UPDATES': ('__dict__',),
#  '__annotations__': {},
#  '__builtins__': <module 'builtins' (built-in)>,
#  '__cached__': None,
#  '__doc__': None,
#  '__file__': '/Users/ervand_agadzhanyan/Desktop/Summary/_ '
#              'Interviews/python/theory/import/memory/3. from lib import *.py',
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8e3006be50>,
#  '__name__': '__main__',
#  '__package__': None,
#  '__spec__': None,
#  'cache': <function cache at 0x7f8e30175940>,
#  'cached_property': <class 'functools.cached_property'>,
#  'cmp_to_key': <built-in function cmp_to_key>,
#  'lru_cache': <function lru_cache at 0x7f8e301758b0>,
#  'partial': <class 'functools.partial'>,
#  'partialmethod': <class 'functools.partialmethod'>,
#  'pprint': <module 'pprint' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py'>,
#  'reduce': <built-in function reduce>,
#  'singledispatch': <function singledispatch at 0x7f8e30175c10>,
#  'singledispatchmethod': <class 'functools.singledispatchmethod'>,
#  'total_ordering': <function total_ordering at 0x7f8e400a8c10>,
#  'update_wrapper': <function update_wrapper at 0x7f8e30162c10>,
#  'wraps': <function wraps at 0x7f8e3018fee0>}
print(locals().__sizeof__())  # 1160
