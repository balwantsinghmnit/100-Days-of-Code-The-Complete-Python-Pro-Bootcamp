#take input

number = input("Enter a two digit number")

#extract digits from input
first_digit = number[0]
second_digit = number[1]

#convert to integer and add
answer = int(first_digit) + int(second_digit)

#print the answer
print(answer)
