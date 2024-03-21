# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row

# Create empty variable for comparising
highest_number = 0

# loop trough all the numbers
for score in student_scores:
    
    # Compare new number with excisting number
    if score > highest_number:
        # keep score
        highest_number = score
    
# Print highest number to the screen
print(f"The highest score in the class is: {highest_number}")
