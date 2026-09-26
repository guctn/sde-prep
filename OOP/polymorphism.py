# Polymorphism = Means to have many forms or faces in programming. 
# It allows us to define methods in the child class with the same name as defined in their parent class. 
# In Python, we use method overriding to achieve polymorphism.
# TWO WAYS TO ACHIEVE POLYMORPHISM:
# 1. Method Overriding | Inheritance - When a child class has a method with the same
# 2. Duck typing = Object must have necessary attributes and methods to be used for a specific purpose, regardless of the actual type of the object.        
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    
class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return self.height * self.base / 2

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius) 

shapes = [Circle(2), Square(5), Triangle(10, 5), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")