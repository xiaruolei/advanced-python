def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


def say(self):
    return self.name


class Base:
    def answer(self):
        return "base"


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


from collections.abc import *
if __name__ == "__main__":
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    # # type 创建动态类
    # User = type("User", (Base,), {"name":  "user", "say": say})
    # my_obj = User()
    # print(User.name)
    # print(my_obj.name)
    # print(my_obj.say())
    # print(my_obj.answer)

    my_obj = User(name="Bob")
    print(my_obj)

