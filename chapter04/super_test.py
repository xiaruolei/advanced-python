# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#         super(B, self).__init__()
#
# from threading import Thread
# class MyThread(Thread):
#     def __init__(self, name, user):
#         self.user = user
#         super().__init__(name=name)


class A:
    def __init__(self):
        print("A")
        print("end A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()
        print("end B")


class C(A):
    def __init__(self):
        print("C")
        super().__init__()
        print("end C")


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()
        print("end D")


if __name__ == "__main__":
    # b = B()
    print(D.__mro__)
    d = D()
