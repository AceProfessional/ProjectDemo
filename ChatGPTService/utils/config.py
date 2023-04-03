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
import logging
import os
import platform
import sys
import json
from loguru import logger
from datetime import datetime


class DefaultConfiguration:

    def __init__(self):
        self.project_path: str = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
        if platform.system() == 'Linux':
            separator = '/'
        elif platform.system() == 'Windows':
            separator = '\\'
        else:
            sys.exit()
        self.config_path: str = os.path.join(self.project_path, 'conf{}config.json'.format(separator))


class GPTConfiguration(DefaultConfiguration):

    def config(self, config_path=None) -> dict:
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


class LogsConfiguration(GPTConfiguration):

    @logger.catch()
    def logs(self):
        logs_date: str = datetime.now().strftime("%Y%m%d")
        logs_dir: str = os.path.join(self.project_path, 'logs')
        logs_path: str = os.path.join(logs_dir, 'access_{}.log'.format(logs_date))
        logs_level: str = self.config().get('log_level')
        logs_format: str = '[{time:YYYY-MM-DD HH:mm:ss}] {level: <8}[{name: <8}] : {message}'
        if os.path.isdir(logs_dir) is False:
            os.mkdir(logs_dir)
        try:
            logger.add(sink=logs_path, level=logs_level.upper(), rotation='00:00', encoding='utf8', format=logs_format)
            logs_level = logs_level.upper()
        except Exception as error:
            logger.add(sink=logs_path, level='DEBUG', rotation='00:00', encoding='utf8', format=logs_format)
            logs_level = 'DEBUG'
            logger.warning('默认日志级别: DEBUG, 配置信息错误: {}'.format(error))
        logger.success('日志服务启动成功: 日志级别: {} 日志保存路径: {}'.format(logs_level, logs_dir))

        return logger
