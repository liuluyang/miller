#
# f = open("./兼职空姐白领学生模特护士联系方式.txt", "r", encoding="utf-8")
# print(f.read())


# f = open("./兼职空姐白领学生模特护士联系方式.txt", "a", encoding="utf-8")
# f.write("\nxxxxxxxxxxxxxxxxxx")
# f.close()

# 循环文件
# import time

# f = open("./兼职空姐白领学生模特护士联系方式.txt", "r", encoding="utf-8")
# for line in f:
#     print(line, end="")
#     time.sleep(1)
# f.close()





# f = open(r"E:\project\education\10-18\兼职空姐白领学生模特护士联系方式GBK.txt", "w", encoding="GBK")
#
# f.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#
# f.flush()
#
# f.close()


# f = open("./test.txt", "w", encoding="GBK")
# f.write("码客教育")
# f.close()

# f = open("./test.txt", "r", encoding="GBK")
# f.seek(4, 0)  #
# print(f.read())
# f.close()

# f = open("./test.txt", "rb")
# # f.seek(4, 1)
# f.seek(-4, 2)
# print(f.tell())
# print(f.read().decode("GBK"))
#
# f.close()


# f = open(r"E:\project\education\10-18\兼职空姐白领学生模特护士联系方式GBK.txt", "r+", encoding="utf-8")
# f.write("hello")
# f.seek(40)
# f.write("hello")
# f.close()

# f = open(r".\兼职空姐白领学生模特护士联系方式GBK.txt", "r", encoding="utf-8")
#
# w_f = open(r".\xxxxx.txt", "w", encoding="utf-8")
#
# for line in f:
#     li = line.split()
#     if li[0] == "黑姑娘":
#         li[3] = "52"
#         line = "   ".join(li)
#     w_f.write(line)
#     w_f.flush()
#

# import sys

# _, old_str, new_str, filename = sys.argv
# f = open(filename, "r", encoding="utf-8")


f = open("./user_info", "r")
print(eval("['username', 123456]"))






