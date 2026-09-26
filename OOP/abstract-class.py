# abstract class = criar uma base comum + estabelecer um contrato que as subclasses precisam respeitar
#                   não pode ser instanciada 

# abstract based classes
from abc import ABC, abstractmethod 

# now no one can creat a Vehicle object
class Vehicle(ABC):

    # every future child class will inherit the abstractclass methods
    @abstractmethod
    def go(self):
        pass
    # we must declare them but don't define them - think it's a rule that each child will set up
    @abstractmethod
    def stop(self):
        pass

# to instantiate a Car object we MUST create all the abstract methods from the parent
class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You stop the motorcycle")
# if the method isn't created we'll receive a TypeError because we forgot the abstract method 
# so it kinda guides what we are FORCED to create for each class

car = Car()
motorcycle = Motorcycle()
boat = Boat()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()

boat.go()
boat.stop()