# Write a program that prompts the user to enter their age 
# and then determines and prints out whether they are eligible to vote (i.e., if they are 18 or older).

user_age = int(input("Please enter your age: "))

if user_age >= 18:
    print("Cogrants, you are eligible to vode!")
else:
    print("Sorry, you are not eligible to vode!")
