class Person:

    def __init__(self):
        self.company = "HCL"
        self.bank = "HDFC"
        self.name = ""
        self.age = None
        self.gender = ""
        self.salary = None

class Emp:

    def __init__(self, name, age, gender, salary):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def printEmp(self):
        print(self.name,"Works in %s"%(self.company))
        print(self.name,"Has a account in %s"%(self.bank))

    def printPerson(self):
        print("Name : {}, Age : {}, Gender : {}, Salary : {}  ".format(self.name, self.age, self.gender, self.salary))

class Department(Person, Emp):

    def __init__(self, name, age, gender, salary):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.dept = "IT"
        Emp.__init__(self, self.name, self.age, self.gender, self.salary)

    def printEmp(self):
        print(self.name, "is in {} department".format(self.dept))
        print(self.name,"Has a account in %s"%(self.bank))


obj = Department("Ram", 21, "Male", 15000)
obj.printPerson()
obj.printEmp()
