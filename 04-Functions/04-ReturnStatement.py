def add(x,y):
    return x + y

def sub(x,y):
    return x - y

print(add(1,2))
print(sub(3,1))


def calc(x,y):
    return x + y, x - y, x * y, x / y

# Packing
# opr = calc(12,5)
# print(opr)

# Unpacking
a,b,c,d = calc(12,5)
print(a,b,c,d)

def func1():
    return 1,2,3,4,5,6,7,8,9,10

a,*b,c,d = func1()
print(a,b,c,d)
