# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

welcome = "Welcome to the secret auction program."

# Ask for name
name = input("What is your name?: ")
print(name)

# Ask for bid and put a dollar sign in front
bid = input("What's your bid?: $")
print("$" + bid)

# Ask for more bidders
more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")


# If yes, clear the screen


# If no, output the winner
result = "The winner is ... with a bid of $..."