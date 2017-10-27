class Car:

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def printCar(self):
        print("Car Details :",self.name,self.color,self.speed)


audi = Car("Audi", "Red", 250)
audi.printCar()

bmw = Car("BMW", "Black", 200)
bmw.printCar()
