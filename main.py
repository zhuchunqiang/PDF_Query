import streamlit as st

from utils import qa_agent

st.title("📑 AI智能PDF问答工具")

with st.sidebar:
    api_key = st.text_input("请输入Moon API密钥：", type="password")
    st.markdown("[获取Moon API key](https://moonshot.cn/)")

uploaded_file = st.file_uploader("上传你的PDF文件：", type="pdf")
question = st.text_input("对PDF的内容进行提问", disabled=not uploaded_file)

if uploaded_file and question and not api_key:
    st.info("请输入你的Moon API密钥")

if uploaded_file and question and api_key:
    with st.spinner("AI正在思考中，请稍等..."):
        response = qa_agent(api_key, uploaded_file, question)
    st.write("### 答案")
    st.write(response)
