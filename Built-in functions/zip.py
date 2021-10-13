# ||||||||||||||| zip ||||||||||||||||||||

a = [5, 6, 7, 8]
b = [100, 200, 300, 400]
c = 'abcd'

# ____________________________
rez = list(zip(a, b))
print(rez)
# ____________________________

for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)
# ____________________________

rez = zip(a, b, c)
print(list(rez))
# ____________________________

rez = zip(a, b, c)
col1, col2, col3 = zip(*rez)
print(col1, col2, col3)
