import threading

def func_1():
    print("Thread_1 Started...")
    for i in range(1,10):
        print("Iteration completed",i)
    print("Thread_1 Ended...")


def func_2():
    print("Thread_2 Started...")
    for i in range(10,20):
        print("Iteration completed",i)
    print("Thread_2 Ended...")


def func_3():
    print("Thread_3 Started...")
    for i in range(20,30):
        print("Iteration completed",i)
    print("Thread_3 Ended...")


t1 = threading.Thread(target=func_1)
t2 = threading.Thread(target=func_2)
t3 = threading.Thread(target=func_3)

t1.start()
t2.start()
t3.start()
