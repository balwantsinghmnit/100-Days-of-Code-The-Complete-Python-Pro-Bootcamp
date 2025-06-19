import random
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

'''
password = ""

for i in range(nr_letters):
    random_char = random.choice(characters)
    password += random_char
for i in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
for i in range(nr_numbers):
    random_digit = random.choice(numbers)
    password += random_digit

print(password)
'''
password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(characters))
for i in range(nr_symbols):
    password_list.append(random.choice(symbols))
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for x in password_list:
    password += x
print(f"Your Password is : {password}")


