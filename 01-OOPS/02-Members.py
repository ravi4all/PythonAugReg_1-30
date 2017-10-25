# Members - Data Members and Member Functions

class Emp:
    # Data Members/Class Variables
    id = 101
    name = "Ram"
    age = 22

    # Member functions/Class functions/Methods
    def printEmp(alpha,id,name, age):
        print("Emp details",alpha.id, alpha.name,alpha.age)
        print("Emp details", id, name, age)


obj = Emp()
obj.printEmp(102,"Shyam", 25)
