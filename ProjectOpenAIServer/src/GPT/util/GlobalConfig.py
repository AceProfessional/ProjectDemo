pip# coding: utf8
""" 
@File: GlobalConfig.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/22 15:36
"""

import os
import platform
import sys
import json
from loguru import logger


class DefaultConfig:
    """ Project defaults config """

    def __init__(self):
        if platform.system() == 'Linux':
            self.__SEPARATOR = '/'
        elif platform.system() == 'Windows':
            self.__SEPARATOR = '\\'
        else:
            sys.exit(1)
        self.PROJECT_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
        self.CONFIG_PATH = os.path.join(self.PROJECT_ROOT, f'src{self.__SEPARATOR}GPT{self.__SEPARATOR}conf{self.__SEPARATOR}config.json')


class GlobalGPTConfig(DefaultConfig):
    """ ChatGPT config """

    def config(self) -> dict:
        """
        Config
        :return: dict: GPT config 
        """
        try:
            if os.path.isfile(self.CONFIG_PATH):
                pass
            else:
                self.CONFIG_PATH = os.path.join(self.PROJECT_ROOT, 'config.json')
                if os.path.isfile(self.CONFIG_PATH):
                    pass
                else:
                    print('配置文件不存在')
                    sys.exit()
        except Exception as error:
            print(error)
        with open(file=self.CONFIG_PATH, mode='r', encoding='utf-8') as config_content:
            config = json.load(config_content)
        return config

