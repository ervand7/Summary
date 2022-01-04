def rec(x):
  print(x)
  rec(x+1)

# rec(1)
#``````````````````````````````````````

def my_second_rec(x):
  if x < 4:
    print(x)
    my_second_rec(x+1)
    print(x)

# my_second_rec(1)
#``````````````````````````````````````

# GETTING FACTORIAL
# before this we remember, how write the usual factorial function
def usual_fact(x):
  counter = 1
  for i in range(x):
    i += 1
    counter *= i
  print(counter)
# usual_fact(15)


def fact(x):
  if x == 1: #
    return 1 # prescribing the conditions for exiting the recursion
  return fact(x - 1) * x

# print(fact(15))
#``````````````````````````````````````

# GETTING fibonacci numbers
# bad way, after the number 22 it already works very slowly
def fib(x):
  if x == 1: #
    return 0 #
  if x == 2: #
    return 1 # prescribing the conditions for exiting the recursion
  return fib(x - 1) + fib(x - 1)

# print(fib(10))
#``````````````````````````````````````

# CHECKING IS IT POLINDROME
def palindrome(x):
  if len(x) <= 1: #
    return True #
  if x[0] != x[-1]: #
    return False # prescribing the conditions for exiting the recursion
  return palindrome(x[1:-1])

# print(palindrome('qwqqeewq'))
#``````````````````````````````````````

# let `s write a progremm which show us the leveks of nesting
a = [1, [2, [56, [44, 56, [67, 7878], 66], 78], 89, 45], [345, [5, 456, [343, 56], 2, 7, 9, 65, 234], 0, 23]]

def nested_rec(my_list, level=1):
  print(*my_list, '|level=', level)
  for i in my_list:
    if type(i) == list:
      nested_rec(i, level+1)

# nested_rec(a)