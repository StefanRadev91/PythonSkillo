# Problem 5:
# Design an abstract class "Vehicle" with a method "start_engine()". 
# Create two subclasses, "Car" and "Bicycle," implementing the "start_engine()" method differently.
# Demonstrate polymorphism by calling the method on instances of both subclasses.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine is started!")

class Bicycle(Vehicle):
    def start_engine(self):
        print("Please start pushing the pedals!")

b1 = Bicycle()
b1.start_engine()  

c1 = Car()
c1.start_engine()