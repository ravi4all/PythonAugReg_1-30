# DRY - Donot Repeat Yourself

def one():
    print("This is my first function")

# one()

def add():
    a = 10
    b = 12
    print(a+b)
    one()

add()
