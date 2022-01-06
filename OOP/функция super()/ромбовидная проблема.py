# https://www.youtube.com/watch?v=zS0HyfN7Pm4&t=578s
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
        super(Kate, self).__init__()


class Bill(Portishead):
    def __init__(self):
        print('Bill')
        super(Bill, self).__init__()


class Jane(Kate, Bill):
    def __init__(self):
        print('Jane')
        super(Jane, self).__init__()


print()
jane = Jane()
# Jane
# Kate
# Bill
# Portishead
