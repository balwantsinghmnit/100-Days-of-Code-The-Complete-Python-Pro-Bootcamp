#print welcome message
print("Welcome to the tip calculator!")

#ask for total bill amount
print("What was the total bill? $",end="")

#take bill amount input
bill_amount = float(input())

#ask how much tip user want to give
print("How much percentage tip would you like to give? 10%, 12%, or 15%? ",end="")
#take tip amount input
tip_amount = float(input())

#ask for how many people bill should be splited
print("How many people to split the bill?",end="")

#take no. of people input
total_people = float(input())

#calculate tip as percentage
tip_in_percentage = tip_amount/100

#total tip calculation
total_tip = bill_amount * tip_in_percentage

#total bill calculation
total_bill = bill_amount + total_tip

#per person bill calculation
per_person_bill = total_bill/total_people

#convert upto 2 decimal point
per_person_bill = "{:.2f}".format(per_person_bill)

#print per person bill amount
print(f"Each person should pay: ${per_person_bill}")