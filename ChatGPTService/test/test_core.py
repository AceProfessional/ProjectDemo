# coding: utf8
""" 
@File: test_core.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/29 20:19
"""

from core import bot
from utils import logs
import os


def test():
    bot.test(text='测试消息')


if __name__ == '__main__':
    test()
