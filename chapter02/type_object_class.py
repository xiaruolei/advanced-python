# type -> class -> obj


# type -> int -> 1
a = 1
print(type(1))
print(type(int))

# type -> str -> "abc"
b = "abc"
print(type(b))
print(type(str))


# type -> Student -> Student obj
class Student:
    pass


c = Student()
print(type(c))
print(type(Student))


# type -> Mystudent > Mystudent obj
class MyStudent(Student):
    pass


d = MyStudent()
print(type(d))

# obj 是最顶层基类， 所有类的父类都是obj
print(Student.__base__)
print(MyStudent.__base__)

print(type.__base__)
print(type(object))
print(object.__bases__)
print(type(type))
