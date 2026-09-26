# multiple inheritance = inherit from more than one parent class
#                       C(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                       A -> B(A) -> C(B)

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# MULTILEVEL IH - parent class but also child 
class Prey(Animal):
    def escape(self):
        print(f"{self.name} is escaping")

# MULTILEVEL IH - parent class
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# MULTILEVEL IH - child class
class Rabbit(Prey): 
    pass

# MULTILEVEL IH - child class
class Hawk(Predator):
    pass

# MULTIPLE IH and MULTILEVEL IH - - child class from 2 classes - it can escape from BIG fish or hunt SMALL fish - and also is an animal
class Fish(Prey, Predator):
    pass 

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.escape()
hawk.hunt()
fish.escape()
fish.hunt()

rabbit.eat()
fish.sleep()