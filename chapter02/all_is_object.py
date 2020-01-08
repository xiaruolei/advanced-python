def ask(name="name in func"):
    print(name)


class Person:
    def __init__(self):
        print ("name in class")


def decorator_func():
    print("dec start")
    return ask

# 函数和类也是对象
# 赋值给一个变量
# my_func = ask
# my_func("hi")

# my_class = Person
# my_class()


# 添加到集合对象中
# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())


# 函数的返回值
my_ask = decorator_func()
my_ask("name in decorator func")
