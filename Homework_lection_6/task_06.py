# Problem 6:
# Implement a class "Book" with special methods "__str__" and "__len__" 
# to provide a string representation and the number of pages. Create instances of "Book" and
# demonstrate the use of these methods.

class Book:
    def __init__(self, name, number_of_pages):
        self.name = name
        self.number_of_pages = number_of_pages
        
    def __str__(self):
        return f"Book: {self.name}, Pages: {self.number_of_pages}"
        
    def __len__(self):
        return self.number_of_pages
    
b1 = Book("Arsenal", 1886)  

print(b1)        
print(len(b1))     