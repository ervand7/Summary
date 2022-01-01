from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


per = Person("Федор", 33)

tm = Template("Мне {{ p.age }} лет, и зовут {{ p.name }}.")
msg = tm.render(p=per)

print(msg)
