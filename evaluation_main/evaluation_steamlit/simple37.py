import streamlit as st

st.title("简单的 Chatbot")

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []


# 用户输入
user_input = st.chat_input("请输入您的问题：")

# 当用户输入内容时，将其添加到聊天记录中
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "bot", "content": f"您刚才说了：{user_input}"})

# 显示聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
