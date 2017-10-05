def even(num):
    return num%2 == 0

a = [x for x in range(101)]

x = list(filter(even, a))
print(x)
