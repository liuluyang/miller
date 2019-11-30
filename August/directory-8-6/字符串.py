# s = "hello miller, how are you"

# print(s)
# print(s[5:7])
# ss = r"ss\n\tss"
# print(ss)

# ############# replace ###########
# replace(self, old,new,count=None):

# s = "aaaaa accccaaaaa"
# res = s.replace("a", "b")
# print(res)
#
# res = s.replace("aa", "b", 3)
# print(res)
#
# num = "1 2 3 4 6 7 "
# number = num.replace(" ", "")
# print(number)

# ################## split 分割 ############## ######### rsplit #############
# split(sep, maxsplit)   # 以sep 作为分隔符， 得到的结果为一个列表， 但是 不包括 sep
# maxsplit 最大分割次数
# s = "Hello, World"
# li = s.split("l",1 )
# print(li)
# print(len(li))

# ######### center ##########
# center(self, width, fillchar=None)

# s = "hello World"
# res = s.center(20, "+")
# print(res)

# ############ count #############
# count(self, sub, start=None, end=None)
#
# s = "aaaa"
# num = s.count("a")
# print(num)

# ########### find 从左往右 ###############   ####### rfind 从右往左 ##############
# find(self, sub, start=None, end=None):

# s = 'Hello Wolrd!'
# print(s.index("W"))  # 会报错
# print(s.find("l"))

# ########## format #############
#
# s = 'my name is {},i am {} years old'
#
# cen = s.format("alex","23")
#
# print(s)
# print(cen)


# s = 'my name is {0},i am {1} years old'
#
# cen = s.format("miller", 23)
# print(cen)


# s = 'my name is {name},i am {age} years old'
# #
# cen = s.format(age="23", name="miller")
# print(cen)

# s = 'my name is {name},i am {age} years old'
# cen = s.format_map({"name": "miller", "age": "23"})
# print(cen)

########## join ################

# li = [str(_) for _ in range(20)]
#
# print(li)
# print(str(li), type(str(li)))
#
# str111 = ""
# for i in li:
#     str111 = str111 + str(i)
# print(str111)
#
# res = "|".join(li)
#
# print(res)


# ############# strip ##############
# s = "  \nHello World\n    "
#
# cen = s.strip()
# print(cen)

# lstrip(self, *args, **kwargs): # real signature unknown
# 去掉字符串左边的 空格 和 换行 table键！都会去掉
# rstrip(self, *args, **kwargs): # real signature unknown
# 去掉字符串右边的 空格 和 换行 table键！都会去掉

# ########## swapcase 大小写转换 ###########
# s = "Hello World"
# res = s.swapcase()
# print(res)  # hELLO wORLD


# ###### capitalize 首字母大写 ##########

# name = "miller liuser"
# res = name.capitalize()
# print(res)  # Miller liuser

# ######### caseflod #######

# s = "ABCDEFG"  # abcdefg
#
# res = s.casefold()
# print(res)


# ############  endswith #######

# endswith(self, suffix, start=None, end=None):

# name = "miller qi"
#
# res = name.endswith("i", 0, 2)
# print(res)


# ############## startswith ###############
# startswith(self, prefix, start=None, end=None):
# name = "miller qi"
# res = name.startswith("i")
# print(res)

# ############ expandtabs ###################
# s = "hello\tWorld"
# print(s)
# res = s.expandtabs(10)
# print(res)


# ########### index 从左往右 ##################  ###### rindex 从右往左 ##############
# index(self, sub, start=None, end=None):
# s = "miller"
# res = s.index("a")
# print(res)
# resl = s.find("a")
# print(resl)  # -1

# ################ isalnum ################

# s = '0123456789qwertyuiopasdfghjklzxcvbnm'
# res = s.isalnum()
# print(res)
#
# s = '0123456789qwertyuiopasdfghjklzxcvbnm中'
# res = s.isalnum()
# print(res)

# ############### isalpha ###############

# s = 'qwertyuiopasdfghjklzxcvbn中m'
#
# res = s.isalpha()
# print(res)

# ############## isdecimal 只能是整数###########

# s = '1234569871'
# res = s.isdecimal()
# print(res)

# ############## isnumeric #############

# s = '②①0123456987二三壹贰，'
# res = s.isnumeric()
# print(res)

# ############### isidentifier ###############

# s = "kasgdfkjga_s"
#
# res = s.isidentifier()
# print(res)

# ############# islower 判断小写 ######################

# s = "13468asdoiSdf_"
# res = s.islower()
# print(res)

# ############## lower 将字符转换成小写的 ######################
# s = "13468ASCDSdf_"
# res = s.lower()
# print(res)  # 13468ascdsdf_

# ############# isupper 判断大写###################

# s = "132__AVDc"
# res = s.isupper()
# print(res)

# ################### upper 将字符转换成大写的 #####################
# s = "65435__ ashdfkasdf"
# res = s.upper()
# print(res)  # 65435__ ASHDFKASDF

# ################### isprintable ###################

# s = "sss\tsss"
# res = s.isprintable()
# print(res)

# ################## isspace ####################

# s = "        "
# res = s.isspace()
# print(res)

# ################### istitle #################
# s = " title False"
# res = s.istitle()
# print(res)


# ################  ljust ####################
# ljust(self, width, fillchar=None): # real signature unknown
# s = 'hello world!'
# n = s.ljust(50,'*')
# print(n)  #hello world!**************************************
# # 把字符串以左对齐方式 填充到指定长度。可以选择填充符
# n = s.rjust(50,'*')
# print(n)
# n = s.center(50,'*')
# print(n)


# ############## partition ###########

# s = 'hello 1 world!'
#
# res = s.partition("l")
#
# print(res)

# ################ rpartition ###############


# ################ splitlines 按换行符 分割字符， 返回列表 ##############
# s = 'hello\nworld!\nmy name is qichen\n123'
# res = s.splitlines()
# print(res)

# ################ title 所有首字母大写 #############
# s = "miller liuser alex"
# res = s.title()
# print(res)


# maketrans(self, *args, **kwargs): # real signature unknown
# intab  = 'abcdef'
# outtab = '123456'   #必须一一对应）

# n = str.maketrans(intab,outtab)  #以aciss表，建立对应关系
# print(n)  #{97: 49, 98: 50, 99: 51, 100: 52, 101: 53, 102: 54}


# translate(self, *args, **kwargs): # real signature unknown
# 将字符串以maketrans 创建的映射表，做参数。将字符串 s 中的对应字符转换一下。
# s = 'hello world!'
# l = s.translate(n)
# print(l)  # h5llo worl4!

# ########### zfill ################

# s = "aaaa"
# res = s.zfill(8)
# print(res)




