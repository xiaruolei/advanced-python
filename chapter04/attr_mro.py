class A:
    name = "class"

    def __init__(self):
        self.name = "obj"


# C3 algorithm
a = A()
print(a.name)


class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)