def gen(s):
    for i in s:
        yield i


g = gen('oleg')
for i in g:
    print(i)

# o
# l
# e
# g
