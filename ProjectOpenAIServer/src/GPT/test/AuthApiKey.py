# coding: utf8
""" 
@File: AuthApiKey.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/25 23:00
"""

import random

class AuthApiKeyClass:
    
    def __init__(self):
        self.__KeyList = [
            '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',
            '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',
            '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',
            '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',
            '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',
        ]
        
    def __get_key(self):
        return random.choice(self.__KeyList)
        
    @classmethod
    def key(cls):
        return cls().__get_key()
