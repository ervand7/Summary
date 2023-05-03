def say(name, surname, age):
    print(f"{name, surname, age} say's function worked out!")


# first decorator
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner  # without()


# second decorator
def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


say = table(header(say))
say("one", "two", "three")

# <table>
# <h1>
# ('one', 'two', 'three') say's function worked out!
# </h1>
# </table>
