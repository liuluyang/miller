# host = ("127.0.0.1", 8000)
# print(host)
# print(type(host))

# tu = tuple()
# print(tu)
# print(type(tu))

# host = ("127.0.0.1", 8000)

# li = [1, 544, 465, 654, 4, 9, 4, 541, 674, 68, 416, 54, 6874, 6, 54, 34, 456, 413, 513]
# tu = (1, 544, 465, 654, 4, 9, 4, 541, 674, 68, 416, 54, 6874, 6, 54, 34, 456, 413, 513)

# tu = ("miller", 123, [555, 666, 777])
#
# print(tu[0])
# tu[2][1] = "liusir"
#

# print(tu)

import time

while True:
    n = 10
    for i in range(10):
        time.sleep(0.02)
        print(" " * (n - i) + "*" * (i * 2 + 1))

    for j in range(8, 0, -1):
        time.sleep(0.02)
        print(" " * (n - j) + "*" * (j * 2 + 1))


