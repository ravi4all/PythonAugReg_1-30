import threading

def worker():
    print(threading.current_thread().getName())

    for i in range(10000000):
        pass

    print(threading.current_thread().getName(), "Ended")

for i in range(1,5):
    thread = threading.Thread(target=worker, name="Worker_"+str(i))
    thread.start()