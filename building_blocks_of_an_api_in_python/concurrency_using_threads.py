# -- coding: utf-8 --
"""

Created on: 10/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import threading
import time


def func1():
    for i in range(3):
        time.sleep(1)
        print("Inside Func1")


def func2():
    for i in range(5):
        time.sleep(.8)
        print("Inside Func2")


threading.Thread(target=func1).start()
threading.Thread(target=func2).start()

print("Threads started")

