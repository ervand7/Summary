# first decorator
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


# second decorator
def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@header
def say():
    name = 'John'
    surname = 'Adams'
    age = 77
    print(f"{name} {surname}, {age}. say's function worked out!")


say()
# <table>
# <h1>
# John Adams, 77. say's function worked out!
# </h1>
# </table>
