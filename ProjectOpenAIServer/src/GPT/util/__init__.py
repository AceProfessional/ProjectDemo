# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/27 13:18
"""

from src.GPT.util.GlobalConfig import GlobalGPTConfig, DefaultConfig
from src.GPT.util.Tools import PublicTools

__DefaultConfig = DefaultConfig()
__GlobalGPTConfig = GlobalGPTConfig()

PROJECT_ROOT: str = __DefaultConfig.PROJECT_ROOT
CONFIG: dict = __GlobalGPTConfig.config()
public_tools = PublicTools()
