# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/28 14:41

import shutil
import os
# ############################################################################################
# shutil.copyfileobj
# with open("./file1", "r",) as read_f, open("./file2", "w", encoding="utf-8") as write_f:
#     shutil.copyfileobj(read_f, write_f)

# ############################################################################################
# shutil.copyfile  源文件必须存在,  目标文件可以不存在. 如果没有就创建
# res = shutil.copyfile(r"D:\education_project\directory-8-28\file1", r"D:\education_project\directory-8-28\file3")
# print(res)

# ############################################################################################
# 目标文件必须存在
# shutil.copymode(r"D:\education_project\directory-8-28\file1", r"D:\education_project\directory-8-28\file2")
#
# print(os.stat(r"D:\education_project\directory-8-28\file1").st_mode)
# # os.chmod(r"D:\education_project\directory-8-28\file2", 33060)
# print(os.stat(r"D:\education_project\directory-8-28\file2").st_mode)

# ############################################################################################
# 目标文件必须存在
# shutil.copystat(r"D:\education_project\directory-8-28\file1", r"D:\education_project\directory-8-28\file2")
#
# print(os.stat(r"D:\education_project\directory-8-28\file1"))

# ############################################################################################
# 源文件存在  目标文件不能存在
# shutil.copytree(r"D:\education_project\directory-8-28\folder1", r"D:\education_project\directory-8-28\folder2", ignore=shutil.ignore_patterns("*.py","*.pyc"))

# ############################################################################################

# shutil.rmtree(r"D:\education_project\directory-8-28\folder2")

# ############################################################################################

# shutil.move(r"D:\education_project\directory-8-28\folder2", r"D:\education_project\directory-8-28\folder1")
# 取决于目标文件是否是一个 真实存在的目录
# 如果存在则移动进去     否则就是剪切粘贴  换个名字

# ############################################################################################

# base_name="一个压缩包" 压缩包的名字
# base_dir=r"D:\education_project\directory-8-28\folder1"  要压缩的文件夹 路径
# 会根据给定的路径 压缩文件夹！


# shutil.make_archive(base_name=r"D:\education_project\110\一个压缩包", root_dir=r"D:\education_project\directory-8-28\folder1", format="zip", )
# 一个压缩包.zip ==> folder2


# shutil.make_archive(base_name=r"D:\education_project\110\一个压缩包", base_dir=r"./folder1", format="gztar", )
# 一个压缩包.zip ==> folder1

# ############################################################################################
# import zipfile

# zi = zipfile.ZipFile("./zip.zip", "w")
# zi.write(r"D:\education_project\directory-8-28\folder1\folder2\folder2\test.py\my_project\manage.py", arcname="manage.py")
# zi.close()

# zi = zipfile.ZipFile("./zip.zip", "r")
# zi.extractall(".")
# zi.close()

# ############################################################################################

# import tarfile

# ta = tarfile.open("./tar.tar", "w")
# ta.add(r"D:\education_project\directory-8-28\folder22222\folder2\folder2\test.py\my_project\app01\admin.py", arcname="admin.py")
# ta.close()

# a = tarfile.open("./tar.tar", "r")
# a.extractall(".")
# a.close()


# s = "abdscsbcva"
# set11 = set()
# li = []
#
# for ind, val in enumerate(s):
#     if val in set11:
#         li.remove(val)
#     else:
#         li.append(val)
#     set11.add(val)
#
# print(set11)
# print(li[0])


import configparser

config = configparser.ConfigParser()
config.read(r"D:\education_project\directory-8-28\install.ini")

for i in config.sections():
    print(i)

print(config["Setup"]["ProductName"])




