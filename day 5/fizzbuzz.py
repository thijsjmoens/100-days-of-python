'''
Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

'''

# Print 1 to 100 (include 100)
for number in range(1, 101):

	# Check if divisible by 3 and by 5
	if (number % 3 == 0) & (number % 5 == 0):

		print("FizzBuzz")

	elif (number % 3 == 0) & ~(number % 5 == 0):

		print("Fizz")

	elif ~(number % 3 == 0) & (number % 5 == 0):

		print("Buzz")

	else:

		print(number)