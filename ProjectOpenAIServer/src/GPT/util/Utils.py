# coding: utf8
""" 
@File: Utils.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/24 22:51
"""


def construct_text(role, text):
    return {"role": role, "content": text}

def construct_user(test):
    return {'user', test}

def construct_system(text):
    return {'system': text}

