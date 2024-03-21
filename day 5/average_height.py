# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
  
# Write your code below this row
count = 0
total_height = 0

for student_height in student_heights:
    total_height = total_height + student_height 
    count += 1
    
# Divide total by count
average_height = total_height / count
clean_avg_height = round(average_height)

# Print all to console
print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {clean_avg_height}")