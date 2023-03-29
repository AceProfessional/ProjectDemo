# coding: utf8
""" 
@File: Tools.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/29 14:45
"""

class PublicTools:
    """ Public tools """
    
    def __init__(self):
        pass
    
    def __construct_text(self, role, text):
        return {'role': role, 'content': text}
    
    def construct_system(self, text):
        return self.__construct_text('system', text)
    
    def construct_user(self, text):
        return self.__construct_text('user', text)
    
    def construct_assistant(self, text):
        return self.__construct_text('assistant', text)
    
    def tokens_number(self, tokens):
        return 'tokens计数: {}'.format(tokens)
