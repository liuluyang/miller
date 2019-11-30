menu = {
    "北京": {
        "朝阳": {
            "夜总会": {
                "小姐姐家": {},
                "老鸨家": {},
            },
            "地铁站": {
                "驾驶室": {},
                "月台": {}
            },
            "天安门": {
                "毛主席": {},
                "五星红旗": {}
            }
        },
        "海淀": {
            "北京大学": {
                "大长腿": {}
            },
            "清华大学": {
                "大屁股": {}
            },
            "颐和园": {
                "大胸脯": {}
            }
        },
        "昌平": {
            "网吧": {
                "": {}
            },
            "太行山": {
                "": {}
            },
            "水库": {
                "": {}
            }
        }
    },

    "上海": {
        "黄浦江": {
            "黄埔军校": {},
            "滨江大道": {},
            "杨浦大桥": {}
        },
        "陆家嘴": {
            "金茂大厦": {},
            "正大广场": {},
            "环球金融中心": {},
        },
        "浦东": {
            "东方明珠": {},
            "科技馆": {},
            "嘉定": {}
        }
    },

    "石家庄": {
        "藁城": {
            "码客": {},
            "市政府": {},
            "妇联": {}
        },
        "桥西": {
            "振头": {},
            "图书馆": {},
            "失恋博物馆": {}
        },
        "新华": {
            "新华书店": {},
            "人民广场": {},
            "北国商城": {}
        }
    },
}

# 1. 可以循环输出。
# 2. 接受用户输入，打印 用户输入城市的下级城市。

# 升级需求：
# 3. q 可以退回上一级
# 4. Q 推到最后。
# 5. 退到最后之后，用户再退，要有提示 已经退回到最顶级
# 6. 代码不超过20行

chooses = []
current_menu = menu
while True:
    for i in current_menu:
        print(i)
    choice = input("please enter your choice:")
    if not choice: continue
    if choice in current_menu:
        chooses.append(current_menu)
        current_menu = current_menu[choice]
    else:
        if chooses and choice == "q":
            current_menu = chooses.pop()
        elif chooses and choice == "Q":
            current_menu = menu
        elif not chooses:
            print("已经到最顶层")


