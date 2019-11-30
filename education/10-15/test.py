

# 100 - 1000 之内， 各位数相加之和 == 5

li = []
for i in range(100, 1001):
    sum_num = 0
    for n in str(i):
        sum_num += int(n)
    if sum_num == 5:
        li.append(i)

print(li)


li = []
for i in range(100, 1000):
    a, b = divmod(i, 100)
    c, d = divmod(b, 10)
    if a + c + d == 5:
        li.append(i)

print(li)
