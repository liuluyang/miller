# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 11:38


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import requests
import json
import os
import time


def get_page(url):
    print('<进程%s> get %s' % (os.getpid(), url))
    respones = requests.get(url)
    if respones.status_code == 200:
        return {'url': url, 'text': respones.text}


def parse_page(res):
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))

    with open('db.txt', 'a') as f:
        f.write(parse_res)

    filename = res['url']
    with open(os.path.join(filename, ".html"), "w") as f:
        f.write(res['text'])

if __name__ == '__main__':

    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    start = time.time()
    p = ThreadPoolExecutor(3)
    # p = ProcessPoolExecutor(3)

    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)
        # parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果
    p.shutdown()

    print(time.time()-start)