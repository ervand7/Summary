# ||||||||||||||| enumerate ||||||||||||||||||||
a = [10, 20, 30, 40, 50, 60]
# print(list(enumerate(a)))

# ______________________________
for index, value in enumerate(a):
    if value % 20 == 0:
        print(f'{index} - {value}')
# ______________________________

for index, value in enumerate(a):
    a[index] += 1
print(*a)
# ______________________________

s = 'hello'
for index, value in enumerate(s):
    print(index, value)
# ______________________________

t = ('apple', 'banana', 'mango')
for index, value in enumerate(t):
    print(index, value)
# ______________________________

d = {'a': 1, 'b': 2, 'c': 3}
for index, value in enumerate(d):
    print(index, value)
# ______________________________

for index, value in enumerate(range(10, 20)):
    print(index, value)
# ______________________________

t = ('apple', 'banana', 'mango')
for index, value in enumerate(t, 13):
    print(index, value)
