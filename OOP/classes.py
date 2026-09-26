from car import Car
# importing the class 

# creating object 01, 02 and 03
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1)
# output: <__main__.Car object at 0x1010f3fd0>
# that's the object's memory address

print(car1.model)
# output: Mustang
print(car1.year)
# output: 2024
# using object.attribute returns the value

# USING METHODS
car1.drive()
# output: You drive the car
car1.stop()
# output: You stopped the car

car2.drive()
# output: You drive the Corvette
car2.stop()
# output: You stopped the Corvette

car3.describe()
# output: 2026|yellow|Charger