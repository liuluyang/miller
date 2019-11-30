# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/7 8:47


def read_info(filename):
    with open(filename, "r", encoding="utf-8") as f:
        li = f.readline().strip("\n").split(",")
        dic = {}
        for line in f:
            n = line.strip("\n").split(",")
            dic.setdefault(n[0], {}).update(dict(zip(li, n)))
        return dic, li


# 1. 修改个人信息

def change_personal_info(all_user_info, username):
    user_obj = all_user_info.get(username)
    li = []
    for ind, val in enumerate(user_obj.items()):
        if ind != 1:
            li.append("      %s: %s " % (ind, val[0]))
    msg = "\n".join(li)
    while True:
        print(msg)
        choice = input(">>>(Q 退出):").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice != 1 and choice <= len(title_list):
                print("你要修改的字段当前值为 %s" % all_user_info[username][title_list[choice]])
                info = input("请输入要修改成啥：")
                all_user_info[username][title_list[choice]] = info
        if choice == "Q":
            break


if __name__ == '__main__':
    all_user_info, title_list = read_info("./staff_list")
    n = 0
    while n < 3:
        username = input("please enter your username:")
        pwd = input("please enter your password:")
        user_obj = all_user_info.get(username)
        if not user_obj or user_obj["password"] != pwd:
            print("go out")
        else:
            menu = '''
            1. 修改个人信息
            2. 打印个人信息
            3. 修改密码
            '''
            change_personal_info(all_user_info, username)
            print(all_user_info)
            break
        n += 1






