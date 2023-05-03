# https://www.geeksforgeeks.org/python-functools-cached_property/


from functools import cached_property


class Sample:

    def __init__(self, lst):
        self.long_list = lst

    @cached_property
    def find_sum(self):
        return sum(self.long_list)


obj = Sample(range(900000000))
print(obj.find_sum)
print(obj.find_sum)
print(obj.find_sum)
