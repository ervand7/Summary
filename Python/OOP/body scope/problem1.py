# Проблема
# We need to call info method from instance

class DepartamentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(PYTHON_DEV, GO_DEV, REACT_SEV)


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


a1 = DepartamentIT2()

a1.info()  # 3 3 2


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2) use <self>
class DepartamentIT3:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)


a2 = DepartamentIT3()

a2.info()  # 3 3 2


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 3) use class name before attribute
class DepartamentIT4:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(DepartamentIT4.PYTHON_DEV, DepartamentIT4.GO_DEV, DepartamentIT4.REACT_SEV)


a3 = DepartamentIT4()

a3.info()  # 3 3 2


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 4) use ordinary function
class DepartamentIT5:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        return print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)


a4 = DepartamentIT5()

a4.info()  # 3 3 2


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 5) use property
class DepartamentIT5:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    @property
    def info(self):
        return print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)


a5 = DepartamentIT5()

a5.info  # 3 3 2


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 6) use classmethod
class DepartamentIT6:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    @classmethod
    def info(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_SEV)


a6 = DepartamentIT6()

a6.info()  # 3 3 2


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 7) use staticmethod
class DepartamentIT7:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    @staticmethod
    def info():
        print(DepartamentIT7.PYTHON_DEV, DepartamentIT7.GO_DEV, DepartamentIT7.REACT_SEV)


a7 = DepartamentIT7()
a7.info()  # 3 3 2
