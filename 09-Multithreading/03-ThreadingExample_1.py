import threading

def worker(num):
    print("Thread {} enters".format(num))
    for i in range(1,10000):
        for j in range(1,10000):
            i + j
    print("Thread {} exits".format(num))



for i in range(1,6):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
