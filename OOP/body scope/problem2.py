# Problem
class DepartamentIT:
    PYTHON_DEV = 3  # Problem is that in given construction we can't change PYTHON_DEV value in lines 14-18
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)

    def hiring_extra_py_dev(self):
        self.PYTHON_DEV += 1


a = DepartamentIT()
print(a.PYTHON_DEV)  # 3
a.hiring_extra_py_dev()
print(a.__dict__)  # {'PYTHON_DEV': 4}  # here we see we created a local attribute
print(a.PYTHON_DEV)  # 4
print(DepartamentIT.PYTHON_DEV)  # 3  # the problem will pop up here

print()


# Solution:
# _______________________________________________________

class DepartamentIT2:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_SEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_SEV)

    def hiring_extra_py_dev(self):
        DepartamentIT2.PYTHON_DEV += 1


b = DepartamentIT2()
print(b.PYTHON_DEV)  # 3
b.hiring_extra_py_dev()
print(b.__dict__)  # {}
print(b.PYTHON_DEV)  # 4
b.hiring_extra_py_dev()
print(DepartamentIT2.PYTHON_DEV)  # 5
