class Player:

    def __init__(self):
        self.name = []
        self.score = []

    def appendData(self,n,s):
        self.name.append(n)
        self.score.append(s)
        print("Name is",self.name)
        print("Score is",self.score)

obj_1 = Player()
obj_1.appendData("Sachin", 55)

obj_2 = Player()
obj_2.appendData("Dravid", 78)
