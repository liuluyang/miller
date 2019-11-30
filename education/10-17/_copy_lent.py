import copy


data = {
    "name": "alex",
    "age": 18,
    "scores": {
        "语文": 130,
        "数学": 60,
        "英语": 98,
    }
}



# d2 = copy.copy(data)
#
# data["age"] = 20
#
# print(d2)
# print(data)


# d2 = copy.copy(data)
#
# print(id(data))
# data["name"] = "liusir"
# print(id(data["name"]))
# data["scores"]["语文"] = 180
# print(id(data["scores"]["语文"]))
#
#
# print("-".center(50,"-"))
# print(id(d2))
# print(id(d2["name"]))
# print(id(d2["scores"]['语文']))


# d2 = copy.deepcopy(data)
#
# print(id(data))
# data["name"] = "liusir"
# print(id(data["name"]))
# data["scores"]["语文"] = 180
# print(id(data["scores"]["语文"]))
#
#
# print("-".center(50,"-"))
# print(id(d2))
# print(id(d2["name"]))
# print(id(d2["scores"]['语文']))


# print(2**15+2**14+2**13+2**11+2**10+2**9+2**8+2**7+2**5+2**3)

# 500
# 110100110110110

# print(bin(500))
# print(int("110100110110110",2))


# 50F3

# print(hex(1443))
# print(5*16**3+15*16**1+3*16**0)
# print(int("0x522", 16))


# print(ord("A"))
# print(chr(32), end="")

# res = "中国".encode("utf-8")
# print(type(res), res)


# print(b'\xd6\xd0\xb9\xfa'.decode("GBK"))
#
# print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode("utf8"))

# b'\xc2\xeb    \xbf\xcd'

# print("ksdkfgsajkdf")


# print(hash("miller"))
# print(hash("miller"))
# print(hash("miller"))



