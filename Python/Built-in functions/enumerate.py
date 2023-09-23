# ||||||||||||||| enumerate ||||||||||||||||||||
a = [10, 20, 30, 40, 50, 60]
print(list(enumerate(a)))  # [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50), (5, 60)]

# ______________________________

for index, value in enumerate(a):
    a[index] += 1
print(*a)  # 11 21 31 41 51 61
# ______________________________

s = 'hello'
for index, value in enumerate(s):
    print(index, value, end="   ")  # 0 h   1 e   2 l   3 l   4 o
print()
# ______________________________

t = ('apple', 'banana', 'mango')
for index, value in enumerate(t):
    print(index, value, end="   ")  # 0 apple   1 banana   2 mango
print()
# ______________________________

d = {'a': 1, 'b': 2, 'c': 3}
for index, value in enumerate(d):
    print(index, value, end="   ")  # 0 a   1 b   2 c
print()
# ______________________________

for index, value in enumerate(range(10, 20)):
    print(index, value, end="   ")  # 0 10   1 11   2 12   3 13   4 14   5 15   6 16   7 17   8 18   9 19
print()
# ______________________________

t = ('apple', 'banana', 'mango')
for index, value in enumerate(t, 13):
    print(index, value, end="   ")  # 13 apple   14 banana   15 mango
print()
