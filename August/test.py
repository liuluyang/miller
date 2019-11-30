#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/13 15:50


# n = '{"username":"miller", "password":123456}'
# print(n, type(n))

# dic = eval(n)
# print(dic, type(dic))

# fp = open("./user_info", "rb")


# print(fp.name)
# print(fp.mode)
# fp.close()
# print(fp.closed)
# fp.seek(-50, 2)
# # print(fp.read())

# print(result, type(result))
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr

#
# msg = MIMEText("邮件内容", "plain", "utf-8")
#
# msg["From"] = formataddr(["miller", "591311452@qq.com"])
# msg["To"] = formataddr(["miller", "591311452@qq.com"])
# msg["Subject"] = "主题"

# server = smtplib.SMTP()

# import sys

# _, username, password = sys.argv
#################################################################################################

# 超过三次之后锁定账户，再次登录时打印："账户被锁定,请联系管理员!" 然后直接退出程序


# def read_user_info(filename):
#     with open(filename, "r", encoding="utf-8") as fp:
#         for line in fp:
#             account = eval(line)
#         return account
#
#
# def authentication(account_data):
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if account_data["status"] == 0:
#         if account_data["username"] == username and account_data["password"] == password:
#             print("Welcome")
#             return True
#         else:
#             print("Username or Password wrong")
#     else:
#         print("您的账户被锁定！ 请联系管理员解锁！")
#         return True
#
#
# def write_user_info(account_data, filename):
#     account_data["status"] = 1
#     with open(filename, "w", encoding="utf-8") as write_f:
#         write_f.write(str(account_data))
#
#
# if __name__ == '__main__':
#     account = read_user_info("./user_info")
#     for i in range(3):
#         res = authentication(account)
#         if res:
#             break
#     else:
#         print("超过三次了")
#         write_user_info(account, "./user_info")

def read_info():
    with open("./staff_list", "r") as fp:
        dic = {}
        li = fp.readline().strip().split(",")
        for line in fp:
            lis = line.strip().split(",")
            dic[lis[0]] = dict(zip(li, lis))
    return dic, li


def write_info(dic, li):
    new_li = []
    new_li.append(",".join(li))
    for i in dic.values():
        new_li.append(",".join(i.values()))

    with open("./staff_list", "w") as fp:
        for i in new_li:
            fp.write(i+"\n")


dic, li = read_info()

write_info(dic, li)

