#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/6


# 函数练习题1：
# 员工信息修改程序
# 在一个文件里存多个人的个人信息，如以下

# username,password,age,position,department,phone
# miller,abc123,30,Teacher,IT,13651830433
# liuser,df2@432,25,Teacher,Teching,18912334223
# black_girl,123456,23,class_master,perpare_lessons,13179879854

# 需求：
# 1.输入用户名密码，正确后登录系统 ，打印
# 1. 修改个人信息
# 2. 打印个人信息
# 3. 修改密码

# 2.每个选项写一个方法
# 3. 当用户选择1时，提示用户选择要修改的字段，根据用户输入对相应字段进行修改
# 4.登录时输错3次退出程序


import os


def read_info(filename):
    f = open(filename, "r", encoding="utf-8")
    first_raw_data = f.readline().strip().split(",")
    account = {}
    for line in f:
        item = line.strip().split(",")
        account[item[0]] = dict(zip(first_raw_data, item))
    f.close()
    return account, first_raw_data


def print_personal_info(account_dict, username):
    '''
    用户打印个人信息
    :param account_dict:   # 所有用户字典
    :param username:   # 当前用户名
    :return:
    '''
    msg = '''\t{:20}{}'''
    print("Information".center(50, "-"))
    for k, v in account_dict[username].items():
        # if k == "password":
        #     continue
        print(msg.format(k, v))
    print("Information".center(50, "-"))


def change_personal_info(account_dict, username):
    '''
    修改个人信息
    :param account_dict:   # 所有用户字典
    :param username:   # 当前用户名
    :return:
    '''
    count = 0
    for k, v in account_dict[username].items():
        if k == "password":
            count += 1
            continue
        print("{}: {:15}   {}".format(count, k, v))
        count += 1

    while True:
        print(account_dict[username])
        choice = input("select column id to change: ")
        if not choice.isdigit(): continue
        choice = int(choice)
        if 0 > choice or choice > len(account_dict[username]) - 1:
            continue
        else:
            key = first_row_data[choice]
            print("current value: ", account_dict[username][key])
        new_value = input("new value: ")
        if not new_value.isalnum():
            continue
        else:
            account_dict[username][key] = new_value
        break
    save_back_to_file(account)


def save_back_to_file(account_dict):
    '''
    将更改后的数据， 写会文件
    :param account_dict:
    :return:
    '''
    save_str = ",".join(first_row_data) + "\n"

    for i in account_dict.values():
        save_str += ",".join(list(i.values())) + "\n"

    with open(filename + ".data", "w", encoding="utf-8") as f_new:
        f_new.write(save_str)
    f_new.close()

    os.replace(filename + ".data", filename)


def edit_password(account_dict, username):
    while True:
        old_pwd = input("请输入原密码：")
        new_pwd = input("请输入新密码：")
        confirm_new_pwd = input("请再次输入新密码：")
        if account_dict[username]["password"] != old_pwd:
            print("原密码不正确,请重新输入.")
        else:
            if new_pwd == confirm_new_pwd:
                account_dict[username]["password"] = new_pwd
                break
            else:
                print("两次输入不一致,请重新输入")
    save_back_to_file(account)


if __name__ == '__main__':
    filename = "staff_data"
    account, first_row_data = read_info(filename)

    menu = '''
    1. 打印个人信息
    2. 修改个人信息
    3. 修改密码
    '''
    count = 0
    while count < 3:
        username = input("please enter your username:").strip()
        pwd = input("please enter your password:").strip()
        user_obj = account.get(username, None)
        if not user_obj:
            print("wrong username or password")
        else:
            if not user_obj["password"] == pwd:
                print("wrong username or password")
            else:
                while True:
                    print(menu)
                    option = {
                        "1": print_personal_info,
                        "2": change_personal_info,
                        "3": edit_password
                    }
                    choice = input("please choose: ").strip()
                    if choice.upper() == "Q":
                        exit("bey")
                    if not choice.isdigit(): continue
                    option[choice](account, username)
        count += 1





