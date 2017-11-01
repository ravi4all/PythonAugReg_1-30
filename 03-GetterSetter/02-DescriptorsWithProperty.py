# Descriptors - Getters and Setters
class Person:

    def __init__(self):
        self.__name = ""

    def fset(self, value):
        self.__name = value
        print("Setting {}".format(self.__name))

    def fget(self):
        print("Getting {}".format(self.__name))
        return self.__name

    def fdel(self):
        print("Deleting {}".format(self.__name))

    userName = property(fget, fset, fdel, "I am property..")

obj = Person()
obj.userName = "Ram"
obj.userName
del obj.userName
