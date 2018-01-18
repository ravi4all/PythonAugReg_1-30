import threading

def worker_1():
    print(threading.current_thread().getName(), "Started")
    # print("Worker_1 Init")

    for i in range(10000000):
        pass

    # print("Worker_1 End")
    print(threading.current_thread().getName(), "Ended")

def worker_2():
    print(threading.current_thread().getName(), "Started")
    # print("Worker_2 Init")

    for i in range(100000):
        pass

    # print("Worker_2 End")
    print(threading.current_thread().getName(), "Ended")

def worker_3():
    print(threading.current_thread().getName(), "Started")
    # print("Worker_3 Init")

    for i in range(100000):
        pass

    # print("Worker_3 End")
    print(threading.current_thread().getName(), "Ended")

def worker_4():
    print(threading.current_thread().getName(), "Started")
    # print("Worker_4 Init")

    for i in range(10000000):
        pass

    # print("Worker_4 End")
    print(threading.current_thread().getName(), "Ended")

# worker_1()
# worker_2()
# worker_3()
# worker_4()

thread_1 = threading.Thread(target=worker_1)
thread_2 = threading.Thread(target=worker_2)
thread_3 = threading.Thread(target=worker_3)
thread_4 = threading.Thread(target=worker_4)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# print(threading.current_thread().getName())