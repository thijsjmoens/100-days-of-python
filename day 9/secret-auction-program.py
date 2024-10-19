# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# Start with welcome screen
welcome = "Welcome to the secret auction program."
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print(welcome)

# Variable for clearing the screen
clear_screen = "\n " * 20

# Variable to check for more bidders
check_more_bidders = "yes"

# Dictonary for storage name and price
auctions = {}

# Ask for name
name = input("What is your name?: ")

# Ask for bid and put a dollar sign in front
bid = int(input("What's your bid?: $"))

# Assign name and price to dictonary
auctions[name] = bid

# Ask for more bidders
check_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

# If yes, clear the screen
print(clear_screen)

while check_more_bidders == "yes": 

	# Ask for name
	name = input("What is your name?: ")

	# Ask for bid and put a dollar sign in front
	bid = int(input("What's your bid?: $"))

	# Assign name and price to dictonary
	auctions[name] = bid

	# Ask for more bidders
	check_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	
	# If yes, clear the screen
	print(clear_screen)


# Create variable for winner
winner = ""
highest_number = 0


# Check who has the highest bid
for key in auctions:

	# Compare all bids against each other
	if auctions[key] > highest_number:
		winner = key
		# print(winner)
		highest_number = auctions[key]


# If no, output the winner
result = f"The winner is {winner} with a bid of ${highest_number}"

print(result)



