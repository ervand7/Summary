from first import *  # <*> на самом деле заменяет __all__

a = Doctor
b = Person
c = Example  # ошибка, так как Example не входит в переменную __all__ в файле <first.py>
