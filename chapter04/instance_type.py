class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print(id(B))
print(id(type(b)))
print(type(b))
print(type(b) is B)
print(type(b) is A)

