import random

names = names_string.split(", ")

# Check the number of people
number_of_people = len(names)

# Pick a random number
random_number = random.randint(0, number_of_people - 1)

# Check the number with the right person
person_who_pays = names[random_number]

# Output that the winning person has to pay
print(f"{person_who_pays} is going to buy the meal today!")