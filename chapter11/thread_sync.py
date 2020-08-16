import threading

total = 0
lock = threading.Lock()
rlock = threading.RLock() # 在同一个线程里面，可以连续调用多次acquire，一定要注意acquire的次数要和release的次数相等


def add():
    global total
    global rlock
    for i in range(10000):
        rlock.acquire()
        total += 1
        dosomething(lock)
        rlock.release()


def desc():
    global total
    global rlock
    for i in range(10000):
        rlock.acquire()
        total -= 1
        rlock.release()


def dosomething(lock):
    rlock.acquire()
    # do something
    rlock.release()


if __name__ == "__main__":
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(total)

    # 1. 用锁会影响性能
    # 2. 锁会引起死锁
    # 3. 死锁的情况
    """
    A(a, b)
    acquire(a)
    acquire(b)
    
    A(a, b)
    acquire(b)
    acquire(a)
    """
