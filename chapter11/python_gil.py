# gil: global interpreter lock
# python中的一个线程对英语c语言中的一个线程
# gil使得同一时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上
# gil会根据执行的字节码行数以及时间片释放gil， gil在遇到io的操作时主动释放

# import dis
#
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))


total = 0


def add():
    global total
    for i in range(10000):
        total += 1


def desc():
    global total
    for i in range(10000):
        total -= 1


import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)
