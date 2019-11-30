# with open("test111111111", "rb") as fp:
#     offs = -10
#     while True:
#         fp.seek(offs, 2)
#         li = []
#         for line in fp:
#             li.append(line)
#             print(li)
#         if len(li) > 1:
#             print(li[-1].decode("GBK"))
#             break
#         else:
#             offs *= 2

# for line in fp.readlines():  # 不断调用
# #     print(line.decode("GBK"), end="")

# fp = open("test111111111", "rb")
# fp.close()
# print(fp.closed)
with open("test111111111", "rb") as fp:
    offs = -10
    while True:
        li = []
        fp.seek(offs,2)
        for line in fp:
            li.append(line)
        if len(li) > 1:
            print(li[-1].decode("utf-8"))
            break
        else:
            offs *= 2

print(fp.closed)

