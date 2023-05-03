# хорошая статья (источник): https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial
import sys
from importlib import import_module
from pprint import pprint

"""When you start a Python interpreter, one of the things it creates automatically is a list that contains all 
of directories it will use to search for modules when importing. This list is available in a variable named sys.path. 
Here is an example of printing out sys.path. Note that the empty '' entry means the current directory."""
pprint(sys.path)


"""IMPORT BY STRING.
If you want to import a module programmatically, you can use importlib.import_module(). 
This function is useful if you are creating a plugin system where modules need to be 
loaded at run-time based on string names. String should match the same format you would normally use to import"""
my_module = import_module("my_package.my_module")
# Then you can use it as if you did `import my_package.my_module`
my_module.my_function()
