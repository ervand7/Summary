# Ссылки для поиска работы:
# https://geekjob.ru/
# https://career.habr.com/vacancies?type=all
# https://web.telegram.org/#/im?p=@jobforjunior
# Стажировки:
# https://sbergraduate.ru/sberseasons-moscow/
# https://fintech.tinkoff.ru/study/start/
# https://job.lanit.ru/vacancy/Pages/new-search.aspx#isyoung=1

# ____________________________________________________________________
def func(m, l=[]):
    l.append(m)
    return l


# print(func(5))
# print(func(5))
# print(func(54))


def func2(m, l=[]):
    l.append(m)
    return l


# print(func2(5))
# ____________________________________________________________________

a = [1, 2, 3]
b = a

b.append(5)
# print(a)

# чтобы этого избежать и создать независимую копию, есть 3 варианта
b = a.copy()
b1 = list(a)
b2 = a[:]
# ____________________________________________________________________

a_ = 2
b_ = 3
a_, b_ = b_, a_
# print(a_)
# print(b_)

a_ = b_ + a_
b_ = b_ + a_
a = a_ - a_
b_ = b_ - b_
# ____________________________________________________________________

my_list = [[1, 2], [3, 4], [5, 6]]
# [1, 2, 3, 4, 5, 6]
new = []
for i in my_list:
    for j in i:
        new.append(j)

# print(new)


my_list2 = sum(my_list, [])


# print(my_list2)
# ____________________________________________________________________
def my_decorator(foo):
    def inner(*args, **kwargs):
        print('decorator started')
        result = foo(*args, **kwargs)
        print('decorator ended')
        return result

    return inner


@my_decorator
def experimental(*args, **kwargs):
    print('Hello world')


# experimental()
