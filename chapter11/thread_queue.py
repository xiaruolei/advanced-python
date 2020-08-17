# 线程间通信
import time
import threading
from chapter11 import variables


def get_detail_html(lock):
    # 爬取文章详情
    while True:
        lock.acquire()
        if len(variables.detail_url_list) > 0:
            url = variables.detail_url_list.pop()
            lock.release()
            print("get detail html start")
            time.sleep(2)
            print("get detail html end")
        else:
            lock.release()
            time.sleep(1)


def get_detail_url(lock):
    # 爬取文章列表页
    while True:
        print("get detail url start")
        time.sleep(4)
        for i in range(10):
            lock.acquire()
            if len(variables.detail_url_list) >= 10:
                lock.release()
                time.sleep(1)
            else:
                variables.detail_url_list.append("http://google.com/{id}".format(id=i))
                lock.release()
        print("get detail url end")


# 线程间通信方式：共享变量
if __name__ == "__main__":
    lock = threading.RLock()
    thread_detail_url = threading.Thread(target=get_detail_url, args=(lock,))
    thread_detail_url.start()

    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(lock,))
        thread_detail_html.start()

    start_time = time.time()

    # thread_detail_url.join()
    # thread_detail_html.join()

    # 当主线程退出的时候， 子线程kill掉
    print("Elapsed time: {}".format(time.time() - start_time))