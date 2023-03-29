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


def test():
    # old_msg = bot.test('123')
    # msg = old_msg.append(bot.construction_user(text='456'))
    # print(old_msg)
    print(bot.rep(messages='你好'))


if __name__ == '__main__':
    test()
