class Person:

    def __init__(self):
        self.company = "HCL"
        self.bank = "HDFC"
        self.name = ""
        self.age = None
        self.gender = ""
        self.salary = None

    def printPerson(self):
        print(self.__class__)
        print("Name : {}, Age : {}, Gender : {}, Salary : {}  ".format(self.name, self.age, self.gender, self.salary))

class Emp(Person):

    def __init__(self, name, age, gender, salary):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def printEmp(self):
        print(self.name,"Works in %s"%(self.company))
        print(self.name,"Has a account in %s"%(self.bank))

class Student(Person):

    def __init__(self, name, age, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender



student = Student("Ram", 21, "Male")
student.printPerson()

emp = Emp("Shyam", 26, "Male", 20000)
emp.printPerson()
emp.printEmp()
