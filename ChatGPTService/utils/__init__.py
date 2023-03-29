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

from utils.config import GPTConfiguration

__gpt_configuration = GPTConfiguration()

project_path: str = __gpt_configuration.project_path
config_path: str = __gpt_configuration.config_path
gpt_configuration: dict = __gpt_configuration.config()

