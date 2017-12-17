import threading

def worker():
    print(threading.current_thread().getName())

# worker()

for i in range(5):
    thread = threading.Thread(target=worker, name="Thread_"+str(i))
    thread.start()
