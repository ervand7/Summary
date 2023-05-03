# doc: https://zepworks.com/deepdiff/current/serialization.html#

from deepdiff import DeepDiff

t1 = {'a': [1, 2], 'b': [3, 4]}
t2 = {'a': [2, 1], 'b': [4, 3]}
DeepDiff(t1, t2, ignore_order=True)


def ignore_order_func(level):
    return 'a' in level.path()


print(DeepDiff(t1, t2, ignore_order=True, ignore_order_func=ignore_order_func))
# {'values_changed': {"root['b'][0]": {'new_value': 4, 'old_value': 3}, "root['b'][1]": {'new_value': 3, 'old_value': 4}}}
