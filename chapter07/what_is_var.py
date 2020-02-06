# python和java中的变量本质不一样，python的变量实质上是一个指针
a = [1, 2, 3]
b = a
print(id(a), id(b))
print(a is b)
b.append(4)
print(a)


# is: compare id
# ==: compare content (def __eq__)
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(id(a), id(b))
print(a is b)  # id(a) != id(b)
print(a == b)


# class is an object, so we can get class's id
class People:
    pass


person = People()
if type(person) is People:
    print(type(person))
    print(id(type(person)))
    print(id(People))

if isinstance(person, People):
    print(type(person))