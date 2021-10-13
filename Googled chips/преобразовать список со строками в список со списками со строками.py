# преобразовать список со строками в список со списками со строками
# 1 вариант:
list_with_strings = ['efefwef', 'sadxa', '3452']
list_with_lists = []
for i in list_with_strings:
    i = [element.strip("'[]") for element in i.split(", ")]
    list_with_lists.append(i)
print(list_with_lists)


# 2 вариант:
def convert(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
    return res


print(convert(list_with_strings))
