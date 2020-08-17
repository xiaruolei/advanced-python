from concurrent import futures

# 线程池， 为什么要线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致


import time


def get_html(times):
    # print("processing page {}".format(times))
    time.sleep(times)
    print("processed page {}".format(times))
    return times


# # 通过submit函数提交执行的函数到线程池中, submit 是立即返回
# executor = futures.ThreadPoolExecutor(max_workers=4)
# task1 = executor.submit(get_html, 3)
# task2 = executor.submit(get_html, 2)
#
# # 取消未开始的线程
# print("task2 cancel:", task2.cancel())
#
# # done方法用于判定某个任务是否完成
# print("task1 done:", task1.done())
# time.sleep(3)
# print("task1 done:", task1.done())
#
# # result方法可以获取task的执行结果
# print("task1 result:", task1.result())


# # 获取已经成功的task的返回
# executor = futures.ThreadPoolExecutor(max_workers=4)
# urls = [3, 2, 4]
# all_tasks = [executor.submit(get_html, url) for url in urls]
# for future in futures.as_completed(all_tasks):
#     data = future.result()
#     print("page {} success".format(data))


# # 通过executor的map获取已经完成的task的值
# executor = futures.ThreadPoolExecutor(max_workers=2)
# urls = [3, 2, 4]
# for data in executor.map(get_html, urls):
#     print("page {} success".format(data))


# wait等待某个事件的发生
executor = futures.ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]
all_tasks = [executor.submit(get_html, url) for url in urls]
futures.wait(all_tasks, return_when=futures.FIRST_COMPLETED)
print("main")
for future in futures.as_completed(all_tasks):
    data = future.result()
    print("page {} success".format(data))