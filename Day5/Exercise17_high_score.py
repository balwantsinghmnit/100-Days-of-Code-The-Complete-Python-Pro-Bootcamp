# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

highest_score = student_scores[0]

for i in range(1,len(student_scores)):
  if highest_score < student_scores[i]:
    highest_score = student_scores[i]

print(f"The highest score in the class is: {highest_score}")