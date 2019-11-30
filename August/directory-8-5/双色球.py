# 作业：双色球选购
# 1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
# 2 确保用户不能重复选择，不能超出范围
# 3 用户输入有误时有相应的错误提示
# 4 最后展示用户选择的双色球的号码
# 升级需求：
# 1 一个while循环

# red_ball = []
# blue_ball = []
#
# while True:
#     if len(red_ball) < 6:
#         red_num = input("\033[0;31;0m please select your red number:\033[0m").strip()
#         if not red_num.isdigit():
#             print("only select 1-32 number")
#         elif 0 > int(red_num) or int(red_num) > 32:
#             print("only select 1-32 number")
#         elif red_num not in red_ball:
#             red_ball.append(red_num)
#         elif red_num in red_ball:
#             print("repetition number")
#
#     elif len(blue_ball) != 2 and len(red_ball) == 6:
#         blue_num = input("\033[0;34;0m please select your blue number: \033[0m").strip()
#         if not blue_num.isdigit():
#             print("only select 1-32 number")
#         elif 0 > int(blue_num) or int(blue_num) > 16:
#             print("only select 1-32 number")
#         elif blue_num not in blue_ball:
#             blue_ball.append(blue_num)
#         elif blue_num in blue_ball:
#             print("repetition number")
#     else:
#         print(red_ball, "\n", blue_ball, "\n", "Good luck")
#         break

#