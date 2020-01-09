# ----1. 检查某个类是否有某种方法----
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(["Google", "Facebook"])
print(len(company))

# method 1
print(hasattr(company, "__len__"))

# method 2 (判定某个对象的类型): isinstance
from collections.abc import Sized
print(isinstance(company, Sized))


class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, A))


# ----2. 强制某个子类必须实现某些方法----
import abc


class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


# use metaclass, so error will be raised when we create an object rather than call object's function
# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError


class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass


redis_cache = RedisCache()
# redis_cache.set("key", "value")
