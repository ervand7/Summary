# официальная документация (источник этого конспекта): https://pyyaml.org/wiki/PyYAMLDocumentation
# pip install pyyaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

