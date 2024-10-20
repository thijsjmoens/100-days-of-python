

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Create functions for add, subtract, divide, multiply

def add(number1, number2):
	return number1 + number2



def subtract(number1, number2):
	return number1 - number2



def divide(number1, number2):
	return number1 / number2



def multiply(number1, number2):
	return number1 * number2



def calculator():


	# Create check variable for new calculations
	is_new_calculations = True

	# Start with welcome screen
	print(logo)

	# Ask for first number
	first_number = int(input("What's the first number?:"))

	# Loop the questions if check is true
	while is_new_calculations == True:

		# Ask for operation
		print("+\n-\n*\n/\n")
		operation = input("Pick an operation:")

		# Ask for second number
		second_number = int(input("What's the next number?:"))

		# Calculate the numbers
		# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
		calculator = {
			"+": add(first_number, second_number),
			"-": subtract(first_number, second_number),
			"*": multiply(first_number, second_number),
			"/": divide(first_number, second_number),
		}

		# Output calculation
		result = calculator[operation]

		# Ask for more calculations
		new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
		if new_calculation == "n":
			is_new_calculations = False
		elif new_calculation == "y":
			is_new_calculations = True
			first_number = result
		else :
			is_new_calculations = False



calculator()
