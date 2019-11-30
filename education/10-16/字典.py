# staff_list = [
# [“miller”, 23, ‘CEO’, ‘88888’],
# [‘黑姑娘’, 24, ‘行政’, ‘55555’],
# [‘liuser’, 25, ‘讲师’, ‘44444’],
# [‘egon’, ‘33’, ‘组长’, ‘77777’],
# xxxxxx
# xxxx
# xxxxx
# ]


# for i in staff_list:
#     if i[0] == "黑姑娘":
#         print()


# user_info1 = {"username": "miller", "password": 123564789}
# user_info2 = dict(username="miller", password=123456789)
#
# user_info3 = {}.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100)
# print(user_info3)


# names = {"miller": [23, "CEO", 66666], "blackgirl": [24, "行政", 40000]}
# names["liusir"] = [26, "teacher", 5555]
# names.setdefault("old_driver", [50, 'driver', 10000])
# print(names.pop("blackgirl"))
# print(names)


# print(names.popitem())
#
# print(names)


# dic1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
# dic2 = {"key3": "xxxxxx", "key4": "value4"}
#
# dic1.update(dic2)
#
# print(dic1)


# dic1 = {"key1": "value1", "key2": "value2", "key3": "value3"}

# print(dic1["xxxxx"])  # 查询不存在的key  会抛出异常

# print(dic1.get("xxxxx"))

# print(dic1.items())


# dic = {"name": "miller", "age": 28, "phone": 132467468, "position": "CEO", "salary": 2222}
# li = list(dic.keys())
# for i in enumerate(li):
#     print(i)


# dic = {}
# for i in range(100):
#     dic[i] = i*2
#
# print(dic)


dic = {"k0": 0, "k1": 1, "k2": 2, "k3": 3, "k4": 4, "k5": 5, "k6": 6, "k7": 7, "k8": 8, "k9": 9}

for i in dic:
    if 5 < int(i.replace("k", "")):
        print(dic[i])

# for k, v in dic.items():
#     if v % 2 == 0 and v != 0:
#         dic[k] = -1
#
# print(dic)


