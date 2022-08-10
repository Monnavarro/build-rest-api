# -- coding: utf-8 --
"""

Created on: 10/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import asyncio
import time

async def func1():
    for i in range(5):
        print("Inside Func1")
        await asyncio.sleep(1)

async def func2():
    for i in range(5):
        print("Inside Func2")
        await  asyncio.sleep(.8)

start = time.time()
async_task = asyncio.gather(func1(), func2())
asyncio.get_event_loop().run_until_complete(async_task)
end = time.time()
print('Asyncio took {} seconds'.format(round(end-start), 2))

