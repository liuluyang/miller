# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/29 9:39


import re


# ##################################################################
# with open("./three_pei", "r") as f:
#     for line in f:
#         print(line.split()[-1])

# with open("./three_pei", "r") as f:
#     print(re.findall("1[0-9]{10}", f.read()))
# ##################################################################
# s = 'a13744234523'
#
# print(re.search("^[0-9]{11}", s))


# ^ 表示从字符串 开头开始匹配， 如果过不符合，直接退出

# ##################################################################
# s = '13744234523'
# print(re.search("[0-9]{11}$", s))

# s = '13744234523'

# print(re.search("...........", s))


# s = '13744234523 '
#
# print(re.search(".+", s), end="")

#  .  匹配任意的除 \n 之外的字符

# ##################################################################
# s = "eaaaabbaaacc"
#
# print(re.search("eb*", s))

# * 匹配*号前的字符 0次 到 无限次

# ##################################################################
# s = "aaaaabbaaacc"
#
# print(re.search("ab+", s))

# * 匹配*号前的字符 1次 到 无限次

# ##################################################################

# s = "aaaaabbaaacc"
#
# print(re.search("a+?b+?", s))

#  ?  和 * + {n,m} 搭配的时候,  以非贪婪模式匹配


# s = "alex"
# print(re.search("b?", s))

# ?    和单独的字符搭配时 匹配前一个字符1次或0次

# ##################################################################
# s = "aaaaabbaaacc"
# #
# # print(re.search("a{2}", s))
# # print(re.search("a{5}", s))

#  匹配 {n} 之前的字符 n 次
# ##################################################################

# s = "aaaaabbaaacc"
# print(re.search("a{2,20}", s))
#  匹配 {n, m} 之前的字符 n次 到 m次。

# ##################################################################

# s = "aaaaabbaaacc"
# print(re.search("bb|aaa|ccc", s))

# | 或的意思。 匹配到一个就行
# ##################################################################
# s = "abcabca456c"
#
# res = re.search("(abc){2}a(456)c", s)
# print(res.groups())

# ()  分组匹配。 () 内的内容。会被提取出来

# ##################################################################
# s = "abca\\bca45-6c"

# print(re.search("\d+", s))

# print(re.search("[^A-Za-z0-9_-]+", s))
# print(re.search("[^A-Za-z0-9_-]+", s))

# []
# ##################################################################

# s = "abca\\bca45-6c"
# print(re.search(r"\\", s).group())

# res = re.search("\w+", s)
# print(res)

# string = "13138387438"
# res = re.search("(?P<name1>[0-9]{3})(?P<name2>[0-9]{4})(?P<name3>[0-9]{4})", string)
# print(res.groupdict()["name1"]+"****"+res.groupdict()["name3"])

#  (?P<name1>[0-9]{3})
# ?P<name> 分组匹配时， 为组 起个名字。

# #########################search#########################################

# re.search  从整个字符串里面找. 找到第一个匹配项。 就停止。

# s = "abcabcabc"
# print(re.search("abc", s))

# ###########################match#######################################
# re.match  从字符串起始位置开始查找, 如果能找到就继续向后匹配, 如果第一个都不匹配直接退出。
# s = "abcabcabc"
# print(re.match("abc", s))

# ##########################findall########################################
# s = "abcabc.abc"
#
# print(re.findall(r"\.", s))

# s = "abc.abc.abc"

# print(re.split("\.", s))

# ############################sub######################################
# s = "abc.abc.abc"
#
# print(re.sub("abc","123", s))

# #########################fullmatch#########################################

# s = "591311452@163.org"
#
# print(re.fullmatch("[A-Za-z0-9]+@(qq|163|sina)\.(com|cn|org)", s))


# strings = "HtTps://www.baidu.com"
#
# print(re.fullmatch("(H|h)(T|t)(T|t)(P|p)s?://www\.(\w+)\.(com|cn|org)", strings))


# ############################compile######################################

# pattern = re.compile("[A-Za-z0-9]+@(qq|163|sina)\.(com|cn|org)")
#
# s = "591311452@163.org"
#
# print(pattern.search(s))

