from jinja2 import Template

per = {'name': 'Федор', 'age': 34}

# вариант 1:
tm = Template("Мне {{ p.age }} лет, и зовут {{ p.name }}.")
msg = tm.render(p=per)

# вариант 2:
tm2 = Template("Мне {{ p['age'] }} лет, и зовут {{ p['name'] }}.")
msg2 = tm.render(p=per)

print(msg)
print(msg2)
