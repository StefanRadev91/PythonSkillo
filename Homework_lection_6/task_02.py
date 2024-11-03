# Problem 2:
# Create a class "Student" with protected attributes for name and age. 
# Implement property getter and setter methods for these attributes. Demonstrate their usage.

class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Името трябва да бъде непразен низ")  
        if value[0].islower():
            raise ValueError("Името трябва да започва с главна буква")  
        self._name = value

    @property
    def age(self):
        return self._age  

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Годините трябва да са положително цяло число")  
        self._age = value
    def __str__(self):
        return f"Student(name='{self.name}', age={self.age})"

student1 = Student("Stefan", 33)
print(student1)