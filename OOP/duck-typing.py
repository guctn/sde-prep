# Duck typing = Object must have the minimum necessary attributes and methods to be used for a specific purpose, regardless of the actual type of the object.

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False 
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]
# so here we change the Car class method from howk() to speak()
# because the it has the minimum necessary methods to be considered an animal
for animal in animals:
    animal.speak()
    print(animal.alive)