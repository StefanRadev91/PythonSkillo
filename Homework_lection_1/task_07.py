# Create a program that checks whether a given number 
# is even or odd. Prompt the user to enter a number and then print out whether it's even or odd.

number = int(input("Please enter a number to check: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")
