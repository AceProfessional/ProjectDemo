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
import random
import requests
import json
from src.GPT.util import CONFIG, public_tools


class GPT:
    """ GPT """

    def __init__(self):
        self.__GPT_CONFIG: dict = CONFIG.get('gpt_api')
        self.__key: str = random.choices(self.__GPT_CONFIG.get('key'))[0]

    def __requests_headers(self) -> dict:
        headers         = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__key)
        }
        return headers

    def __requests_message(self, text) -> list:
        msg = [
            public_tools.construct_system(text='You are a helpful assistant.'),
            public_tools.construct_user(text=text)
        ]
        return msg

    def __requests_data(self, text) -> dict:
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': self.__requests_message(text=text),
            'temperature': 1,
            'top_p': 1,
            'n': 1,
            'stream': True,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }
        return data

    def ask(self, prompt) -> str:
        """
        GPTAsk
        :param prompt: str: question
        :return: : str: answer
        """
        openai.api_key = self.__key
        response = openai.Completion.create(
            # engine='text-davinci-003',
            model='text-davinci-003',
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

    def get_response(self, text) -> requests.Response:
        response = requests.post(
            url=self.__GPT_CONFIG.get('url'),
            headers=self.__requests_headers(),
            data=json.dumps(self.__requests_data(text=text))
        )
        return response
        # try:
        #     if response.status_code == 200:
        #         return json.loads(response.content.decode('utf-8'))
        # except Exception as error:
        #     print(error)

    def bot_output(self, ask):
        response = self.get_response(text=ask)
        for i in response.iter_lines():
            print(json.load(i.decode()))
        # yield response.get('choices')[0]['message']['content']
