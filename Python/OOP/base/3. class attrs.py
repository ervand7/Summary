class Person:
    name = "Ivan"


a = Person()
b = Person()

# class attrs are not saved in instance __dict__
print(a.__dict__)  # {}
print(b.__dict__)  # {}

print(hex(id(Person.name)))  # 0x7fd05003ad30
print(hex(id(a.name)))  # 0x7fd05003ad30
print(hex(id(b.name)))  # 0x7fd05003ad30

Person.name = "Vasya"
print(hex(id(Person.name)))  # 0x7fb2381e8b70
print(hex(id(a.name)))  # 0x7fb2381e8b70
print(hex(id(b.name)))  # 0x7fb2381e8b70
