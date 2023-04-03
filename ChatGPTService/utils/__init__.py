# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/29 19:51
"""

from utils.config import DefaultConfiguration, GPTConfiguration, LogsConfiguration

_default_configuration = DefaultConfiguration()
_gpt_configuration = GPTConfiguration()
_logs_configuration = LogsConfiguration()

project_path = _default_configuration.project_path
config_path = _default_configuration.config_path
gpt_configuration = _gpt_configuration.config()
logs = _logs_configuration.logs()
