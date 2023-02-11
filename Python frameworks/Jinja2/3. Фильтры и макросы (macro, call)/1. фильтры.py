# список всех фильтров здесь:
# https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters

from jinja2 import Template

# вариант со списком словарей:
cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300},
]

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)  # Суммарная цена автомобилей 105900

# вариант со списком чисел:
digs = [1, 2, 3, 4, 5]
tpl = "Суммарная цена автомобилей {{ cs | sum }}"
tm = Template(tpl)
msg = tm.render(cs=digs)
print(msg)  # Суммарная цена автомобилей 15
