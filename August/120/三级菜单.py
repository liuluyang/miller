# menu = {
#     "北京": {
#         "朝阳": {
#             "夜总会": {
#                 "小姐姐家": {},
#                 "老鸨家": {},
#             },
#             "地铁站": {
#                 "驾驶室": {},
#                 "月台": {}
#             },
#             "天安门": {
#                 "毛主席": {},
#                 "五星红旗": {}
#             }
#         },
#         "海淀": {
#             "北京大学": {
#                 "大长腿": {}
#             },
#             "清华大学": {
#                 "大屁股": {}
#             },
#             "颐和园": {
#                 "大胸脯": {}
#             }
#         },
#         "昌平": {
#             "网吧": {
#                 "": {}
#             },
#             "太行山": {
#                 "": {}
#             },
#             "水库": {
#                 "": {}
#             }
#         }
#     },
#
#     "上海": {
#         "黄浦江": {
#             "黄埔军校": {},
#             "滨江大道": {},
#             "杨浦大桥": {}
#         },
#         "陆家嘴": {
#             "金茂大厦": {},
#             "正大广场": {},
#             "环球金融中心": {},
#         },
#         "浦东": {
#             "东方明珠": {},
#             "科技馆": {},
#             "嘉定": {}
#         }
#     },
#
#     "石家庄": {
#         "藁城": {
#             "码客": {},
#             "市政府": {},
#             "妇联": {}
#         },
#         "桥西": {
#             "振头": {},
#             "图书馆": {},
#             "失恋博物馆": {}
#         },
#         "新华": {
#             "新华书店": {},
#             "人民广场": {},
#             "北国商城": {}
#         }
#     },
# }


# 1. 可以循环输出。
# 2. 接受用户输入，打印 用户输入城市的下级城市。

# 升级需求：
# 3. q 可以退回上一级
# 4. Q 推到最后。
# 5. 退到最后之后，用户再退，要有提示 已经退回到最顶级
# 6. 代码不超过20行

# li = []
# last_menu = menu.copy()
# while True:
#     for i in last_menu:
#         print(i)
#     choice = input("请输入城市名：").strip()
#     if not choice: continue
#     if choice in last_menu:
#         li.append(last_menu)
#         last_menu = last_menu[choice]
#     else:
#         if li and choice == "q":
#             last_menu = li.pop()
#         if li and choice == "Q":
#             last_menu = menu
#             li.clear()
#         else:
#             print("已经是最顶层了")


# def match_count(s):
#     s = str(s)
#     digitarray = s.lstrip("0")
#     length = len(digitarray)
#     if length == 0:
#         return 0
#     li = [0 for _ in range(length + 1)]
#     li[0] = 1
#     for i in range(1, length + 1):  # 1 6
#         if digitarray[i - 1] == "0":
#             li[i] = 1
#         else:
#             li[i] = li[i - 1]
#         if i > 1 and (int(s[i - 2]) == 1) or (int(s[i - 2]) == 2 and int(s[i - 1]) <= 6):
#             li[i] += li[i - 2]
#         print(li)
#     print(li[length])


# match_count(15217)

# 1. 当字符串

# import string, random
# #
# # li = list(string.ascii_uppercase + string.digits)
# # all_num = ["".join(random.choices(li, k=6)) for i in range(10)]
# # for cat_num in all_num:
# #     for i in range(len(cat_num)-len(cat_num)*2, 0):
# #         if cat_num[i] == "8":
# #             print("限号", cat_num)
# #             break

import random
import string
params = string.ascii_uppercase + string.digits
cards = set()
num = [1, 8]
while len(cards) < 10:
    card = []
    for i in range(5):
        card.append(random.choice(params))
    card = "".join(card)
    if card.isdigit() or card.isalpha():
        continue
    else:
        cards.add(card)

for card in cards:
    for c in range(len(card)-1, -1, -1):
        if card[c].isdigit() and int(card[c]) in num:
            print(card, card[c])
            break
        elif card[c].isdigit():break






