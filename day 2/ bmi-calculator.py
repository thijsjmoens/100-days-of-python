# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# prepare the height first
new_height = float(height) ** 2

# calculate the bmi
bmi = int(weight) // new_height

# print bmi as an interger
print(int(bmi))