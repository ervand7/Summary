# https://www.youtube.com/watch?v=zS0HyfN7Pm4&t=578s
# При том что в обоих вариантах __mro__ одинаковый, результат стека вызова
# разный, так как super(), использованный во втором варианте работает учитывая
# __mro__, в то время как в первом варианте мы руками делали инициализацию

# Вариант с реализацией без super
class Portishead:
    def __init__(self):
        print('Portishead')


class KanyeWest(Portishead):
    def __init__(self):
        print('KanyeWest')
        Portishead.__init__(self)  # the same effect of super(KanyeWest, self).__init__()


class ASAPRocky(Portishead):
    def __init__(self):
        print('ASAP Rocky')
        Portishead.__init__(self)


class ASAPSebbie(ASAPRocky, KanyeWest):
    def __init__(self):
        print('ASAP Sebbie')
        ASAPRocky.__init__(self)
        KanyeWest.__init__(self)


asap_sebbie = ASAPSebbie()
print(ASAPSebbie.__mro__)


# Этот вариант приводит нас к неправильному стеку вызова:
# ASAP Sebbie
# ASAP Rocky
# Portishead
# KanyeWest
# Portishead


# ______________________________________________________________________________________________________
# Правильный вариант реализации с применением super


class Kate(Portishead):
    def __init__(self):
        print('Kate')
        super().__init__()


class Bill(Portishead):
    def __init__(self):
        print('Bill')
        super().__init__()


class Jane(Kate, Bill):
    def __init__(self):
        print('Jane')
        super().__init__()


print()
jane = Jane()
# Jane
# Kate
# Bill
# Portishead
print(Jane.__mro__)