# Closures
def outer(x):

    # Nested Function
    def inner():
        return  x + 1
    # Return nested function
    return inner

x = outer(2)
print(x())
