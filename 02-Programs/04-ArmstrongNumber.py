num = 153
temp = num
sum = 0

while temp > 0:
    r = temp%10
    sum = sum + r**3
    temp = temp//10

if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")