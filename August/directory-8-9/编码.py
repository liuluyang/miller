# with open("./test.py.txt", "r", encoding="GBK") as fp:
#     content = fp.read()
#     print(content)
#     print(content.encode("GBK"))
#     print(content.encode("utf-8"))


# s1 = b"miller"
#
# s2 = "miller"
#
# print(s1)
# print(s2)


# s2 = "中国"
# print(s2.encode("utf-8"))
#
# b'miller'
# b'\xe4\xb8\xad\xe5\x9b\xbd'
# b开头的都代表是bytes类型，是以16进制来显示的，2个16进制代表一个字节。
# # utf-8是3个字节代表一个中文，所以以上正好是9个字节
