# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/22 16:48
"""

from .GlobalConfig import DefaultConfig, GlobalGPTConfig

# Defaults config
CONF = DefaultConfig()
# GPT defaults config
GPT_CONF = GlobalGPTConfig().config()


