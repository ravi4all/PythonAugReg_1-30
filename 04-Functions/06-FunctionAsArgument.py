def one():
    print("Hello this is function one")

def two(func):
    # func = one
    print("Hello this is function two")
    # func() = one()
    func()

# We can pass function as an argument
two(one)
