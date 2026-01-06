# Visitor — add new operations without changing objects
# ❓ The idea
# Move operations out of objects into a separate “visitor” object.

# Elements
class Shape:
    def accept(self, visitor):
        pass


class Circle(Shape):
    def accept(self, visitor):
        visitor.visit_circle(self)


class Square(Shape):
    def accept(self, visitor):
        visitor.visit_square(self)


# Visitor
class AreaCalculator:
    def visit_circle(self, circle):
        print("Calculating circle area")

    def visit_square(self, square):
        print("Calculating square area")


# Usage
shapes = [Circle(), Square()]
visitor = AreaCalculator()

for shape in shapes:
    shape.accept(visitor)
