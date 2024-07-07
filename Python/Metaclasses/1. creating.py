class Usual(list):
    name = "Ivan"
    age = 13

    def get_length(self):
        return len(self)


ThroughMetaclass = type(
    # class name
    'ThroughMetaclass',

    # the list of base classes
    (list,),

    # dict of attrs and methods
    {
        "get_length": lambda self: len(self),
        "name": "Ivan",
        "age": 13
    }
)

print(Usual.__dict__)  # {'__module__': '__main__', 'name': 'Ivan', 'age': 13, 'get_length': <function Usual.get_length at 0x7f79f019e4c0>, '__dict__': <attribute '__dict__' of 'Usual' objects>, '__weakref__': <attribute '__weakref__' of 'Usual' objects>, '__doc__': None}
print(ThroughMetaclass.__dict__)  # {'get_length': <function <lambda> at 0x7f79f00cef70>, 'name': 'Ivan', 'age': 13, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'ThroughMetaclass' objects>, '__weakref__': <attribute '__weakref__' of 'ThroughMetaclass' objects>, '__doc__': None}