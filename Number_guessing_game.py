"""This Number Guessing Game is an interactive challenge where players try to guess a randomly generated number within a specified range. 
The game begins by asking the player to input the lower and upper bounds for the number range. 
After setting the range, the player has a limited number of guesses, calculated based on the size of the range.
With each guess, the game provides feedback on whether the guess is too high or too low and informs the player of the remaining chances.
If the player guesses correctly, they win; otherwise, they are revealed the correct number at the end"""


import random
import math

print("Welcome to the Number Guessing Game!")

# Taking Inputs
while True:
    try:
        lower = int(input("Enter Lower bound: "))
        upper = int(input("Enter Upper bound: "))
        if lower < upper:
            break
        else:
            print("Lower bound must be less than Upper bound. Please try again.")
    except ValueError:
        print("Please enter valid integers.")

# Generating a random number between lower and upper
x = random.randint(lower, upper)
total_chances = math.ceil(math.log2(upper - lower + 1))
print(f"\nYou've only {total_chances} chances to guess the integer!\n")

# Initializing the number of guesses
count = 0
guessed_correctly = False

# Guessing loop
while count < total_chances:
    count += 1
    while True:
        try:
            guess = int(input("Guess a number: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    if guess == x:
        print(f"Congratulations! You guessed the number in {count} tries.")
        guessed_correctly = True
        break
    elif guess < x:
        print("You guessed too small!")
    else:
        print("You guessed too high!")

    remaining_chances = total_chances - count
    if remaining_chances > 0:
        print(f"You have {remaining_chances} {'chance' if remaining_chances == 1 else 'chances'} left.")
    else:
        print("No chances left!")

if not guessed_correctly:
    print(f"\nThe number was {x}. Better luck next time!")
