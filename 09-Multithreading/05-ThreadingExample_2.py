import threading

def banking(num):
    print("Thread {} enters".format(num))
    userName = input("Enter your name : ")
    print("Welcome",userName)
    
    for i in range(1,10000):
        pass

    print("Thread {} exits".format(num))


for i in range(6):
    thread = threading.Thread(target=banking, args=(i,))
    thread.start()
