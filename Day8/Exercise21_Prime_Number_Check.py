# Write your code below this line 👇
import math

def prime_checker(number):
  prime_flag = True
  for i in range(2,math.floor(math.sqrt(number))+1):
    if number%i==0:
      prime_flag = False
      break
  if number<2 or not prime_flag:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)