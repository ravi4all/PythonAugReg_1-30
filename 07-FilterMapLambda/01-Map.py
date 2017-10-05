def tempConv(x):
    return float(9/5 * x+32)

temp = [34.5,38.1,33.2,32.2,35.4]

# for i in temp:
#     print(tempConv(i))

# f = list(map(tempConv, temp))
# print(f)

def even(num):
    return num%2 == 0

a = [x for x in range(101)]

x = list(map(even, a))
print(x)
