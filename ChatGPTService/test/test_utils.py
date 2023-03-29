# coding: utf8
""" 
@File: test_utils.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/29 19:53
"""

from utils import project_path, config_path, gpt_configuration

def test():
    print('项目路径: {}'.format(project_path))
    print('配置路径: {}'.format(config_path))
    print('读取配置文件: {}'.format(gpt_configuration))
    print('gpt_key: {}'.format(gpt_configuration.get('key')))
    print('gpt_url: {}'.format(gpt_configuration.get('url')))
    
    
if __name__ == '__main__':
    test()
