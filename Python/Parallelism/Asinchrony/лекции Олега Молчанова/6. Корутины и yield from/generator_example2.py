def subgen():
    message = yield 'Ready to accept message'
    yield f'Subgen received: {message}'


g = subgen()
print(g.send(None))  # or print(next(g))
print(g.send('Ok'))

# Ready to accept message
# Subgen received: Ok