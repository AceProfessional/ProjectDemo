# coding: utf8
""" 
@File: config.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/29 19:42
"""

import os
import platform
import sys
import json


class DefaultConfiguration:

    def __init__(self):
        self.project_path = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
        if platform.system() == 'Linux':
            separator = '/'
        elif platform.system() == 'Windows':
            separator = '\\'
        else:
            sys.exit()
        self.config_path = os.path.join(self.project_path, 'conf{}config.json'.format(separator))


class GPTConfiguration(DefaultConfiguration):
    
    def config(self, config_path=None):
        if config_path is None:
            config_path = self.config_path
        try:
            if os.path.isfile(config_path):
                with open(file=config_path, mode='r', encoding='utf8') as config_file:
                    config = json.load(config_file)
                return config
        except Exception as error:
            print('读取配置文件错误: {}'.format(error))
            sys.exit()


class LogsConfiguration:
    
    def __init__(self):
        pass
    
    def log(self):
        pass
