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
    print(f"You have {count_attempts} attempts remaining to guess the number.")
    
    # Ask the player for a guess
    guess = input("Make a guess: ")
    
elif difficulty == 'hard':
    count_attempts = 5
    print(f"You have {count_attempts} attempts remaining to guess the number.")
    
else:
    exit()

