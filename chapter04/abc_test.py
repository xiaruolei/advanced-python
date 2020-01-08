# 检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(["Google", "Facebook"])
print(len(company))

# method 1
print(hasattr(company, "__len__"))

# method 2 (判定某个对象的类型)
from collections.abc import Sized
print(isinstance(company, Sized))


# 强制某个子类必须实现某些方法
class CacheBase(object):
    def get(self, key):
        pass

    def set(self, key, value):
        pass
