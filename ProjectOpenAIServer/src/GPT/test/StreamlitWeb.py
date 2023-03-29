# coding: utf8
""" 
@File: StreamlitWeb.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/25 19:14
"""

import openai
import streamlit as st
import random

KeyList = [
    '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',
    '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',
    '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',
    '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',
    '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',
]

# from message_log import message_log

message_log = [{"role": "user", "content": "你好！"}]

api_key = random.choice(KeyList)
openai.api_key = api_key


def generate_response(message_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,  # The conversation history up to this point, as a list of dictionaries
        temperature=0.5,  # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


def web():
    st.set_page_config(page_title="GPT")
    st.markdown("# 当前使用模型为gpt-3.5-turbo")
    # 增加一个按钮，点击后清空对话记录，重新开始对话
    if st.button('重制对话'):
        st.balloons()
        # api_key = random.choice(KeyList)
        # print(api_key)
        st.session_state['generated'] = []
        st.session_state['past'] = []
        message_log.clear()
        st.experimental_rerun()
    st.markdown("### 请在下方输入对话内容, `Ctrl`+`Enter`即可开始对话")

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    user_input = st.text_area("You:", key='input')

    if user_input:
        message_log.append({"role": "user", "content": user_input})
        output = generate_response(message_log)
        message_log.append({"role": "assistant", "content": output})
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            st.markdown(f'''**弱智你的:**  {st.session_state['past'][i]}''')
            st.markdown(f'''**强大的AI:**  {st.session_state["generated"][i]}''')
            # 添加分隔符，跟输入框的长度一致
            st.markdown(f'''---''')


if __name__ == '__main__':
    print(api_key)
    web()
