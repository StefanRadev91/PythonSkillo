import math

# Problem 2: Area of Shapes

def area_square(side):
    return area_rectangle(side, side)

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * (radius ** 2)
