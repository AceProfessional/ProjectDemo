# coding: utf8
""" 
@File: interaction.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/22 15:29
"""

import openai


class GPT:

    def __init__(self):
        self.__key = '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'

    def ask(self, prompt):
        openai.api_key = self.__key
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=1024,
            stop=None,
            temperature=0.3,
            n=1,
            timeout=30
        )

        answer = response.choices[0].text.strip()
        # answer = response.response.choices[0].text.strip()
        return answer

    def __create(self):
        openai.api_key = self.key
        openai.Completion.create(
            prompt='python项目层级规范示例',
            model='text-davinci-003',
            timeout=30,
            max_tokens=1000
        )
