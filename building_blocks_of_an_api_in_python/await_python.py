# -- coding: utf-8 --
"""

Created on: 10/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import asyncio
async def main():
    await asyncio.sleep(4)
    await asyncio.sleep(2)
    return "hello"

print(asyncio.run(main()))

