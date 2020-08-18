# 多进程编程
# 耗cpu的操作，用多进程编程，对于I/O操作来说，使用多进程编程。进程切换的代价高于线程
import time
from concurrent import futures


# 对于消耗cpu的操作，多进程优于多线程
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


# 对于I/O操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    # with futures.ProcessPoolExecutor(3) as executor:
    # # with futures.ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, num) for num in range(25, 30)]
    #     start_time = time.time()
    #     for future in futures.as_completed(all_task):
    #         data = future.result()
    #         print("exe result: {}".format(data))
    # print(time.time() - start_time)

    # with futures.ProcessPoolExecutor(3) as executor:
    with futures.ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, num) for num in [2] * 30]
        start_time = time.time()
        for future in futures.as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
    print(time.time() - start_time)