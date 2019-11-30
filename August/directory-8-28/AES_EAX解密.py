#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/14
from base64 import b64decode
from Crypto.Cipher import AES

# b64_dic ={'nonce': 'GH0NhqPl2Csw0TZrbi/bzA==', 'header': 'aGVhZGVy', 'ciphertext': 'kIzFfW0U3w==', 'tag': 'vScsoRy2k0CX3IaDUDBgdg=='}

# json_k = ['nonce', 'header', 'ciphertext', 'tag']

# json_v = {k:b64decode(v) for k, v in b64_dic.items()}

# key = b'\x08de#w\xe2\\\xee\x0e\xdam6\xec\xa4j\xcf'  # 这个就是前面的生成的密钥。

# cipher = AES.new(key, AES.MODE_EAX, nonce=jv["nonce"])

# cipher.update(jv["header"])
# cipher.update(b'miller.json')

# plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])

# print(plaintext.decode())

###############################################################################################


json_dic = {"key": "5sbc6bBcCnk5nQ5snX/Gzg==", "nonce": "MY3v1fViVmYxKx5+c9KI5w==", "ciphertext": "JVZaJ7jnmcTZZSvSWdHh/f2TBLQyg42OtuY1enLA", "tag": "2MQ5/7ghpjosJkXlRK2s6w=="}

dic = {key:b64decode(val) for key, val in json_dic.items()}


# 1. 得到加密的key
key = dic["key"]

# 2. 得到nonce
nonce = dic["nonce"]

# 3. 拿到 加密文本/ 标签
ciphertext = dic["ciphertext"]
tag = dic["tag"]

#4. 得到解密的对象
cipher = AES.new(key, mode=AES.MODE_EAX, nonce=nonce)

# 5. 进行解密
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print(plaintext.decode())







