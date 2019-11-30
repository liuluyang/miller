# evn/python
# _*_ utf-8 _*_
# author: "miller"
# s55103510

import copy

# data = {
#     "name": "alex",
#     "age": 18,
#     "scores": {
#         "语文": 130,
#         "数学": 60,
#         "英语": 98,
#     }
# }
#
# data2 = data
#
# data2["name"] = "miller"
#
# print(data)  # 会被改变，因为 data2 和 data 共享同一个字典对象


# ############### copy ####################
# data = {
#     "name": "alex",
#     "age": 18,
#     "scores": {
#         "语文": 130,
#         "数学": 60,
#         "英语": 98,
#     }
# }

# data2 = data.copy()  # copy(data)

# print(data2, id(data2))
# print(data, id(data))

# data2["name"] = "miller"

# print(data2)
# print(data)


# #######################################
# data = {
#     "name": "alex",
#     "age": 18,
#     "scores": {
#         "语文": 130,
#         "数学": 60,
#         "英语": 98,
#         "xx":{
#             "ddd":123
#         }
#     }
# }

# data2 = copy.copy(data)
# print(data2)

# data2["scores"]["语文"] = 0

# data2["name"] = "miller"

# print("data2", data2, id(data2))
# print("data",data, id(data))
#
# print(id(data2["name"]))
# print(id(data["name"]))
#
# print(id(data2["age"]))
# print(id(data["age"]))
#
# print(id(data2["scores"]))
# print(id(data["scores"]))

# ###################### deepcopy ####################################

# data = {
#     "name": "alex",
#     "age": 18,
#     "scores": {
#         "语文": 130,
#         "数学": 60,
#         "英语": 98,
#         "xx":{
#             "ddd":123
#         }
#     }
# }

# data2 = copy.deepcopy(data)
# print("data2", data2, id(data2))
# print("data", data, id(data))

# data2["scores"]["xx"]["ddd"] = 5555

# print(data2)
# print(data)


# print(bin(61352))  # 1110111110101000
# # print(2 ** 15 + 2 ** 14 + 2 ** 13 + 2 ** 11 + 2 ** 10 + 2 ** 9 + 2 ** 8 + 2 ** 7 + 2 ** 5 + 2 ** 3)

# 128 64  32  16  8  4  2  1     # 十进制zip
# 0   1   0   1   0  1  1  1     # 二进制


# ################################ 十六进制 ###############################

# 0 1 2 3 4 5 6 7 8 9  A  B  C  D  E  F
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# print(hex(61352))  # 0x  efa8  # 61352

# print(14 * 16 ** 3 + 15 * 16 ** 2 + 10 * 16 ** 1 + 8 * 16 ** 0)

# print(oct(61352))



# print(ord("1"))
# print(chr(36))

# print( "a" > "b")
import random

#  65 - 90   97 - 122  48 - 57

# random.randrange(65, 90)
# random.randrange(97, 122)
# random.randrange(48, 57)

# li = list(range(65, 91))
# li.extend(range(97, 123))
# li.extend(range(48, 58))

# s = ""
# for i in range(6):
#     s += chr(random.choice(li))
# print(s)

# print(int("11111011", 2))

# print("码客".encode("GBK"))

# c2eb   bfcd




