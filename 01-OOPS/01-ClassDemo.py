class Emp:
    """This is my first class demo..."""
    print("This is a class...")

# Main Module
print(__name__)

# __name__ = 'ravi'

if __name__ == '__main__':
    # Making Object of Emp classs
    obj = Emp()
    print(obj)
    print(type(obj))
    # Will return name of class
    print(Emp.__name__)
    # Will return type of class Emp
    print(Emp.__class__)
    # Will return type of obj
    print(obj.__class__)
    # Will tell if obj belongs to class Emp
    print(isinstance(obj, Emp))
    # Printing the doc string of class Emp
    print(Emp.__doc__)
else:
    print("Name was changed...")
