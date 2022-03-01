from jinja2 import Template

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)

# ----------------- Improved example from stackoverflow ------------------
a = """
{% macro render_dialog(title, class='dialog') -%}
<div class="{{ class }}">
    <h2>{{ title }}</h2>
    <div class="contents">
        {{ caller() }}
    </div>
</div>
{%- endmacro %}

{% call render_dialog(title='Hello World') %}
   This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}
"""

tm = Template(a)
msg = tm.render()
print(msg)
