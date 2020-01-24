# set: 无序， 不重复
s1 = set('abc')
s1 = set(['a', 'b', 'c'])
s1 = {'a', 'b', 'c'}
s2 = frozenset('abc')  # 作为dict的key

# add
s1.add('d')

# update
s3 = set('def')
s1.update(s3)

s1 = set('abcd')
s3 = set('def')
res_set = s1.difference(s3)
res_set = s1 - s3
res_set = s1 | s3
res_set = s1 & s3
print(res_set)

if 'c' in s1:
    print("c in set1")