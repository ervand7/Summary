# https://ru.wikipedia.org/wiki/Получение_ресурса_есть_инициализация#Псевдокод_на_Python
resource_for_grep = False


class RAII:
    g = globals()

    def __init__(self):
        self.g['resource_for_grep'] = True

    def __del__(self):
        self.g['resource_for_grep'] = False


print(resource_for_grep)  # False
r = RAII()
print(resource_for_grep)  # True
del r
print(resource_for_grep)  # False
