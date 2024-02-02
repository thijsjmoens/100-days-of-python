# print("The Love Calculator is calculating your score...")
name1 = "Angela Yu" #input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# Make the input lowercase
name1_lower = name1.lower()
name2_lower = name2.lower()

# Check the letters of the word TRUE in the name
name_t = name1_lower.count('t') + name2_lower.count('t')
name_r = name1_lower.count('r') + name2_lower.count('r')
name_u = name1_lower.count('u') + name2_lower.count('u')
name_e = name1_lower.count('e') + name2_lower.count('e')

# Check the letters of the word LOVE in the name
name_l = name1_lower.count('l') + name2_lower.count('l')
name_o = name1_lower.count('o') + name2_lower.count('o')
name_v = name1_lower.count('v') + name2_lower.count('v')

name_true_check = name_t + name_r + name_u + name_e
name_love_check = name_l + name_o + name_v + name_e

# Make string to concatenate
string_true = str(name_true_check)
string_love = str(name_love_check)
total_points = string_true + string_love

# Make a interger for comparising
total_integer_points = int(total_points)

# Check the total points and print the message
if total_integer_points <= 10 or total_integer_points >= 90:
    print(f"Your score is {total_points}, you go together like coke and mentos.")
elif total_integer_points >= 40 and total_integer_points <= 50:
    print(f"Your score is {total_points}, you are alright together.")
else: 
    print(f"Your score is {total_points}.")