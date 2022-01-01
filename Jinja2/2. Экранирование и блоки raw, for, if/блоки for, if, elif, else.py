from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 2, 'city': 'город2'},
    {'id': 3, 'city': 'город3'},
    {'id': 4, 'city': 'город4'},
    {'id': 5, 'city': 'город5'},
    {'id': 6, 'city': 'город6'},
]

# знак минус (-) убирает перенос строки
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 3 -%}
    <option value="{{ c['id'] }}">"{{ c['city'] }}"</option>
{% elif c.city == "Москва" -%}
    <option>{{ c['city'] }}</option>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>
'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
