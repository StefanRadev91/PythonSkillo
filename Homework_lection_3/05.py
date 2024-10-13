# Modify problem 2 so that every time the user is prompted the problem is different. 
# Think of a way to design that and come up with a proper solution for that.

import random

win_streak = 0

while True:
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    result = first_number + second_number
    
    user_choice = input(f"How much is {first_number} + {second_number}: ")
    
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if user_choice == result:
        win_streak += 1 
        print("Congrats!")
        print(f"Try to guess another, your win streak is {win_streak}")
    else:
        print(f"Sorry, you lose. Your final win streak is {win_streak}")
        break

