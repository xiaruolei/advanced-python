my_list = []
my_list.append(1)
my_list.append("a")

from collections import abc

a = [1, 2]
c = a + [3, 4]
print(c)
a += [3, 4]
print(a)

# c = a + (3, 4) # -> not valid
a += (3, 4)  # -> valid
print(a)
a.extend(range(3))
print(a)
a.append([1, 2])
print(a)
