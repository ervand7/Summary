# основная статья: https://www.w3schools.com/python/ref_random_choices.asp
import random

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights=[5, 1, 1], k=14))
