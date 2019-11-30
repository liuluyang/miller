import sys
import time


def progress_bar(total, finished=0):
    current = finished
    while current < total:
        cur_size = yield
        current += cur_size
        num = int(current/total * 100)
        cur_plan = "=" * num
        kong_plan = " " * (100-num)
        print("\r[{}{}]{:.1%}".format(cur_plan, kong_plan, current/total), end="")


pro = progress_bar(5050, 2000)
next(pro)


for i in range(1, 101):
    try:
        pro.send(i)
        time.sleep(0.1)
    except StopIteration as e:
        pass


# dic = {0: 1, 2: 3}
#
# res = 2 in dic
# print(res)


