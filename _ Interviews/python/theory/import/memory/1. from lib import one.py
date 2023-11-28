import pprint
from functools import wraps  #

pprint.pprint(locals())
# {'__annotations__': {},
#  '__builtins__': <module 'builtins' (built-in)>,
#  '__cached__': None,
#  '__doc__': None,
#  '__file__': '/Users/ervand_agadzhanyan/Desktop/Summary/_ '
#              'Interviews/python/theory/import/memory/1. from lib import one.py',
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8e400cbe50>,
#  '__name__': '__main__',
#  '__package__': None,
#  '__spec__': None,
#  'pprint': <module 'pprint' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py'>,
#  'wraps': <function wraps at 0x7f8e300f6ee0>}
print(locals().__sizeof__())  # 624
