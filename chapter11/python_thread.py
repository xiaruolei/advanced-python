# 对于io操作来说，多线程和多进程性能操作不大
# 1. 通过thread类实例化

import time
import threading


def get_detail_html(url):
    print("get detail html start")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url start")
    time.sleep(4)
    print("get detail url end")


# 2. 通过继承Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html start")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url start")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    # # 当主线程退出的时候，子线程kill掉
    # # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    #
    # start_time = time.time()
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()
    #
    # print("Elapsed time: {}".format(time.time() - start_time))

    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")

    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("Elapsed time: {}".format(time.time() - start_time))

