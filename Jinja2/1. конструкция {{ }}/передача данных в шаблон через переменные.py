from jinja2 import Template

name = "Федор"
age = 28

tm = Template("Мне {{ a * 2 }} лет, и зовут {{ n.upper() }}.")
msg = tm.render(n=name, a=age)

print(msg)
