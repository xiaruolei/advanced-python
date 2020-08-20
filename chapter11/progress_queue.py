import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe
# from queue import Queue
# # Queue的种类
# from queue import Queue
# from multiprocessing import Queue
# from multiprocessing import Manager
# q = Manager().Queue()


# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# # multiprocessing中的queue不能用于pool进程池
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue, ))
#     pool.apply_async(consumer, args=(queue, ))
#     pool.close()
#     pool.join()


# # 通过pipe实现进程间通信
# # pipe的性能高于queue
# def producer(pipe):
#     pipe.send("a")
#     time.sleep(2)
#
#
# def consumer(pipe):
#     time.sleep(2)
#     data = pipe.recv()
#     print(data)
#
#
# if __name__ == "__main__":
#     start = time.time()
#     receive_pipe, send_pipe = Pipe()
#     # pipe只能适用于两个进程
#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(receive_pipe,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()
#     print(time.time() - start)


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    progress_dict = Manager().dict()
    first_progress = Process(target=add_data, args=(progress_dict, "a", 1))
    second_progress = Process(target=add_data, args=(progress_dict, "b", 2))

    first_progress.start()
    second_progress.start()

    first_progress.join()
    second_progress.join()

    print(progress_dict)
