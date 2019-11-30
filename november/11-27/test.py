# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/27 9:01


import asyncio
import aiohttp


async def spider(url):
    result = aiohttp.request(url)
    return result


async def task(url):
    print("starting........")
    x = await asyncio.spider(url)
    await x
    print("end.................")


loop = asyncio.get_event_loop()
tasks = [task("www.baid.com"), task("www.baid.com"), task("www.baid.com"), task("www.baid.com"), task("www.baid.com")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
