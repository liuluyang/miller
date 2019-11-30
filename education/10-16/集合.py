# a = {1, 2, 3, 4, 2, 'miller', 3, 'liuser', 'miller'}

# print(a)  # {1, 2, 3, 4, 'miller', 'liuser'}

# dic = {}
# print(type(dic))

# print(type(set()))

# a = [1, 2, 3, 4, 2, 'miller', 3, 'liuser', 'miller']
# a = set(a)
# print(a)


# a = {1, 2, 3, 4, 'liuser', 'miller'}
# a.add("old_driver")
# print(a)
# a.add((1,2))
#
# print(a)


# a = {1, 2, 3, 4, 'liuser', 'miller'}
#
# a.discard("liuser")
# a.discard("xxxxxxx")  # 如果删除不存在的元素， 什么都不干
# print(a)

# a = {1, 2, 3, 4, 'liuser', 'miller'}

# b = a.pop()
# print(b)


# a = {1, 2, 3, 4, 'liuser', 'miller'}
# a.remove(5555)
# print(a)


set1 = {"miller", "liuser", "olddriver", 1, 2, 3, 5, 6}
set2 = {2, 3, "rain", "黑姑娘", "周xc", "张bz", "miller"}


# res = set1 & set2
# print(res)
# res = set1.intersection(set2)
# print(res)


# res = set1 | set2
# print(res)
# res = set1.union(set2)
# print(res)


# res = set2 - set1
# print(res)  # {'rain', '周xc', '张bz', '黑姑娘'}
# res = set2.difference(set1)  # set2 - set1  # {'rain', '周xc', '张bz', '黑姑娘'}
# print(res)


# res = set1 - set2
# print(res)  # {1, 5, 6, 'olddriver', 'liuser'}
# res = set1.difference(set2)  # set1 - set2  # {1, 5, 6, 'liuser', 'olddriver'}
# print(res)


# res = (set1-set2) | (set2-set1)
# print(res)
# res = set1 ^ set2
# print(res)
# res = set1.symmetric_difference(set2)
# print(res)


# set1.intersection_update(set2)
# print(set1)

# set1.update(set2)
# print(set1)

# set1.difference_update(set2)
# print(set1)
# set2.difference_update(set1)
# print(set2)

# set1.symmetric_difference_update(set2)
# print(set1)


# & | - ^

