# Descriptors - Getters and Setters

class Person:

    def __init__(self):
        self.company = "HCL"
        self.bank = "HDFC"
        self.name = ""
        self.age = None
        self.gender = ""
        self.__salary = None

    def __set__(self, instance, value):
        self.__salary = value
        print("Setting...",self.__salary)

    def __get__(self, instance, owner):
        print("Getting", self.__salary)
        return self.__salary

class Emp:
    userName = Person()

obj = Emp()
obj.userName = "Ram"
obj.userName
