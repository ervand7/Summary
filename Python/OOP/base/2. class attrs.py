class Person:
    name = "Ivan"

    def __init__(self, x: int):
        self.x = x


a = Person(1)
b = Person(1)

# class has `name` in __dict__, but does not have `x`
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Ivan', '__init__': <function Person.__init__ at 0x7feff01de4c0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# instances have `x` in __dict__, but does not have `name`
print(a.__dict__)  # {'x': 1}
print(b.__dict__)  # {'x': 1}

print(hex(id(Person.name)))  # 0x7fd05003ad30
print(hex(id(a.name)))  # 0x7fd05003ad30
print(hex(id(b.name)))  # 0x7fd05003ad30

Person.name = "Vasya"  # address changed
print(hex(id(Person.name)))  # 0x7fb2381e8b70
print(hex(id(a.name)))  # 0x7fb2381e8b70
print(hex(id(b.name)))  # 0x7fb2381e8b70
