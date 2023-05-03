# generator of permutations
from itertools import product

word = 'привет'
x = [i for i in word]

for roll in product(x, repeat=6):
    print(roll)
