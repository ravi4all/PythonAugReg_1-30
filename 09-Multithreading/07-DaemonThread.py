import threading
import time

def worker():
    thread_name = threading.current_thread().getName()
    print("Thread {} enters".format(thread_name))

    time.sleep(2)

    print("Thread {} exits".format(thread_name))


def worker_2():
    thread_name = threading.current_thread().getName()
    print("Thread {} enters".format(thread_name))

    for i in range(1,100000000):
        pass

    print("Thread {} exits".format(thread_name))

for i in range(5):
    thread = threading.Thread(target=worker)
    thread.start()

thread_2 = threading.Thread(target=worker_2, daemon=True)
thread_2.start()
