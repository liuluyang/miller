# name = "miller"
# res = input()
#
# res == "miller"

# li = list()
# print(li)


# 列表
# li = [1, 2, 4, 5, 6, 7]
# print(li)

# 添加的方法：
# li.insert(1, "a")  # 两个参数： 1.要插入的位置   2. 要插入的值
# li.append("b")  # 追加到 列表的最后

# 修改的方法：
# li[5] = "c"
# print(li)
#
# # 删除
# del li[6]  # 根据索引删除
# print(li)

# li = [1, 'a', 2, 4, 2, 5, 'c', 'b']
# li.remove(2)  # 根据值删除
# print(li)


# [1, 'a', 4, 2, 5, 'c', 'b']
# [1, 'a', 4, 2, 5, 'c', 'b']


'''相互转换'''

# 将数字 转换成字符串
# num = 111111.2346
# print(type(num))
#
# num = str(num)
# print(type(num))


# 将字符串转换成数字
# num = "111111.2346"
# print(type(num))
#
# num = float(num)
# print(type(num))
#
# num = int(num)
# print(type(num))


''''''

# s = "hello"
#
# res = list(s)
# print(res)
#
#
# ret = "".join(res)
# print(ret)


# if  else    elif

# name = "miller"
# pwd = "123"
#
# username = input("请输入账号：")
# password = input("请输入密码：")
#
# if username is "" or password is "":
#     print("不能为空")
#
# if username == name and password == pwd:
#     print("欢迎登陆")
# else:
#     print("账户名密码不对")


# n = 0
# sum_num = 0
#
# while n < 100:
#     if n == 50:
#         break
#     n += 1
#     sum_num += n
#
# print(sum_num)


# score = 75
#
# if score >= 90 and score == 100:
#     print('优秀')
# if score >= 80 and score == 85:
#     print('良好')
# if score >= 70:
#     print('普通')
# else:
#     print('很差')

# n = 0
# while n < 3:
#     n += 1
# else:
#     print("try enter three times.")


# a = 1
# b = a
# a = 2
#
# print(b)

# 15、我们要一个登陆程序。 该程序可以在用户输入错误的情况下提示用户 并且让用户重新输入。 但是错误的机会只有3次：

# name = "miller"
# pwd = "123"
#
# n = 0
# while n < 3:
#     username = input(">>>")
#     password = input(">>>")
#     if username == name and password == pwd:
#         print("welcome to beijing")
#         break
#     else:
#         print("username or password was wrong")
#     n += 1





