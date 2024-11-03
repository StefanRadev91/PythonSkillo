# Problem 4:
# Implement a class "Rectangle" with private attributes for 
# length and width. Include special methods "__eq__" and "__lt__" to compare rectangles based on area and
# perimeter. Test the comparison operators with multiple instances.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area() and self.perimeter() == other.perimeter()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area() or (self.area() == other.area() and self.perimeter() < other.perimeter())
        return NotImplemented

    def __repr__(self):
        return f"Rectangle(length={self.__length}, width={self.__width})"


rect1 = Rectangle(4, 5)
rect2 = Rectangle(5, 4)
rect3 = Rectangle(3, 6)
rect4 = Rectangle(2, 10)

print(f"rect1: {rect1}, area: {rect1.area()}, perimeter: {rect1.perimeter()}")
print(f"rect2: {rect2}, area: {rect2.area()}, perimeter: {rect2.perimeter()}")
print(f"rect3: {rect3}, area: {rect3.area()}, perimeter: {rect3.perimeter()}")
print(f"rect4: {rect4}, area: {rect4.area()}, perimeter: {rect4.perimeter()}")


print(f"rect1 == rect2: {rect1 == rect2}")  
print(f"rect1 < rect3: {rect1 < rect3}")    
print(f"rect3 < rect4: {rect3 < rect4}")    
print(f"rect2 < rect1: {rect2 < rect1}")    