from curses.textpad import rectangle
from turtle import Shape


class Shape:
    def area(self):
        return self.area()

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius * self.radius

Rectangle=Rectangle(10,20)
circle= Circle(12)
print(Rectangle.area())
print(circle.area())