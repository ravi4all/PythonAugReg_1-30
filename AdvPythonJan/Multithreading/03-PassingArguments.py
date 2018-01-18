import threading

def worker(num):
    # print(threading.current_thread().getName())

    print("Thread",num,"Entered")
    for i in range(10000000):
        pass

    print("Thread",num,"Exit")

for i in range(1,5):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()