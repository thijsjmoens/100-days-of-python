#!/usr/bin/env python

# Import local and external libraries
import art
import random
import os

# Credits
__author__ = "Thijs Moens"
__copyright__ = "Copyright 2025, Thijs Moens"
__credits__ = ["Thijs Moens"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Thijs Moens"
__email__ = "thijsmoens@email.com"
__status__ = "Production"

# This is a game where you have to guess a number between 1 and 100

# Variable that counts the attempts
count_attempts = ''

# Empty variable for guess
guess = 0

# Variable for number to guess
number_to_guess = random.choice(range(1, 100))

# Clear the screen
os.system('cls||clear')
    
# Print the logo of the game
print(art.logo)

# Print welcome text
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Ask the player if the game should be hard or easy
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Show the rules for each difficulty
if difficulty == 'easy':
    count_attempts = 10
    
elif difficulty == 'hard':
    count_attempts = 5
    
else:
    exit()
    
while int(guess) != number_to_guess: 
    
    # Check if there are no more attempts
    if count_attempts == 0:
        print(f"You've run out of attempts. Better luck next time. (the answer was {number_to_guess}.)")
        exit()

    print(f"You have {count_attempts} attempts remaining to guess the number.")
    
    # Ask the player for a guess
    guess = input("Make a guess: ")
    
    # Check if guess is the correct number
    if int(guess) == number_to_guess:
        print(f"You got it! 🎉 The answer was {number_to_guess}")
        break
    elif int(guess) < number_to_guess:
        print("Too low")
        print("Guess again")
        count_attempts -= 1
    else: 
        print("Too high")
        print("Guess again")
        count_attempts -= 1