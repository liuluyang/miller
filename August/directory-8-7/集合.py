# ############## 定义方式 #################
set()
# set111 = {}
# set222 = set()
# print(type(set111))  # <class 'dict'>
# print(type(set222))  # <class 'set'>


# 利用天生的去重属性， 为列表去重
# li = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(li)
# set2222 = set(li)
# print(set2222)

# set1 = set(range(1, 11))
# print("set1", set1)


#  #################### 添加  #####################
# 添加一个可 哈希 的数据类型。 (不可变数据类型)
# set1.add((1, 2, 3))
# print(set1)


# #################### 删除 ######################
# discard删除集合中的一个成员， 如果所删除的成员不存在，就啥都不干
# set1.discard(2)
# print(set1)

# pop  # 随机弹出一个成员， 如果集合为空。 报错
# res = set1.pop()
# print(res)
# print(set1)

# remove  # 删除一个已存在的成员， 如果不存在报错 KeyError
# set1.remove(123)
# print(set1)

# ################### 查询 #########################
# 因为集合是无序的,没有索引无法通过索引查， 也无法通过 键查询，因为集合没有键这个说法。
# 所以想要查看所有的数据， 可以通过 for 循环， 一个一个的遍历出来查看。
# for i in set1:
#     print(i)


# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set2 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# set3 = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
#
# print("set1", set1)
# print("set2", set2)
# print("set3", set3)
# 差集  求两个集合 或者 多个集合的差集， 并返回一个新的集合。
# difference
# res = set1.difference(set2, set3)
# print(res)
# res = set1 - set2
# print(res)
#
#
# res = set2.difference(set1)
# print(res)
# res = set2 - set1
# print(res)

# 再原来的基础上修改，
# difference_update
# print(id(set1))

# set1.difference_update(set2)
# print(id(set1))


# 交集
# intersection
# res = set1.intersection(set2)
# print(res)
# res = set1 & set2
# print(res)

# intersection_update
# set1.intersection_update(set2, set3)
# print(set1)


# 并集  合集
#  ############## union #############
# res = set1 | set2 | set3
# print(res)
# res = set1.union(set2)
# print(res)
# ############## union ##############
# res = set1.union({"22": 123}.values())
# print(res)

# res = set1.union({"22": 123}.keys())
# print(res)

# res = set1.union({"22": 123}.items())
# print(res)

# res = set1.union([1, 2.4])
# print(res)
# 将一个可迭代对象中的每个元素添加到集合中，并返回一个新的集合


# ############## update ##############

# set1.update([1, 2, 4, 8, 9, 10, 89, 432, ])
# print(set1)
# set1.update(set2, set3)
# print(set1)

# 讲一个可迭代序列中的每个元素，添加到原集合中

# ##############################################################################
# 差集 -
# 对称差集 ^
# 交集 &
# 并集 |


# 对称差集
# res = set1.symmetric_difference(set2)
# print(res)
# res1 = (set1 - set2) | (set2 - set1)
# print(res1)


# set1.update(set2, set3)  # 求并集的
# set1.intersection_update(set2, set3)  # 交集的

# set1.difference_update(set2)  # 差集的
# set1.symmetric_difference_update(set2)  # 对称差集的


#########################################################################################################

# isdisjoint  # 报告两个集合是否有交集， 有就返回False，没有就返回True
# res = set1.isdisjoint(set2)
# print(res)


# set777 = {1, 2, 3, 4}
# set888 = {1, 2, 3, 4}

# issubset
# res = set777.issubset(set888)
# print(res)

# issuperset
# res = set888.issuperset(set777)
# print(res)

import random

nums = [random.randrange(1, 101) for _ in range(100)]

nums = nums.copy()

"""
1.求列表nums所有元素的和    nums_all
2.求列表nums所有奇数元素的和 nums_ji
3.求列表nums所有偶数元素的和 nums_ou
4.找出列表nums里面最大的数   nums_max 
5.找出列表nums里面最小的数   nums_min

6.找出列表nums里面相同元素分别有多少个 nums_count
8.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）
"""
# 1.求列表nums所有元素的和    nums_all
# res = sum(nums)

# 2.求列表nums所有奇数元素的和 nums_ji
# n = 0
# for i in nums:
#     if i % 2 != 0:
#         n += i
# print(n)
#
#
# res = sum([i for i in nums if i % 2 != 0])
# print(res)

# 3.求列表nums所有偶数元素的和 nums_ou
# n = 0
# for i in nums:
#     if i % 2 == 0:
#         n += i
# print(n)

# res = sum([i for i in nums if i % 2 == 0])
# print(res)

# 5.找出列表nums里面最小的数   nums_min
# n = nums[0]
# for i in nums:
#     if i < n:
#         n = i
# print(n)
#
# res = min(nums)
# print(res)

# 4.找出列表nums里面最大的数   nums_max
# n = nums[0]
# for i in nums:
#     if i > n:
#         n = i
# print(n)
#
# res = max(nums)
# print(res)

# 6.找出列表nums里面相同元素分别有多少个 nums_count

# dic = {}
# for i in nums:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)
# nums.sort()
# print(nums)

# dic = {}
# for i in nums:
#     dic.setdefault(i, [0])[0] += 1
#
# print(dic)
# nums.sort()
# print(nums)


# 8.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）

# print(nums)
# n = -1
# for i in range(len(nums)):
#     if nums[n] > 10:
#         nums.pop(n)
#     else:
#         n -= 1
#
# print(nums)


#####################################################################
# res = sum(nums)  # 全部和
# res = sum([i for i in nums if i % 2 == 0])  # 偶数
# res = sum([i for i in nums if i % 2 != 0])   # 奇数
# res = max(nums)
# res = min(nums)

# dic = {}
# for i in nums:
#     dic.setdefault(i, [0])[0] += 1

# res = set(nums)

# i = 1
# while i<=9:
#     for j in range(1, i+1):
#         print("{} * {} = {}".format(j, i, i*j), end="  ")
#     i+=1
#     print()
