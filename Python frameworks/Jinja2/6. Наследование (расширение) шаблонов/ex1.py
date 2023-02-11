from jinja2 import Environment, FileSystemLoader


subs = ['Математика', 'Физика', 'Информатика', 'Русский']
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.html')
output = template.render(list_table=subs)

print(output)
