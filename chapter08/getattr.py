# __getattr__, 查找不到属性的时候调用
# def __getattribute__, 首先调用这个函数，即便能查找到属性
from datetime import date


class User:
    # def __init__(self, name, birthday, info):
    #     self.name = name
    #     self.birthday = birthday
    #     self.info = info

    def __init__(self, info):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return "call __getattribute__ first"


if __name__ == "__main__":
    # user = User("Bob", date(year=2000, month=2, day=11), info={"company": "Google"})
    user = User(info={"company": "Google", "name": "Bob", "birthday": date(year=2000, month=2, day=11)})
    print(user.name)
    print(user.company)
    print(user.test)


