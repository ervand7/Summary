# In Python, the `del` statement is used to remove items from data
# structures like lists, dictionaries, or to delete variables and their
# references. Here are some common usages of the `del` statement:

# 1. **Deleting Variables:**
# You can use `del` to remove a variable and its reference from memory.
x = 5
del x

# 2. **Deleting Elements from Lists:**
# You can use `del` to remove elements from a list by specifying the index of the item you want to delete.
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Removes the element at index 2 (value 3)

# 3. **Deleting Slices from Lists:**
# You can also delete a slice of elements from a list.
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]  # Removes elements at indices 1 and 2 ([2, 3])

# 4. **Deleting Elements from a Dictionary:**
# You can use `del` to remove items (key-value pairs) from a dictionary by
# specifying the key.
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']  # Removes the key 'b' and its associated value


# 5. **Deleting Entire Variables and Objects:**
# You can use `del` to delete an entire object, including its variables.
class MyClass:
    pass


obj = MyClass()
obj.hello = "world"

del obj.hello  # Deletes `hello` attr
del obj  # Deletes the entire object

# 6. **Deleting Variables from a Module:**
# You can use `del` to remove variables or functions from a module. This can be
# useful when you want to clean up a module's namespace.
from functools import wraps

del wraps  # Removes my_function from the current module's namespace

# It's important to note that using `del` can lead to unexpected behavior if
# not used carefully, especially when deleting variables or elements from
# data structures. It should be used with caution to avoid unintentional
# data loss or reference errors.
