# instance variable = variables defined in the constructor - every object must have them
# class variables = variables defined outside of the constructor - allow you to share data among all objects

class Student: 
    # class variables: shared among all objects
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        # self is for the object itself
        # use Student instead for class variables
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# class_year is a class variable that applies for all objects - not good use
print(student1.name, student1.class_year)
print(student2.name, student2.class_year)
# output: Patrick 2024

# it's common to access a class variable using the class name
print(Student.class_year) 
# output: 2024
# this makes obvious that this variable is a class variable this way

print(Student.num_students)
# output: 2

print(f"My graduation class of {Student.class_year} has {Student.num_students} students")
#output:  My graduation class of 2024 has 2 students