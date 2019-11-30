# 1.找到文件，双击打开
# 2.读或者修改
# 3.保存&关闭

# read  r
# write w
# append a

# D:\education_project\directory-8-12\staff.txt
# ###################### r 只读模式#####################
# fp = open("staff.txt", "r", encoding="utf-8")
# result = fp.read()
# print(result)
# fp.close()

# ###################### w 只写模式 #####################
# w 模式会先去查看有没有这个文件，如果有直接打开但是会清空原有的所有数据
# 如果没有则会创建一个 同名的文件。

# fp = open(r"D:\education_project\directory-8-2\test.py.txt", "w", encoding="GBK")
# fp.write("我是野生程序员")
# fp.close()

# fp = open(r"D:\education_project\directory-8-12\test111111111", "w", encoding="GBK")
# fp.write("我是野生程序员1\n")
# fp.write("我是野生程序员2\n")
# fp.close()

# fp = open(r"D:\education_project\directory-8-12\test111111111", "a", encoding="GBK")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.write("我是野生程序员3")
# fp.write("我是野生程序员4")
# fp.close()


# fp = open(r"D:\education_project\directory-8-12\test111111111", "r", encoding="GBK")
# res = fp.readline()
# print(res)
# res = fp.readline()
# print(res)
# print("分隔符".center(30, "-"))
# res = fp.read()
# print(res)
# fp.close()

# fp = open("兼职空姐白领学生模特护士联系方式.txt", "r", encoding="utf-8")
# res = fp.read()
# print(res, type(res))
# fp.close()

# ####################### a 追加模式 #######################
# 向文件中追加写入内容
# fp = open("兼职空姐白领学生模特护士联系方式.txt", "a", encoding="utf-8")
# fp.write("sexy_girl    北京   175   55    17145235841\n")
# fp.close()


# fp = open("兼职空姐白领学生模特护士联系方式.txt", "r", encoding="utf-8")
# for line in fp:
#     print(line)
#     break
# info = line.split()
# name, city, height, weight, phone = info
#
# height = int(height)
# weight = int(weight)
#
# if height > 170 and weight < 50:
#     print(line)
# fp.close()

# ################################# file对象的其他方法####################################
# fp = open(r"D:\education_project\directory-8-12\test.py.txt", "r", encoding="GBK")

# print(fp.mode)  # 返回文件的打开模式
# print(fp.name)  # 返回文件名
# print(fp.closed)  # 返回 bool

# print(fp.fileno())  # 返回文件句柄在内存中的索引值

# for line in fp.readlines():  # readlines 不断调用readline 并将内容以列表的形式返回
#     print(line, end="")


# fp.close()

######################################################################################
# flush 将写入内存中的数据， 强行刷新到硬盘中
# fp = open(r"test111111111", "a", encoding="GBK")
# fp.write("我是野生程序员7\n")
# fp.flush()
# while True:
#     print(1)

# ###################### seek 以字节为单位移动 光标的位置。 ##############################
# 正数为 从左向右 移动
# 负数为 从右向左 移动
# 有三种模式：
# 默认为 0 表示从文件的初始开始移动
#  1  表示 从光标当前位置开始移动
#  2  表示 从文件的末尾开始移动

# fp = open("seek_lean", "w", encoding="utf-8")
# fp.write("码客教育")
# fp.close()

# fp = open("seek_lean", "r")
# fp.seek(6)
# # print(fp.read().decode("utf-8"))

# # fp.seek(-3, 2)
# # print(fp.read().decode("utf-8"))
# print(fp.tell())

# fp.close()


# tell()   # 返回的是光标在文件中的当前位置

# ##################### w+ 模式 ##################
# fp = open("test111111111", "w+", encoding="utf-8")
# fp.write("码客教育拉拉裤靠的就是鼓")
# fp.seek(0)
# print(fp.read())
# fp.close()

# ##################### r+ 模式 ##################
# fp = open("test111111111", "r+", encoding="utf-8")
# print(fp.read())
# fp.write("\n123456789\n")
# fp.close()

# fp = open("test111111111", "r+", encoding="utf-8")
# print(fp.readline())   # r+ 模式写入时 默认从文件的最后写入内容！
# fp.seek(30)  # 如果是seek移动的光标位置， 就从光标位置开始写入。
# fp.write("kashdfhasf\n")
# fp.close()

# ##################### a+ 模式 ##################
# fp = open("test111111111", "a+", encoding="utf-8")
# fp.write("my name is miller")
# fp.seek(0)
# print(fp.read())
# fp.close()


# ###################### truncate ######################################
# with open("truncate_lean.txt", "r+", encoding="utf-8") as fp:
#     print(fp.readline(), end="")
#     fp.truncate(6)  # 计算字节
#     print(fp.readline(), end="")

#  truncate 这个方法要使用 混合可读写的模式打开文件。
#  他会将size 这个参数之后的内容全部删除掉。只剩下size之前包括size 的内容。

# size 参数

# ######################## 如何更改文件中一行中的某一段的内容 ##################
# with open("兼职空姐白领学生模特护士联系方式.txt", "r", encoding="utf-8") as fp:
#     fp.write("hello")
#     fp.seek(45)
#     fp.write("world")
#     fp.close()
#
#     print(fp.readline())
#     fp.seek(-45, 2)
#     print(fp.readline())
#     fp.close()
#
#     print(fp.readline(100))  # 默认读一行，指定Limit 读取多少个字符。 超出 \r\n 的忽略
#     print(fp.readlines(70)) # hint可以被指定来控制行数:如果所有行的总大小(在字节/字符)中超过了hint,那么就不会读取更多的行。


# f_name = "兼职空姐白领学生模特护士联系方式.txt"
# f_new_name = "%s.new" % f_name
# old_str = "刘诺涵"
# new_str = "[黑姑娘]"
# f = open(f_name, 'r', encoding='utf-8')
# f_new = open(f_new_name, 'w', encoding="utf-8")
# for line in f:
#     if old_str in line:
#         new_line = line.replace(old_str, new_str)
#     else:
#         new_line = line
#     f_new.write(new_line)
# f.close()
# f_new.close()

# import os
# os.replace(f_new_name, f_name)  # 将新文件名 替换成 旧文件。

# ###################### rb 模式 #####################
# img_f = open("D:\education_project\directory-8-12\交集.png", "rb")
# res = img_f.read()


# ######################## wb #######################
# img_f = open("D:\education_project\directory-8-12\交集111.png", "wb")
# img_f.write(res)


# r  rb  seek
