# Problem 7:
# Create a class "Animal" with a special method "__init__" 
# that sets a species attribute. Implement subclasses "Dog" and "Cat" with their own "__str__" methods. Use
# polymorphism to display species information.

class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f"Hello my name is {self.name}, my color is {self.color} and I am {self.age} years old"

class Dog(Animal):
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} and I love to play with my owner"

class Cat(Animal):
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} and I love to sleep"

dog = Dog("Buck", "Black", 18)
print(dog)

cat = Cat("Patrisha", "Pink", 23)
print(cat)