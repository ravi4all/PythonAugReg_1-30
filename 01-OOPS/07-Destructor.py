import weakref
class Car:

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def printCar(self):
        print("Car Details :",self.name,self.color,self.speed)

    def __del__(self):
        print("Object destroyed...",self.name)


audi = Car("Audi", "Red", 250)
audi.printCar()
audi_version_2 = audi

print(audi)

bmw = Car("BMW", "Black", 200)
bmw.printCar()
print(bmw)

print("Weak Ref Before:",weakref.ref(bmw))
bmw = None
# print("Weak Ref After:",weakref.ref(bmw))

# del audi
# print("Audi Instance :", isinstance(audi_version_2, Car))
# print("BMW Object",bmw)
