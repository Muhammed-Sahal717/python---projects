# example for constructor overloading
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

# creating rectangle with default dimensions
rect1 = Rectangle()
rect1.area() # outputs 1, because default width and height are 1

# creating rectangle with custom dimensions
rect2 = Rectangle(5, 3)
rect2.area() # outputs 15, because width is 5 and height is 3
