def gen(s):
    yield from s


g = gen('oleg')
for i in g:
    print(i)

# o
# l
# e
# g
