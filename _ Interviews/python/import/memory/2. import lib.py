import pprint
import functools  #

pprint.pprint(locals())
# {'__annotations__': {},
#  '__builtins__': <module 'builtins' (built-in)>,
#  '__cached__': None,
#  '__doc__': None,
#  '__file__': '/Users/ervand_agadzhanyan/Desktop/Summary/_ '
#              'Interviews/python/theory/import/memory/2. import lib.py',
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fd6100cbe50>,
#  '__name__': '__main__',
#  '__package__': None,
#  '__spec__': None,
#  'functools': <module 'functools' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/functools.py'>,
#  'pprint': <module 'pprint' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py'>}
print(locals().__sizeof__())  # 624
