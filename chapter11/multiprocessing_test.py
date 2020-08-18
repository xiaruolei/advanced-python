import os
import multiprocessing
import time

# # fork只能用于linux/unix中
# print("bobby")
#
# pid = os.fork()
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))


def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


# 使用线程池
pool = multiprocessing.Pool(multiprocessing.cpu_count())
# result = pool.apply_async(get_html, args=(3,))
#
# #等待所有任务完成
# pool.close()
# pool.join()
#
# print(result.get())

# imap
# for result in pool.imap(get_html, [1,5,3]):
#     print("{} sleep success".format(result))

for result in pool.imap_unordered(get_html, [1, 5, 3]):
    print("{} sleep success".format(result))
