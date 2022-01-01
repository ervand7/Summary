from jinja2 import Template

data = """
{% raw %}Модуль Jinja2 вместо определения {{ name }} подставляет 
соответствующее значение.{% endraw %}
"""

tm = Template(data)
msg = tm.render(name='Федор')

print(msg)
