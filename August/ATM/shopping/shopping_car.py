# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 8:40

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# 1. 登录 3次 退出
# 2. 可以多次购物, # 一边卖一边结账， 买完在结账。
# 3. 充值


import json


def read_info(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())


def write_info(filename, user_info):
    with open(filename, "w") as f:
        return f.write(json.dumps(user_info))


def pay(shopping_car, user_info):
    total_price = sum([i["price"] for i in shopping_car])
    if total_price > user_info["balance"]:
        print("余额不足，请充值！")
    elif total_price <= user_info["balance"]:
        user_info["balance"] -= total_price
    print(user_info)
    write_info(file_path, user_info)


def authentication(user_info, username, password):
    if user_info["name"] == username and str(user_info["password"]) == password:
        return user_info
    else:
        return False


def shopping(userinfo):
    li = []
    for ind, val in enumerate(goods):
        li.append("    %d    %s   %s" % (ind, *val.values()))
    msg = "\n".join(li)
    shopping_car = []
    while True:
        print("商品信息".center(40, "-"),msg, "商品信息".center(40, "-"), sep="\n")
        choice = input("请选择商品(Q 退出, 自动结算)：").strip()
        if choice == "Q":
            pay(shopping_car, userinfo)
            exit("good bay")
        elif choice.isdigit() and int(choice) < len(goods):
            shopping_car.append(goods[int(choice)])
        else:
            print("么的这个商品")


def identification(file_path, user_info):
    n = 0
    while n < 3:
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        userinfo = authentication(user_info, username, password)
        if not userinfo:
            print("用户名或密码错误")
        else:
            shopping(userinfo)
        n += 1
    else:
        if user_info:
            user_info["status"] = 1
            write_info(file_path, user_info)


if __name__ == '__main__':
    file_path = r"D:\education_project\ATM\shopping\account.json"
    user_info = read_info(file_path)
    identification(file_path, user_info)


