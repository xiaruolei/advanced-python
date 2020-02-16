from datetime import date, datetime
import numbers

'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：

（1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则

（2）如果“age”出现在obj(user)的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则

（3）如果“age”出现在User或其基类的__dict__中

（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则

（3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError

'''


# data descriptor
class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("That was no valid number.")
        if value < 0:
            raise ValueError("Number is negative")
        self.value = value

    def __delete__(self, instance):
        pass


# non data descriptor
class NonDataIntField:
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()
    # age = NonDataIntField()


if __name__ == "__main__":
    user = User()

    user.age = 30
    print(user.__dict__)
    print(user.age)

    # user.__dict__["age"] = 30
    # print(user.__dict__)
    # print(user.__dict__["age"])
    # print(user.age)

    # print(getattr(user, 'age'))
