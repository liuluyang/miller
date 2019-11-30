
# 作业：双色球选购
# 1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
# 2 确保用户不能重复选择，不能超出范围
# 3 用户输入有误时有相应的错误提示
# 4 最后展示用户选择的双色球的号码


# 升级需求：
# 1 一个while循环

red_ball = []
blue_ball = []

# while len(red_ball) < 6:
#     number = int(input("\033[31;0m 请选择红球：\033[0m"))
#     if 1 <= number <= 32:
#         if number in red_ball:
#             print("不能重复选择")
#         else:
#             red_ball.append(number)
#             print("已经将 %d 号球, 添加到列表中！！！" % number)
#     else:
#         print("超出选择范围")
#
#
# while len(blue_ball) < 2:
#     number = int(input("\033[34;0m 请选择篮球：\033[0m"))
#     if 1 <= number <= 16:
#         if number in blue_ball:
#             print("不能重复选择")
#         else:
#             blue_ball.append(number)
#             print("已经将 %d 号球, 添加到列表中！！！" % number)
#     else:
#         print("超出选择范围")
#
# print(red_ball)
# print(blue_ball)

while True:
    if len(red_ball) < 6:
        _ball = int(input("\033[31;0m 请选择红球：\033[0m"))
        if 1 <= _ball <= 32:
            if _ball not in red_ball:
                red_ball.append(_ball)
                print("已经将 %d 添加到列表中" % _ball)
            else:
                print("不能重复添加")
        else:
            print("不能超出范围")

    elif len(blue_ball) < 2:
        _ball = int(input("\033[34;0m 请选择蓝球：\033[0m"))
        if 1 <= _ball <= 16:
            if _ball not in blue_ball:
                blue_ball.append(_ball)
                print("已经将 %d 添加到列表中" % _ball)
            else:
                print("不能重复添加")
        else:
            print("不能超出范围")
    else:
        break

print(red_ball)
print(blue_ball)






























