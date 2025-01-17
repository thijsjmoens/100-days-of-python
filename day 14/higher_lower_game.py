#!/usr/bin/env python

# Import local and external libraries
import art
import game_data
import os
import random

# Credits
__author__ = "Thijs Moens"
__copyright__ = "Copyright 2025, Thijs Moens"
__credits__ = ["Thijs Moens"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Thijs Moens"
__email__ = "thijsmoens@email.com"
__status__ = "Production"

# Get data from local file
data = game_data.data

# Create a function to pick a random number
def pick_a_random_nummber(data=data):
    
    # Step 2: Pick a random number
    random_number = random.randint(0, len(data) - 1)
    
    return random_number


# Create a function for comparising
def comparising(data=data):

    # Get the data
    person = data[pick_a_random_nummber()]
    
    # Return the dict for later use
    return person
    
    

# Create a function to check Instagram followers
def check_instagram_followers(data=data):
    
    # Create a variable for output
    more_followers = ''
    
    # Get the comparising persons
    follower_a = comparising()
    follower_b = comparising()
    
    # First check if it is the same person
    if follower_a == follower_b:
        
        # Pick a new one
        follower_b = comparising()
    
    # Check who has more followers
    if follower_a['follower_count'] > follower_b['follower_count']:
        
        # Set variable to a
        more_followers = 'A'
        
    else: 
        
        # Set variable to b
        more_followers = 'B'
        
    # Return the check
    return more_followers
        
        
# ___ HERE BEGINS THE GAME ____        


# Create a variable for the score
score = 0    

# Create a variable for the correct answer
correct_answer = True
    
# Check if the answer is correct and keep brining comparisings
while correct_answer:
    
    # Clear the screen
    os.system('cls||clear')   

    # Print the logo of the game
    print(art.logo)

    # Show person A
    person_a = comparising()
    person_a_name =   person_a['name']
    person_a_description =   person_a['description']
    person_a_country =   person_a['country']
    
    # Print the person to the terminal
    print(f"Compare A: {person_a_name}, a {person_a_description}, from {person_a_country}")
    
    if score > 0:
        
        # Print that the answer is right and show the score
        print(f"You're right! Current score: {score}")

    # Show the VS art
    print(art.vs)

    # Show person B
    person_b = comparising()

    person_b_name = person_b['name']
    person_b_description = person_b['description']
    person_b_country = person_b['country']
    
    # Print the person to the terminal
    print(f"Compare B: {person_b_name}, a {person_b_description}, from {person_b_country}")

    # Show the question who has more followers
    answer = input("Who has more followers? Type 'A' or 'B': ")

    # Check if the answer is correct
    if answer == check_instagram_followers():
        
        # Set the variable to true
        correct_answer = True
        
        # Add 1 point for a good answer.
        score += 1
        
    else:
        
        # Set variable to false
        correct_answer = False
        
        # Clear the screen
        os.system('cls||clear')   

        # Print the logo of the game
        print(art.logo)
        
        # Print that the answer is wrong and exit the gane
        print(f"Sorry, that's wrong. Final score: {score}")

        # Exit game
        exit()
        
        
        
        
# KNOW BUGS
'''
1. There can be 2 of the same persons
2. The comparising is printed 2 times
'''