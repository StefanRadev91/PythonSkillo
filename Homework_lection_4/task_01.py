# Define a function called `simple_calculator` that takes two numbers and 
# an operator ('+', '-', '*', or '/') as arguments and returns the result of the operation.

def simple_calculator(a , b, operator):
    if operator == "+":
        c = a + b
        return c
    elif operator == "-":
        c = a - b
        return c
    elif operator == "*":
        c = a * b
        return c
    elif operator == "/":
        c = a / b
        return c
    
result = simple_calculator(2024, 1991, "-")
print(result)
    
