# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#calculate bmi
bmi = float(weight)/(float(height)*float(height))

#print answer
print(int(bmi))
