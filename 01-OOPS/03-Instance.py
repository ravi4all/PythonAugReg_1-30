class Emp:
    id = 101
    name = "Ram"
    age = 22

    def printEmp(self,id,name, age):
        print("Emp details",self.id, self.name,self.age)
        print("Emp details", id, name, age)

obj = Emp()
obj_1 = Emp()

obj.printEmp(102,"Shyam", 25)
print("Before :")
print(obj.name, obj.age)

print("After :")
obj.name = "Gopal"
obj.age = 29
print(obj.name, obj.age)

#Instance Variable
obj.salary = 15000
print("Salary is",obj.salary)

obj_1.salary = 18000
print("Object_2 details :",obj_1.name,obj_1.age,obj_1.salary)
