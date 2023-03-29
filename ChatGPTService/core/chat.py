# coding: utf8
""" 
@File: chat.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/29 20:06
"""

from utils import gpt_configuration
import requests
import json
from tqdm import tqdm


class ChatBot:

    def __init__(self):
        pass

    def __construction_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(gpt_configuration.get('key'))
        }
        return headers

    def __construction_messages(self, text):
        msg = [
            self.construction_system(text='You are an assistant.'),
            self.construction_user(text=text)
        ]
        return msg

    def __construction_text(self, role, text):
        return {'role': role, 'content': text}

    def construction_user(self, text):
        return self.__construction_text(role='user', text=text)

    def construction_system(self, text):
        return self.__construction_text(role='system', text=text)

    def construction_assistant(self, text):
        return self.__construction_text(role='assistant', text=text)

    def test(self, text):
        return self.__construction_message(text=text)

    def __construction_data(self, messages):
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': self.__construction_messages(text=messages),
            'temperature': 1,
            'top_p': 1,
            'n': 1,
            'stream': True,
            # 'max_tokens': 4096,
            'presence_penalty': 0,
            'frequency_penalty': 0
        }
        return data

    def __gpt_response(self, messages):
        response = requests.post(
            url=gpt_configuration.get('url'),
            data=json.dumps(self.__construction_data(messages=messages)),
            headers=self.__construction_headers()
        )
        return response

    def rep(self, messages):
        response = self.__gpt_response(messages=messages)
        for data in tqdm(response.iter_lines()):
            data: bytes
            if data != b'':
                data = data.decode().split('data: ')[1]
                if data != '[DONE]':
                    print(data)
                    # if json.loads(data)['choices'][0]['delta']['role'] == 'assistant':
                    #     pass
                    # else:
                    content = json.loads(data)['choices'][0]['delta']['content']
                    print(content)
        return 



