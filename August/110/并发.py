# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/3 15:32


# 64 32 16 8 4 2 1
# 1  1  0  1 1 0 1

# print(int("1101101", 2))
# print(64+32+8+4+1)
# print(1*2**6+1*2**5+1*2**3+1*2**2+1*2**0)


# C56AF

# print(10*16**1+15*16**0)

# print(divmod(1314, 16))
# print(divmod(82, 16))


# print(hex(100))  # 0x64
# print(oct(100))  # 0o144
# print(bin(100))  # 0b1100100

import sys

# print(sys.getfilesystemencoding())
# print(sys.getdefaultencoding())

# age = b"123"
# print(type(age))


# nation = "中国"
#
# res = nation.encode("utf-8")
# print(res)
# # print(res.decode("utf-8"))


# string1 = "我爱你"



import os,sys

# print(os.linesep.encode())

# print(os.stat(r"F:\Teacher\share\video\8月\8-6字符串方法.wmv"))
# print(os.stat(r"F:\Teacher\share\video\8月\8-6字符串方法.wmv").st_size)

# with open(r"F:\Teacher\share\video\8月\8-6字符串方法.wmv", "rb") as f:
    # res = f.read()
    # import time
    # while True:
    #     print(hash(res))
    #     time.sleep(0.5)

    # f.seek(10, 0)  # 移动光标的   0文件开头  1当前位置  2文件末尾
    # f.seek(5000000000, 1)  # 移动光标的   0文件开头  1当前位置  2文件末尾
    # print(f.tell())  # 告知光标在哪里的












