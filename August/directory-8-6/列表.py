# li = [45, 66, 87, 23, 1, 2, 4, 5]
# li.sort()  # 原地排序
# print(li)


# li = ['miller', '王长贵', '@', '1', '4', '#', '黑姑娘']
# li.sort()
# print(li)

# li1 = ['#', '1', '4', '@', 'miller', '王长贵', '黑姑娘']
# li1.reverse()
# print(li1)  # ['黑姑娘', '王长贵', 'miller', '@', '4', '1', '#']


# ⑾练习：
# names=["miller", "黑姑娘", "rain", "eva", "狗蛋", "银角大王", "eva", "鸡头", "liuser"]  # 进入以下操作

# 通过names.index()的方法返回第2个eva的索引值
# res = names.index("eva")
# print(res)
# res = names.index("eva", names.index("eva")+1)
# print(res)

# 把以上的列表通过切片的形式实现反转
# names = ["miller", "黑姑娘", "rain", "eva", "狗蛋", "银角大王", "eva", "鸡头", "liuser"]
# #       ['liuser', '鸡头', 'eva', '银角大王', '狗蛋', 'eva', 'rain', '黑姑娘', 'miller']
# print(names[::-1])


# 打印列表中所有下标为奇数的值
# print(len(names))
# for i in range(len(names)):
#     if i % 2 != 0:
#         print(names[i])

# 通过names.index()方法找到第2个eva值 ，并将其改成EVA
# print(names)
# names[names.index("eva", names.index("eva")+1)] = "EVA"
# print(names)

# name = ['miller', 'liuser', 'rain', 'olddriver']
# name.insert(3, "black_girl")
# print(name)

# li1 = ['玉田','王长贵','小萌']

# name.extend(li1)
# print(name)

# li = [1, 2, [3, 4, [5, 6, [7, 8]]]]


# name = ['miller', 'liuser', 'rain', 'olddriver']

# res = name.pop(2)
# print(res)
# print(name)


# name.remove(name[0])
# print(name)

# print(id(name))
# name.clear()
# print(name, id(name))


# name = ['miller', 'liuser', 'rain', 'olddriver', '玉田', '王长贵', '小萌']

# res = name[1::2]
# print(res)
# print(name)


# res = name[-6::]
# print(res)
# print(name)
