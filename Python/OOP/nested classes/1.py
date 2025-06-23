# we cannot use Outer namespace from Inner

class Outer:
    name = "Ivan"

    def __init__(self):
        # otherwise Inner will not be created while creating Outer instance
        self.inner = self.Inner()

    class Inner:
        name = "Vasya"


print(Outer.name)  # Ivan
print(Outer.Inner.name)  # Vasya

o = Outer()
print(Outer.__dict__)  # {'__module__': '__main__', 'name': 'Ivan', 'Inner': <class '__main__.Outer.Inner'>, '__dict__': <attribute '__dict__' of 'Outer' objects>, '__weakref__': <attribute '__weakref__' of 'Outer' objects>, '__doc__': None}
print(o.__dict__)  # {}
print(o.Inner.name)  # Vasya
