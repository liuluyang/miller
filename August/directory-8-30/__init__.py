# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/30 10:02



"""
周考
"""
"""
注：
所有考题必须在函数内作答
"""

"""
第一题：
返回一个列表
列表包含数字、字符串、列表、元祖、字典、集合六种数据
每种数据必须命名
"""

def func_01():
    """
    第一题
    :return:
    """
    li = [int, tuple, float, str, list, set, dict]
    li1 = []
    for i in range(len(li)):
        if isinstance(li[i], dict):
            res = li[i](((i,i*2),))
        else:
            res = li[i](i)
        li1.append(res)
    return li1


"""
第二题：
s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
s_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
把字符串s处理成一个新的字符串s_new并返回
"""
def func_02():
    """
    第二题
    :return:
    """
    s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
    s = s.replace("|", ",").replace(" ", "")
    return s
# print(func_02())
"""
第三题：
s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
data = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
把字符串s处理成一个字典data并返回
"""
def func_03():
    """
    第三题
    :return:
    """
    s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
    s = s.replace(" ", "").split("|")
    dic = {}
    for i in s:
        k, v = i.split(":")
        dic[k] = v
    return dic
# print(func_03())
"""
第四题：
nums = [random.randrange(1, 101) for _ in range(100)]
计算出列表nums所有数的和、奇数的和、偶数的
把结果放进字典result并返回
注：不能用内置函数sum()
"""
def func_04():
    """
    第四题
    :return:
    """
    import random
    nums = [random.randrange(1, 101) for _ in range(100)]
    result = {'所有数和':0, '奇数和':0, '偶数和':0}
    for i in nums:
        if i % 2 == 0:
            result["偶数和"] += i
        elif i %2 != 0:
            result['奇数和'] += i
        result["所有数和"] += i
    return result


# print(func_04())

"""
第五题：
nums = [random.randrange(1, 101) for _ in range(100)]
找出列表nums最大数、最小数
把结果放进字典result并返回
注：不能用内置函数max()min()
"""
def func_05():
    """
    第五题
    :return:
    """
    import random
    nums = [random.randrange(1, 101) for _ in range(100)]
    result = {'最大数':nums[0], '最小数':nums[0]}
    for i in nums:
        if i > result["最大数"]:
            result["最大数"] = i
        if i < result["最小数"]:
            result["最小数"] = i
    return result

# print(func_05())
"""
第六题：
nums_01 = [random.randrange(1, 101) for _ in range(100)]
nums_02 = [random.randrange(1, 101) for _ in range(100)]
找出两个列表里面都有的数字、和所有出现过的数字
把结果放进字典result并返回
"""
def func_06():
    """
    第六题
    :return:
    """
    import random
    nums_01 = set([random.randrange(1, 101) for _ in range(100)])
    nums_02 = set([random.randrange(1, 101) for _ in range(100)])
    # nums_01 = set(i for i in range(1, 11))
    # nums_02 = set(i for i in range(5, 16))

    # result = {'都有的数字':None, '所有出现过的数字':None}
    result = {'都有的数字':nums_01 & nums_02, '所有出现过的数字':nums_01 | nums_02}

    # nums_001 = nums_01 & (nums_02)  # 求交集
    # nums_002 = nums_01 | nums_02 # 求并集
    #
    # print(nums_001)
    # print(nums_002)
    return result
# print(func_06())

"""
第七题：
工资信息
data = {'佩奇':15000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000, '白姑娘':10000}
按他们的工资大小进行排序，之后把他们的姓名放进列表并返回
"""
def func_07():
    """
    第七题
    :return:
    """
    data = {'佩奇': 15000, '老男孩': 6000, '海峰': 7000, '马JJ': 8000, '老村长': 9000, '黑姑娘': 10000, '白姑娘': 10000}

    return [i[0] for i in sorted(data.items(), key=lambda x: x[1], reverse=True)]

# print(func_07())
"""
第八题：
把文件 我的作品.txt 的内容按顺序进行编号
之后打乱作品写入一个新的文件，类似于 我的作品_打乱.txt 的内容 
"""
def func_08():
    """
    第八题
    :return:
    """
    import random
    with open("xxx", "r", encoding="utf8") as f, open("xxxx", "w") as fp:
        li = [str(ind)+val.strip() for ind, val in enumerate(f.readlines(), 1)]
        fp.writelines(random.shuffle(li))


class Person(object):
    def __init__(self, name):
        super(self, Person).__init__()


"""
第九题：
写个函数
每次调用该函数返回一个符合要求的车牌号
车牌号要求：
五位数、必须同时包含数字和字母
"""
def func_09():
    """
    第九题
    :return:
    """
    import string, random,re
    while True:
        res = re.match("(?![0-9]$)(?![A-Za-z$])([A-Za-z0-9]{5})", "".join(random.sample(string.ascii_uppercase + string.digits, k=5)))
        if res:
            return res.group()

# print(func_09())
"""
第十题：
用循环打印下面的图形：大小不必一样
              *               
             * *              
            *****             
           *     *            
          *********           
         *         *          
        *************         
       *             *        
      *****************       
     *                 *      
      *****************       
       *             *        
        *************         
         *         *          
          *********           
           *     *            
            *****             
             * *              
              *
"""
def func_10():
    """
    第十题
    :return:
    """


"""
第十一题：
这里有一个 食堂账本.txt
统计一下总收入、最受欢迎的菜品
注：
1.最受欢迎菜品可能不止一种
2.有的菜品有大小份，但是算作一种菜品，也就是忽略大小份
"""
def func_11():
    """
    第十一题
    :return:
    """
    result = {'总收入':0, '最受欢迎的菜品':[]}


"""
第十二题：
写一个递归函数打印出1->10-10->1的数
"""
def func_12(num=0):
    """
    第十二题
    :return:
    """

    if num == 10:
        return 10
    num += 1
    print(num)
    func_12(num)
    print(num)

# func_12()

"""
第十三题：
写一个计算函数运行时间的装饰器
"""
import time
def func_13(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(time.time() - start_time)
    return inner


"""
第十四题：
写一个可以产生一百万个数字的生成器
"""
def func_14():
    """
    第十四题
    :return:
    """
    return (i for i in range(1000000))

# print(func_14())

"""
第十五题：
统计一下自己项目里面有多少python文件,以及总共有多少行代码
"""
def func_15(document_path,distinct):
    """
    第十五题
    :return:
    """
    import os
    if not document_path or not os.path.exists(document_path):
        return 0
    if os.path.isfile(document_path) and os.path.splitext(document_path)[1] in [".py", ".html", ".css", ".js"]:
        with open(document_path, "r", encoding="utf-8") as f:
            for i in f:
                if i != "\n":
                    distinct.add(i)
        return
    elif os.path.isdir(document_path):
        li = os.listdir(document_path)
        for i in li:
            file_dir_path = os.path.join(document_path, i)
            func_15(file_dir_path, distinct)
    return len(distinct)


print(func_15(input(), set()))

if __name__ == '__main__':
    pass


