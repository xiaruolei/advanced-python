def handle_item(item):
    return item * item


# 列表生成式
odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 1)
print(list(odd_gen))

# 字典推导式
my_dict = {"Bob": 20, "Jim": 21, "Tom": 22}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(my_set)
