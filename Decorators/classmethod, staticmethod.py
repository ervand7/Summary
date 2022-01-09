# @staticmethod
# at staticmethod any function do not receive required arguments, even 'self' of 'cls'
class Example:
    @staticmethod
    def print_hello():
        print('staticmethod is called')


# and the function that was decorated by staticmethod can be called and from class, and from exemplar of class
my_example = Example()


# my_example.print_hello()
# Example.print_hello()

# _____________________________________________________________________
class OurPoint:
    __count = 0

    def __init__(self, x=0, y=0):
        OurPoint.__count += 1
        self.x = x
        self.y = y

    @staticmethod
    def get_count():
        return OurPoint.__count


p1 = OurPoint()
p2 = OurPoint()
p3 = OurPoint()


# print(p3.get_count())
# print(OurPoint.get_count())  # we avoid error: get_count() missing 1 required positional argument: 'self'
# _____________________________________________________________________
# @classmethod
class Example2:
    @classmethod
    def print_class_world(cls):
        print('Class, world')


# Example2.print_class_world()
# e2 = Example2()
# e2.print_class_world()
# print(e2.__class__())

