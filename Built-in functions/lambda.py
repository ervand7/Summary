# |||||||||| lambda |||||||||||||||||
r = lambda x: x ** 2
# print(r(7))

x_ = 123
t = lambda x_: 'positive' if x_ > 0 else 'negative'
# print(t(x_))

a = [78, 56, 23, 8, 54512, 65, 98, 2354, 41, 5000]
a.sort(key=lambda x: x // 10 % 10)
# print(a)
