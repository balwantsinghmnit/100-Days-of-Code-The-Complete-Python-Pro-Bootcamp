print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#add and make one string
name = name1 + name2
#lower it 
name = name.lower()

#count for true
digit1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")

#count for love
digit2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

answer = digit1 * 10 + digit2

if answer < 10 or answer > 90:
    print(f"Your score is {answer}, you go together like coke and mentos.")
elif answer >40 and answer < 50:
    print(f"Your score is {answer}, you are alright together.")
else:
    print(f"Your score is {answer}.")