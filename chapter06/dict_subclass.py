# 不建议继承list和dict
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


d1 = Mydict(one=1)
print(d1)
d1["one"] = 1
print(d1)

# 如果继承dict，继承UserDict
from collections import UserDict
class MyUserdict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


d2 = MyUserdict(one=1)
print(d2)

from collections import defaultdict
d3 = defaultdict(dict)
print(d3["key"])


