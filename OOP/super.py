# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods
#           super = parent

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled 

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# here with super() method we call the constructor from the parent 
# then we can also set the common attributes 
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color,is_filled)
        self.radius = radius 

    # method overwriting - if a child shares a similar method
    # the childs method will be used instead of its parent's
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius**2}")
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color,is_filled)
        self.width = width

    # if you don't want to overwrite it, but use both methods (parent and child)
    # use super()
    def describe(self):
        print(f"It is a square with a area of {self.width**2}")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It's a triangle with an area of {self.height * self.width / 2}")
        super().describe()
        
circle = Circle("red", True, 5)
square = Square("blue", False, 10)
triangle = Triangle("yellow", True, 4, 8)

circle.describe()
square.describe()
# output: It is a square with a area of 20
#         It is blue and not filled
triangle.describe()