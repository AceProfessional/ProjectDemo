# coding: utf8
""" 
@File: RequestParam.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/24 22:37
"""

import os
from src.GPT.util.Utils import (
    construct_text
)


def get_reqsponse(openai_api_key, system_prompt, history, temperature, top_p, stream, selected_model):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(openai_api_key)
    }

    payload = {
        'model': selected_model,
        'history': history
    }
