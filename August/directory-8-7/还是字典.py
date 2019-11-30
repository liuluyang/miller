# 创建
# dic = {"name": "miller"}
# print(type(dic), dic)  # <class 'dict'>

# dic = dict(name="miller", age=23)
# print(type(dic), dic)  # <class 'dict'>

# print(id(dic), dic)
# dic = dict({"name": "miller"})
# print(id(dic), dic)

# 增

# dic = {"name": "miller"}
# dic["age"] = 23
# print(dic)
#
# dic.update({"salary": 10000})
# print(dic)
#
# dic.setdefault("height", 173)
# print(dic)

# 改

# dic = {"name": "miller"}
#
# dic["name"] = "liuser"
# print(dic)
#
# dic.update({"name": "black_girl"})
# print(dic)

# 查

# dic = {"name": "miller"}
# res = dic["name"]
# print(res)

# res = dic.get("123", "没找到")
# print(res)


# names = {
#     'miller': [23, 'CEO', 66666],
#     'blackgirl': [24, '行政', 40000],
#     'liuser': [25, '讲师', '30000']
# }

# for i in names.keys():
#     print(i, end="     ")

# for i in names.values():
#     i[0] = 80

# for i in names.items():
#     print(i, type(i))

# res = list(names.keys())
# print(res)

# 删除
# dict
# names = {
#     'miller': [23, 'CEO', 66666],
#     'blackgirl': [24, '行政', 40000],
#     'liuser': [25, '讲师', '30000']
# }

# clear  pop  popitem  del
# res = names.pop("miller")
# print(res)

# res = names.popitem()
# print(res)

# del names["miller"]
# print(names)
# print(names)
# names.clear()
# print(names)

# res = bytes(123456789)
# print(len(res))






