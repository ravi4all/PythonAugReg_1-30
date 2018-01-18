import threading
import time

def worker(num):
    print("Thread {} Entered".format(num))

    print("Thread {} going to sleep".format(num))
    time.sleep(2)
    print("Thread {} wake".format(num))
    # for i in range(10000):
    #     pass

    print(threading.current_thread().getName(),"Exit")

for i in range(1,6):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()