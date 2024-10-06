# Write a program that prompts the user to enter a radius and 
# then calculates and prints the area and circumference of a circle with that radius.

from math import pi

radius = int(input("Please enter radius of the circle: "))

square_the_radius = radius * radius

area = square_the_radius * pi

circumference = (radius * 2) * pi

print(f"{area:.2f}")
print(f"{circumference:.2f}")

