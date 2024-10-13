import random

attempts = 5
guessed_number = random.randint(1, 100)

user_answer = int(input("Try to guess the number: "))
while True:
    if guessed_number > user_answer:
        attempts -= 1
        if attempts == 0:
            print(f"You don't have any more attempts, game over! The number you were searching for is {guessed_number}")
            break
        else:
            print(f"Too low, left attempts = {attempts}")
    elif guessed_number < user_answer:
        attempts -= 1
        if attempts == 0:
            print(f"You don't have any more attempts, game over! The number you were searching for is {guessed_number}")
            break
        else:
            print(f"Too high, left attempts = {attempts}")
    else:
        print("Correct!")
        break
    user_answer = int(input("Try again: "))