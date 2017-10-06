# def even(num):
#     return num%2 == 0

a = [x for x in range(101)]

x = list(filter(lambda num: num%2 == 0, a))
print(x)

temp = [34.5,38.1,33.2,32.2,35.4]

f = list(map(lambda c: float(9/5 * c+32), temp))
print(f)
