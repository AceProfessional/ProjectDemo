# coding: utf8
""" 
@File: run.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/27 13:23
"""

# from src.GPT.run import main

import openai

from src.GPT.service import gpt

def test(message):
    openai.api_key='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'
    
    def create_sessions():
        response = openai.ChatCompletion.create(
            model='gpt-4',
            # model='gpt-3.5-turbo',
            messages=message,
            timeout=30
        )
        return response
    
    response = create_sessions()
    return response.choices[0].text.strip()

if __name__ == '__main__':
    # print(test('你好'))
    print(gpt.bot_output(ask='你好'))
    # main()
    pass
