# coding: utf8
""" 
@File: run.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/22 15:23
"""

from src.GPT.util import CONF as conf
from src.GPT.service import gpt


def main():
    while True:
        try:
            prompt = input("您想问什么？: ")
            if prompt.lower() == "结束会话":
                break
            answer = gpt.ask(prompt)
            print(answer)
        except Exception as error:
            print(error)
        
