# welcome user
print("Welcome to the tip calculator.")

# ask for the bill
bill = float(input("What was the total bill? $"))

# ask for percentage
percentage = input("What percentage tip would you like to give? 10, 12, 15? ")

# ask for number of people
number_of_people = int(input("How many people to split the bill? "))

# calculate percentage
real_percentage = "1." + percentage

# calculate the amount per person
amount = (bill / number_of_people) * float(real_percentage)

# round the amount with 2 decimals
amount = round(amount, 2)

# Print the result
print(f"Each person should pay: ${amount}")
