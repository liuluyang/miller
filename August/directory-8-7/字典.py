# staff_list = [
#     ["miller", 18, "CEO", '88888'],
#     ["black_girl", 24, "行政", '55555'],
#     ["liuser", 17, "董事长", "500"],
#     ["chenser", 30, "组长", "2"]
# ]

# for i in staff_list:
#     if i[0] == "black_girl":
#         print(i[3])
#         break


# dic = {"key1": ["value1", "value2"], "key2": "value2"}

# dic = {"key1": "value2", "key2": "value1"}
# print(dic)
# print(type(dic))  # <class 'dict'>


# ############ 创建字典的方式 ############
# persion1 = {"name":"miller", "age":23}   # 这种方式要熟练
# persion2 = dict(name='liuser',age=20)
# persion3 = dict({"name": "egon", 'age': 20})
# {}.fromkeys([1,2,3,4,5,6,7,8],100)

# persion1 = {"name": "miller", "age": 23}
# print(persion1)

# persion2 = dict(name='liuser', age=20)
# print(persion2)

# print({}.fromkeys([1, 2, 3, 4, 5, 6, 7, 8], 100))

# ############# 增加操作 #################

# names = {"miller": [23, "CEO", 66666] , "black_girl": [24, "行政", 40000]}
#
# names["liuser"] = [24, "董事长", 500]    # 这种方式要熟练
# print(names)
# #
# names.setdefault('olddriver', [50, 'driver', 10000])#
# print(names)

# {"key": "value"}
# ############### 修改操作 ####################
# names = {"miller": [23, "CEO", 66666], "black_girl": [24, "行政", 40000]}
# # print(names)
# # names["miller"][2] = 1000000000      # 这种方式要熟练
# # print(names)
#
# names.update({"miller": [29, "CEO", 10000]})
# print(names)
# names.update({"liuser": [29, "CEO", 10000]})
# print(names)
#
set
# ################ 删除操作 #####################

names = {'miller': [23, 'CEO', 66666], 'blackgirl': [24, '行政', 40000], 'liuser': [25, '讲师', '30000'],
        'olddriver': [50, 'driver', 10000], "old_village_master": [60, "village", 800000]}

res = names.pop("olddriver")
print(res)
print(names)

# result = names.popitem()
# print(result, type(result))  # <class 'tuple'>
# print(names)

# del names["blackgirl"]
# print(names)


# ################## 查询操作 #####################
# dict

# names = {'miller': [23, 'CEO', 66666], 'blackgirl': [24, '行政', 40000], 'liuser': [25, '讲师', '30000'],
#          'olddriver': [50, 'driver', 10000], "old_village_master": [60, "village", 800000]}

# for i in names:
#     print(names[i])

# for i in names.keys():
#     print(i)
#
# for i in names.values():
#     print(i)


# for key, value in names.items():
#     print(key, value)

# print(names["miller"])
#
# print(names.get("123", "没找到"))

# 'key' in dic #若存在则返回True，没有则返回False

# res = [50, 'driver', 10000] in names.values()
# print(res)

# staff_list = [
#     ["miller", 18, "CEO", '88888'],
#     ["black_girl", 24, "行政", '55555'],
#     ["liuser", 17, "董事长", "500"],
#     ["chenser", 30, "组长", "2"]
# ]

# staff_dict = {
#     "miller": {"name": "miller", "age": 18, "position": "CEO", "salary": 88888},
#     "black_girl": {"name": "black_girl", "age": 15, "position": "行政", "salary": 55555},
#     "liuser": {"name": "liuser", "age": 16, "position": "董事长", "salary": 500},
#     "chenser": {"name": "chenser", "age": 17, "position": "组长", "salary": 2},
# }


# print(staff_dict["black_girl"]["salary"])

# print(len(staff_dict))

# set1 = set(range(1, 11))
# set2 = set(range(6, 15))
# set3 = set(range(11, 20))
# print('set1', set1)
# print("set2", set2)
# print("set3", set3)

# ################### 两个 或 多个 集合求差集  符号 "-" #####################
# res = set1.difference(set2, set3)
# 返回一个新的集合，这个集合包含了 set1中有的并且在 set2 和 set3 中不存在的。
# 返回的是  set1 和其他集合的差集

# set1.difference_update(set2)  # 无返回值
# 将 set1 中有的 并且set2中也有的， 删除掉。只留下set1 中存在的。并修改了set1
# print(set1)


# ################### 两个 或 多个 集合求交集  符号 "&"  #####################
# res = set1.intersection(set2)
# 返回一个新的集合，这个集合中包含了 2个 或 多个集合中，共同存在的元素。
# print(res)
# res = set1 & set2
# print(res)

# set1.intersection_update(set2, set3)
# print(set1)
# res = set1 & set2 & set3
# print(res)
# 直接修改的是原集合, 得到的是 2 个或多个集合中，共同存在的元素。

# ################### 两个 或 多个 集合求并集 或 合集  符号  "|" #####################
# res = set1 | set2 | set3
# print(res)

# ################### 对称差集 s1-s2 | s2-s1 ##########################
# 对称差集只是两个差集之间的事。 不会涉及到第三个集合
# res = set1.symmetric_difference(set2)
# print(res)

# res = set1-set2 | set2-set1
# print(res)
# 对称差集 返回的是， set1中有 set2没有。和 set2中有 set1 中没有的。 两部分元素组成的一个集合。


# set1.symmetric_difference_update(set2)
# print(set1)
# 将两个集合分别作了差集，然后将得到的结果，作了并集。 或者可以理解成将得到的对称差集又重新赋值给了set1

# set1 = (set1 - set2) | (set2 - set1)
# print(set1)

# ss = set1 - set2
# sss = set2 - set1
#
# print(ss, sss)
# print(ss | sss)


# ##################### isdisjoint #################
# res = set1.isdisjoint(set3)
# print(res)
# 如果两个集合没有相交的返回 True 否则False

# ################ issubset ###############
# res = set1.issubset(set2)
# print(res)
# 报告另一个集合是否包含这个集合。(完全包含)

# ############## issuperset ############
# res = set1.issuperset(set2)
# print(res)
# 报告这个集合是否包含另一个集合 (完全包含)

# ############ pop ############
# res = set1.pop()
# print(res)
# 随机弹出一个值， 如果集合为空则抛出 KeyError

# ################## remove ###############
# set1.remove(2)
# print(set1)
# # 指定删除一个成员， 如果没有该成员则报错

# ############## discard ##############
# set1.discard(100)
# print(set1)
# 从集合中删除一个成员， 如果这个成员不存在则什么都不干

# ################ add ##################
# set1.add(1)
# print(set1)
# 向集合中添加一个成员。
# 如果原集合中不存在则增加一个， 已存在则没有任何效果。


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
# print(id(set1))
# set1.update([1,2,4,8,9,10,89,432,])
# print(set1, id(set1))

# 讲一个可迭代序列中的每个元素，添加到原集合中


# li = []

# print(bool("") is False)

#
# li = {"ss", "ssss", "sss", "sssss"}
#
# li1 = sorted(li, key=lambda x: len(x))
# print(li1)
