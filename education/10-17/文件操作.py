
# f = open(r".\staff.txt", mode="r", encoding="utf-8")
# res = f.read()
# print(res)
# f.close()

# f = open(r"E:\project\education\10-16\staff.txt", mode="w", encoding="utf8")
# f.write('''Miller 23 CEO 66666\nOldDriver 25 driver 4444\n我爱你''')
# f.close()


# f = open(r"E:\project\education\10-16\staff.txt", mode="a", encoding="utf-8")
# f.write("\nmiller")
# f.close()


import struct

# print(struct.pack("i", 1234569008))
#
# print(16**3*16*2*16**1*16**0)
#
print(struct.unpack("i", b'0\x07\x96I')[0])

print(256**4-1)

# print(int("11111111", 2))


