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
bid = input("What's your bid?: $")

# Assign name and price to dictonary
auctions[name] = bid

# Ask for more bidders
check_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

print(clear_screen)

while check_more_bidders == "yes": 

	# Ask for name
	name = input("What is your name?: ")

	# Ask for bid and put a dollar sign in front
	bid = input("What's your bid?: $")

	# Assign name and price to dictonary
	auctions[name] = bid

	# Ask for more bidders
	check_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

	print(clear_screen)





# If yes, clear the screen


# If no, output the winner
result = "The winner is ... with a bid of $..."










# dict = {
# 	"name": "price",
# 	"Thijs": 142,
# 	"Angela": 140
# }

# dict["Pieter"] = 138

# print(dict)