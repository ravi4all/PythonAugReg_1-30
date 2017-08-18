a = 25

for i in range(2,a):
    if a%i == 0:
        print("Not Prime Number")
        print("a % {} == 0".format(i))
        break
else:
    print("Prime Number")
