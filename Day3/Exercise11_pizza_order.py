print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

small_pizza = 15

medium_pizza = 20

large_pizza = 25

small_pepp = 2

medium_pepp = 3

large_pepp = 3

extra_cheese_cost = 1

total = 0
#check size
if size == "S":
    total += small_pizza
    if add_pepperoni == "Y":
        total += small_pepp
elif size == "M":
    total += medium_pizza
    if add_pepperoni == "Y":
        total += medium_pepp
elif size == "L":
    total += large_pizza
    if add_pepperoni == "Y":
        total += large_pepp

if extra_cheese == "Y":
    total += extra_cheese_cost

print(f"Your final bill is: ${total}.")