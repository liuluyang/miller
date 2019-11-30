# import sys
# import os
#
# result = sys.argv
#
# if len(result) != 4:
#     msg = '''need [old_str new_str filename]'''
#     exit("参数错误退出\n%s" % msg)
# else:
#     _, old_str, new_str, filename = result
#     new_filename = filename + "new"
#     with open(filename, "r", encoding="utf-8") as f, open(new_filename, "w", encoding="utf-8") as w_f:
#         for line in f:
#             line1111 = line.replace(old_str, new_str)
#             w_f.write(line1111)
#     os.replace(new_filename, filename)

# user_info = None
# with open("./account.json", "r", encoding="utf-8") as f:
#     user_info = eval(f.read())

# for i in range(3):
#     username = input("Please enter your username:").strip()
#     password = input("Please enter your password:").strip()
#     if user_info["state"] == 1:
#         if user_info["username"] == username and user_info["password"] == password:
#             print("welcome to beijing")
#             break
#         else:
#             print("username or password was wrong")
#     else:
#         exit("账户被锁定, 请联系管理员")
# else:
#     user_info["state"] = 0
#     with open("./account.json", "w", encoding="utf-8") as f:
#         f.write(str(user_info))

# n = 0
# while n < 3:
#     username = input("Please enter your username:").strip()
#     password = input("Please enter your password:").strip()
#     if not username or not password:
#         print("不能输入空, 请重新输入")
#         continue
#     if user_info["username"] == username and user_info["password"] == password:
#         print("welcome to beijing")
#         break
#     else:
#         print("username or password was wrong")
#     n += 1
# else:
#     user_info["state"] = 0
#     with open("./account.json", "w", encoding="utf-8") as f:
#         f.write(str(user_info))

title = None
all_data = []

with open("./stock_data.data", "r", encoding="utf-8") as f:
    title = f.readline().split()
    for line in f:
        all_data.append(line.strip().split())

while True:
    li = []
    option = input("\033[31;1m查询接口:\033[0m").strip()
    if "<" in option:
        name, val = option.split("<")
        ind = title.index(name)
        if val.isdigit:
            val = float(val)
        for row in all_data:
            if float(row[ind]) < val:
                li.append(row)
    elif ">" in option:
        name, val = option.split(">")
        ind = title.index(name)
        if val.isdigit:
            val = float(val)

        for row in all_data:
            if float(row[ind]) > val:
                li.append(row)
    else:
        ind = title.index("名称")
        for row in all_data:
            if option in row[ind]:
                li.append(row)
    print(title)
    for i in li:
        print(i)



















