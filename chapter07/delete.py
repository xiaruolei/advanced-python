# python中垃圾回收的算法是采用引用技术
a = object()
b = object()

del a
print(b)


class A:
    def __del__(self):
        pass