# pattern = "[A-Za-z0-9]+@(qq|163|sina)\.(com|cn|org)"

# ##################################################################
# s = "591311452@163.org"
#
# print(re.search(pattern,s))
# print(re.search(pattern,s).group())
# print(re.search(pattern,s).groups())
# print(re.search(pattern,s).groupdict())
# print(re.search(pattern,s).start())
# print(re.search(pattern,s).end())
# print(re.search(pattern,s).span(2))

# m = re.search(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
# print(m.groups())
# print(r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1 \3'))

# 7.expand(template):
# 将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。

# s = "abC\nAbc\naBc\n"

# print(re.findall("^abc", s, re.M and re.I))

# s = "abC\nAbc\naBc\n"
#
# print(re.findall("abc", s, re.I))

# s = "abC\nAbc\naBc\n"

# print(re.findall(".+", s, re.S))

# s = "sadass1223dasd"

# print(re.search("(?![0-9]+$)(?![A-Za-z]+$)([A-Za-z0-9]{8,16})", s))


def add_subtraction(one_equation):
    # print("加减",one_equation)
    if len(one_equation.split("+")) > 1:
        x, y = one_equation.split("+")
        return float(x) + float(y)
    elif len(one_equation.split("-")) > 1:  # 有符号的这里需要特别的处理一下！
        x, y = one_equation.rsplit("-", 1)
        return float(x) - float(y)


def multi_division(one_equation):
    # print("乘除",one_equation)
    if len(one_equation.split("*")) > 1:
        x, y = one_equation.split("*")
        return float(x) * float(y)
    elif len(one_equation.split("/")) > 1:
        x, y = one_equation.split("/")
        return float(x) / float(y)


def before_after(inner_equation, res, val):
    inner_equation = unity(inner_equation.replace(res, str(val), 1))
    return inner_equation


def xxx(inner_equation):
    while True:
        res = regex_multi_division.search(inner_equation)
        print(res)
        if res:
            val = multi_division(res.group())
            # inner_equation = before_after(inner_equation, res.group(), val)
            inner_equation = unity(before_after(inner_equation, res.group(), val))
            print("乘除....", inner_equation)
        else:
            break
    while True:
        res = regex_add_subtraction.search(inner_equation)
        print(res)
        if res:
            val = add_subtraction(res.group())
            inner_equation = unity(before_after(inner_equation, res.group(), val))
            print("加减....", inner_equation)
        else:
            break
    return inner_equation


def unity(sub_s):
    if sub_s.__contains__("+-") or sub_s.__contains__("++") or sub_s.__contains__("-+") or sub_s.__contains__("--"):
        sub_s = sub_s.replace("+-", "-").replace("++", "+").replace("-+", "-").replace("--", "+")
    return sub_s


import time


def timer(func):
    start = time.time()

    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(time.time() - start)
        return ret

    return inner


@timer
def search_inner(s):
    while True:
        res = regex_inner_equation.search(s)
        if res:
            val = xxx(res.group())
            s = before_after(s, res.group(), val.strip("()"))
        else:
            return xxx(s)


regex_inner_equation = re.compile("\([^()]+?\)")
regex_multi_division = re.compile("\d+\.?\d*[*/]\d+\.?\d*")
regex_add_subtraction = re.compile("\d+\.?\d*[+\-]\d+\.?\d*")

# 使用re模块  将下面这个字符串计算出来
s = "1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998-10*568/14))-(-4*3)/(16-3*2))"

# print(eval(s))
# print(search_inner(s))

# A = [0, 1, 2, 3]
#
# B = [1, 2, 1, 0]

# lst = [['老王', '开车'], ['去', '上班!']]
#
# print("".join(lst[i][j] for i in range(len(lst)) for j in range(len(lst[i]))).replace("班", ""))

dic = {}


def register(num):
    def inner(func):
        dic[num] = func
        return func
    return inner


@register("1")
def xx():
    return 123


@register("2")
def xxx():
    return 123456


print(dic["2"]())
