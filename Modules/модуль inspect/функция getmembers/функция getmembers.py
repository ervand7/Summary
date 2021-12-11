import inspect

import example

for name, data in inspect.getmembers(example):
    if name == '__builtins__':
        continue
    print('%s :' % name, repr(data))

"""
Output:
A : <class 'example.A'>
B : <class 'example.B'>
__cached__ : '/Users/dasaagadzanan/Desktop/Summary/Modules/модуль inspect/функция getmembers/__pycache__/example.cpython-38.pyc'
__doc__ : 'Sample file to serve as the basis for inspect examples.\n'
__file__ : '/Users/dasaagadzanan/Desktop/Summary/Modules/модуль inspect/функция getmembers/example.py'
__loader__ : <_frozen_importlib_external.SourceFileLoader object at 0x7f94492bb730>
__name__ : 'example'
__package__ : ''
__spec__ : ModuleSpec(name='example', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f94492bb730>, origin='/Users/dasaagadzanan/Desktop/Summary/Modules/модуль inspect/функция getmembers/example.py')
instance_of_a : <example.A object at 0x7f944ac82df0>
module_level_function : <function module_level_function at 0x7f944929dc10>
"""
