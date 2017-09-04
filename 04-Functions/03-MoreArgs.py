# def emp(id,name,age):
#     # print("Id is {}, Name is {}, Age is {}".format(id, name, age))
#     # print("Id is %s, Name is %s, Age is %s"%(id, name, age))
#     # print("Id is",id, "Name is",name, "Age is",age)
#     print(
# """ID is {}
# Name is {}
# Age is {}
# """.format(id, name, age))

id = 1
name = "Ravi"
age = "16"

def emp(id,name,age):
    print("Id is {}, Name is {}, Age is {}".format(id, name, age))


emp(101, "Ram", 20)
emp(id=102, name = "Shyam", age=22)
emp(id, name, age)

def empAddress(*address):
    # print("Address is {}".format(address))
    print("Address is")
    for a in address:
        print(a)

empAddress("Office Address", "Home Address", "Office_2 Address")

empAddress({"home":"Home Address", "office" : ["Office Address_1, Office Address_2"]})
