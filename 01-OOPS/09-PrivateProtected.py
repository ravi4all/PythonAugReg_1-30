class Emp:

    # Protected
    _dept = "IT"

    # Private
    __salary = 25000

    def __init__(self, address):
        self.id = 101
        self.name = "Ram"
        self.age = 24
        self.__address = address

    def printEmp(self):
        print("Emp salary :",self.__salary)
        print("Emp Address :",self.__address)

obj_1 = Emp("Rohini, Delhi")
print(obj_1.name)
# print(Emp.__dict__)
obj_1._dept = "Manager"
print(obj_1._dept)
# print(obj_1.__salary)
obj_1.printEmp()
