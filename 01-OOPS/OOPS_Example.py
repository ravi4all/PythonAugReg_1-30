import getpass
class ATM:
    """This is ATM example"""
    def __init__(self, pin):
        self.__pin = pin
        self.name = "Ram"
        self.bank = "HDFC"
        self.totalBal = 25000

    def authenticateUser(self):
        if self.__pin == "1234":
            self.welcomeUser()
        else:
            print("You are a fraud...")

    def welcomeUser(self):
        print("Welcome {} to {}".format(self.name, self.bank))
        self.atmMenu()

    def atmMenu(self):
        print("""
        1. Withdraw
        2. Deposit
        3. Balance Enquiry
        4. PIN Change
        """)

        todo = {
            "1" : self.withdraw,
            "2" : self.deposit,
            "3" : self.balEnq,
            "4" : self.pinChange
        }

        userChoice = input("Enter your choice : ")

        todo.get(userChoice)()

    def withdraw(self):
        amount = int(input("Enter the amount : "))
        if amount > self.totalBal:
            print("Not enough balance...")
        else:
            self.totalBal = self.totalBal - amount
            print("Remaining Balance is",self.totalBal)
        self.atmMenu()

    def deposit(self):
        amount = int(input("Enter the amount : "))
        self.totalBal = self.totalBal + amount
        print("Available Balance is",self.totalBal)
        self.atmMenu()

    def balEnq(self):
        print("Your balance is",self.totalBal)
        self.atmMenu()

    def pinChange(self):
        newPin = input("Enter new PIN : ")
        self.__pin = newPin
        print("PIN Changed Successfully...")
        self.atmMenu()

print("*********** Welcome to HDFC Bank *************")
pin = input("Enter your PIN :")

# print("Enter your PIN : ")
# pin = getpass.getpass()

if __name__ == '__main__':
    obj_1 = ATM(pin)
    obj_1.authenticateUser()
