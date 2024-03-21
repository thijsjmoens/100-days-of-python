target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above

# Write your code here

# Create an empty variable
sum_of_even_numbers = 0

for number in range(0, target):
    
    if (number % 2) == 0:
        sum_of_even_numbers += number
        
        
if (target % 2) == 0:
    sum_of_even_numbers += target
    
# Print sum of all even numbers
print(sum_of_even_numbers)