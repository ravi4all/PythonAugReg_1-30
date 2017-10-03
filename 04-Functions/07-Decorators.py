# Closures with Decorators
def outer(msg):
    def inner():
        print("This is inner function")
        return msg()
    return inner

# Decorator
@outer
def function2():
    print("This is function 2")

# Passing function as an argument
# x = outer(function2)
# x()

function2()
