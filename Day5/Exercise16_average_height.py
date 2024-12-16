# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_student = 0
total_height = 0
for height in student_heights:
  total_height += height
  total_student += 1

avg_height = round(total_height/total_student)

print(f"total height = {total_height}")
print(f"number of students = {total_student}")
print(f"average height = {avg_height}")