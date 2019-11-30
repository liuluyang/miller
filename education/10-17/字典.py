menu = {
    "北京": {
        "沙城": {
            "网吧": {},
            "ktv": {},
            "夜总会": {}
        },
        "朝阳": {
            "酒吧": {},
            "洗浴中心": {},
            "非正常按摩店": {}
        },
        "怀柔": {
            "足疗": {},
            "点穴减肥": {},
            "盲人按摩": {}
        }
    },
    "上海": {
        "陆家嘴": {
            "刘龙病史": {},
            "九龙冰室": {},
            "辽宁舰": {}
        },
        "蛇山": {
            "小白": {},
            "小青": {},
            "许仙": {},
            "法海": {}
        },
        "不知道": {
            "不知道1": {},
            "不知道2": {},
            "不知道3": {},
        }
    },
    "石家庄": {
        "藁城": {
            "网吧1号": {},
            "网吧2号": {},
            "网吧3号": {}
        },
        "阿里山": {
            "钻石大姐": {},
            "MK": {},
            "饺子馆":{}
        },
        "邯郸": {
            "没去过1":{},
            "没去过2":{},
            "没去过3":{},
        }
    },
}

last_menu = []

while True:
    for name in menu:
        print(name)
    choice = input("请输入城市名字：").strip()
    if not choice: continue
    if choice in menu:
        last_menu.append(menu)
        menu = menu[choice]
    elif choice == "q":
        if last_menu:
            menu = last_menu.pop()
        else:
            print("已经到最顶层")
    elif choice == "Q":
        if last_menu:
            menu = last_menu.pop(0)
            last_menu.clear()
        else:
            print("已经到最顶层")
















