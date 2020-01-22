import bisect
from collections import deque

# 用来处理已排序的序列，用来维持已排序的序列，升序
# 二分查找
int_list = []
int_list = deque()
bisect.insort(int_list, 3)
bisect.insort(int_list, 2)
bisect.insort(int_list, 5)
bisect.insort(int_list, 1)
bisect.insort(int_list, 6)
print(int_list)
