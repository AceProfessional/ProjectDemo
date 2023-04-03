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

from utils.config import DefaultConfiguration

_default_configuration = DefaultConfiguration()

project_path = _default_configuration.project_path
config_path = _default_configuration.config_path
conf = _default_configuration.config
logs = _default_configuration.logs
env = _default_configuration.run_environment
