# Проблема
# We need to call info method from instance

class DepartamentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(PYTHON_DEV, GO_DEV, REACT_SEV)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


a = DepartamentIT()
# a.info()  # here will be error

# _______________________________________________________
# Solution:
# _______________________________________________________
# 1) bring everything into the global scope
PYTHON_DEV_ = 3
GO_DEV_ = 3
REACT_SEV_ = 2


class DepartamentIT2:

    def info(self):
        print(PYTHON_DEV_, GO_DEV_, REACT_SEV_)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


b = DepartamentIT2()


# b.info()
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2) use <self>
class DepartamentIT3:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


c = DepartamentIT3()


# c.info()


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 3) use class name before attribute
class DepartamentIT4:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(DepartamentIT4.PYTHON_DEV, DepartamentIT4.GO_DEV, DepartamentIT4.REACT_SEV)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


d = DepartamentIT4()


# d.info()
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 4) use property
class DepartamentIT5:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    @property
    def info(self):
        return print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


e = DepartamentIT5()


# e.info
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 5) use classmethod
class DepartamentIT6:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    @classmethod
    def info(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_SEV)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


f = DepartamentIT6()


# f.info()
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 5) use staticmethod
class DepartamentIT7:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    @staticmethod
    def info():
        print(DepartamentIT7.PYTHON_DEV, DepartamentIT7.GO_DEV, DepartamentIT7.REACT_SEV)

    def make_backend(self):
        print('Python and Go')

    def male_fromtend(self):
        print('React')


g = DepartamentIT7()
# g.info()