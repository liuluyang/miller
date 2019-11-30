# 作业：双色球选购
# 1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
# 2 确保用户不能重复选择，不能超出范围
# 3 用户输入有误时有相应的错误提示
# 4 最后展示用户选择的双色球的号码
# 升级需求：
# 1 一个while循环
#
red_ball = []  # 6个红球，球号1-32
blue_ball = []  # 2个蓝球，球号1-16

while True:
    if len(red_ball) < 6:
        red_num = input("\033[0;31;0m please select your red ball: \033[0m").strip()
        if not red_num.isdigit() or 1 > int(red_num) or int(red_num) > 32:
            print("输入值 只能是 1 - 32")
        elif red_num not in red_ball:
            red_ball.append(red_num)
        elif red_num in red_ball:
            print(" 不能选择重复的 球")
    elif len(blue_ball) < 2 and len(red_ball) == 6:
        blue_num = input("\033[0;34;0m please select your red ball: \033[0m").strip()
        if not blue_num.isdigit() or 1 > int(blue_num) or int(blue_num) > 16:
            print("输入值 只能是 1 - 16")
        elif blue_num not in blue_ball:
            blue_ball.append(blue_num)
        elif blue_num in blue_ball:
            print(" 不能选择重复的 球")
    else:
        print(red_ball, "\n", blue_ball, "\n", "Good Luck")
        break


def binary_search(x, li):
    left = 0
    right = len(li) - 1
    while True:
        mid = (left + right) // 2
        if x == li[mid]:
            return mid
        if x > li[mid]:
            left = mid + 1
        if x < li[mid]:
            right = mid - 1


for i in range(1, 5):
    for y in range(1, 6+i):
        print('%s*%s=%s' % (i, y, i * y), end=' ')
    print()

#
# 猜数游戏：
# 随机生一个1-10之间的数
# 最多可以猜三次，如果猜错，会提示猜大了还是猜小了
# 猜对游戏直接结束
# 如果三次都没猜对，最后打印出那个随机数

import random

num = random.randrange(1, 11)
print('随机数已生成， 猜数游戏开始。。。')

for i in range(3):
    number = input("请输入数字:").strip()
    number = int(number)
    if number == num:
        print("恭喜你猜对了")
        break
    elif number > num:
        print("猜的大了")
    elif number < num:
        print("猜的小了")
else:
    print("你要猜的数字是：", num)


for i in range(1, 5):
    for j in range(1, 6 + i):
        print("{} * {} = {}".format(i, j, i * j), end="  ")
    print()


import random

num = random.randrange(1, 10)

print("开始随机数游戏")

for i in range(3):
    number = input("请输入你想的数字:").strip()
    number = int(number)
    if number > num:
        print("大了， 往小猜一猜")
    elif number < num:
        print("小了， 往大猜一猜")
    else:
        print("恭喜你猜对了， But  么的奖励")
        break
else:
    print(num)

n = 0
while n < 3:
    number = input("请输入你想的数字:").strip()
    number = int(number)
    if number > num:
        print("大了， 往小猜一猜")
    elif number < num:
        print("小了， 往大猜一猜")
    else:
        print("恭喜你猜对了， But  么的奖励")
        break
    n+=1
else:
    print(num)


