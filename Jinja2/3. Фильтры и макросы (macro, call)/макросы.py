from jinja2 import Template

html = '''
{%- macro input(name, value='', type='text', size=20) -%}
    <input name="{{ name }}", value="{{ value|e }}", type="{{ type }}", size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm = Template(html)
msg = tm.render()
print(msg)
# <p><input name="username", value="", type="text", size="20">
# <p><input name="email", value="", type="text", size="20">
# <p><input name="password", value="", type="text", size="20">


