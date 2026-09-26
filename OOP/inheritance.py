# Inheritance = allows a class to inherit the attributes and methods of another class
# Parent class = the class being inherited from (also called base class)
# Child class = the class that inherits from another class (also called derived class)  
# BENEFIT: reusablity and extensibility of code
# example:  ANIMAL
#          /  |  \ 
#       cat  CAT  FISH

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating") 

    def sleep(self):
        print(f"{self.name} is asleep")

# Child classes
class Dog(Animal):
    # the class DOG will inherit all the attributes and methods of its parent
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

dog.speak()
cat.speak()
mouse.speak()