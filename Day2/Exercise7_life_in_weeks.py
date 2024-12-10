age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#find left life
life_left = 90 - int(age)
#find in weeks
life_in_weeks = life_left * 52

#print using f-string
print(f"You have {life_in_weeks} weeks left.")