target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

answer = 0
i=2
while i<=target:
    if i%2==0:
        answer += i
    i += 2
print(answer)