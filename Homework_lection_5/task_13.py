# Use list comprehension to create a list of the squares of even numbers from 1 to 30.

even_squares = [x**2 for x in range(1, 31) if x % 2 == 0]
print(even_squares)