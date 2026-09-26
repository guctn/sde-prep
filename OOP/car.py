# object = a package of related attributes (variables) and methods (functions) that act on those attributes
#           example: a car is an object, it has attributes like color, make, model, and methods like drive and brake
#           to create many objects, we use classes
# class = a blueprint (molde) for creating objects
# for better organization we create a separate class file and imports on the main file

class Car:
    # constructor = a special method that is automatically called when an object is created
    # we need this method in order to create objects
    def __init__(self, model, year, color, for_sale):
        # self = 
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # methods are actions the class can performe
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self): 
        print(f"You stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year}|{self.color}|{self.model}")