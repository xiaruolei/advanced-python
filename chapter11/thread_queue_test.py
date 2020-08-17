# 通过queue的方式进行线程间同步

from queue import Queue
import time
import threading


def get_detail_html(queue):
    # 爬取文章详情
    while True:
        url = queue.get()
        print("get detail html start")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    # 爬取文章列表页
    for _ in range(10):
        print("get detail url start")
        time.sleep(4)
        for i in range(20):
           queue.put("http://google.com/{id}".format(id=i))
        print("get detail url end")


# 线程间通信方式：共享变量
if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()

    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        thread_detail_html.start()

    start_time = time.time()

    # detail_url_queue.task_done()
    detail_url_queue.join()

    print("Elapsed time: {}".format(time.time() - start_time))