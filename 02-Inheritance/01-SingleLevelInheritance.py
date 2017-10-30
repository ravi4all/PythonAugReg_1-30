class Car:

     def __init__(self):
         self.color = "Red"
         self.speed = 200
         self.gear = "Automatic"

class Maruti(Car):

    # Constructor Overloading
    def __init__(self):
        super().__init__()
        self.color = "Blue"

    def printUser(self):
        print("Car Details :",self.color, self.speed, self.gear)

obj_1 = Maruti()
obj_1.printUser()
