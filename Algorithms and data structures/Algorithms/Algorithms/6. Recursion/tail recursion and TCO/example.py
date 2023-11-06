# You must understand that Python does not support tail recursion and TCO
# https://stackoverflow.com/questions/33923/what-is-tail-recursion?page=1&tab=scoredesc#tab-top

# usual
def rec_sum(x):
    if x == 0:
        return 0
    return x + rec_sum(x - 1)


"""
The stack is:
rec_sum(5)
5 + rec_sum(4)
5 + (4 + rec_sum(3))
5 + (4 + (3 + rec_sum(2)))
5 + (4 + (3 + (2 + rec_sum(1))))
5 + (4 + (3 + (2 + (1 + rec_sum(0)))))
5 + (4 + (3 + (2 + (1 + 0))))
5 + (4 + (3 + (2 + 1)))
5 + (4 + (3 + 3))
5 + (4 + 6)
5 + 10
15
"""


# tail
def tail_rec_sum(x, running_total=0):
    if x == 0:
        return running_total
    return tail_rec_sum(x - 1, running_total + x)


"""
The stack is:
tail_rec_sum(5, 0)
tail_rec_sum(4, 5)
tail_rec_sum(3, 9)
tail_rec_sum(2, 12)
tail_rec_sum(1, 14)
tail_rec_sum(0, 15)
15
"""

print(rec_sum(5))
print(tail_rec_sum(5))
