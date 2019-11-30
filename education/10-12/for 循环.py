# li = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# n = 0
# while True:
#     if n < len(li):
#         print(li[n])
#     else:
#         break
#     n += 1


# for i in li:
#     print(i)

#  range(1, 100, 2):  # start end step
# start 从那开始
# end  到哪结束
# step 每个几个 取一个值

# for i in range(1, 100, 2):  # start end step
#     print(i)


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(" %d * %d = %d " % (j, i, j*i), end="")
#     print()


print("\n".join(["  ".join(["%d * %d = %d" % (i, j, i*j) for i in range(1, j + 1)]) for j in range(1, 10)]))


