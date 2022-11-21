def gen_with_many_yield():
    yield 1
    print('yield 1 was')
    yield 2
    print('yield 2 was')
    yield 3
    print('yield 3 was')


g = gen_with_many_yield()
for i in g:
    pass

# yield 1 was
# yield 2 was
# yield 3 was

print()
g = gen_with_many_yield()
next(g)
next(g)
next(g)

# yield 1 was
# yield 2 was
