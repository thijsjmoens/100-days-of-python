

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



def subtract(number1, number2):



def divide(number1, number2number1, number2):



def multiply(number1, number2):


# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

calculator = {
	"+": add(),
	"-": subtract(),
	"*": multiply(),
	"/": divide(),
}

# Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.


def calculator():

	# Start with welcome screen
	print(logo)

	# Ask for first number
	first_number = int(input("What's the first number?:"))

	# Ask for operation
	print("+\n-\n*\n/\n")
	input("Pick an operation:")

	# Ask for second number
	second_number = int(input("What's the next number?:"))

	# Output calculation

	# Ask for more calculations
	input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")



