# staff_list = [
#     ["miller", 18, "CEO", '88888'],
#     ["black_girl", 24, "行政", '55555'],
#     ["liuser", 17, "董事长", "500"],
#     ["chenser", 30, "组长", "2"]
# ]

# for i in staff_list:
#     if i[0] == "black_girl":
#         print(i)
#         break


# staff_list = [
#     ["miller", 18, "CEO", '88888'],
#     ["black_girl", 24, "行政", '55555'],
#     ["liuser", 17, "董事长", "500"],
#     ["chenser", 30, "组长", "2"]
# ]

# staff_dict = {
#     "miller": [18, "CEO", '88888'],
#     "black_girl": [24, "行政", '55555'],
#     "liuser": [17, "董事长", "500"],
#     "chenser": [30, "组长", "2"]
# }

# res = staff_dict["miller"]
# print(res)

# ##################### 查询 ########################
# staff_dict = {
#     "miller": {"age": 18, "position": "CEO", "salary": 80000},
#     "black_girl": {"age": 25, "position": "行政", "salary": 80000},
#     "liuser": [17, "董事长", "500"],
#     "chenser": [30, "组长", "2"]
# }

# res = staff_dict["miller"]["salary"]
# print(res)

# ss = staff_dict.get("123456")
# print(ss)

# ######################  ###########################

# staff_dict = {
#     "miller": {"age": 18, "position": "CEO", "salary": 80000},
#     "black_girl": {"age": 25, "position": "行政", "salary": 30000},
#     "liuser": {"age": 10, "position": "董事长", "salary": 10000},
#     "chenser": {"age": 50, "position": "组长", "salary": 20000}
# }

# staff_dict["black_girl"]["age"] = 26
# print(staff_dict)

# 请把这个dict中key大于5的值value打印出来。

# dic = {i: i for i in range(20)}
# for i in dic:
#     if i > 5:
#         print(dic[i])

# for i in dic:
#     if dic[i] % 2 == 0:
#         dic[i] = -1
#
# print(dic)




