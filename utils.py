from openai import OpenAI

def qa_agent(api_key,uploaded_file,question):
    client = OpenAI(api_key=api_key,
                    base_url="https://api.moonshot.cn/v1"
                    )
    file_object = client.files.create(file=uploaded_file, purpose="file-extract")
    file_content = client.files.content(file_id=file_object.id).text

    # 把文件内容通过系统提示词 system prompt 放进请求中
    messages = [
        {
            "role": "system",
            "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。",
        },
        {
            "role": "system",
            "content": file_content,  # <-- 这里，我们将抽取后的文件内容（注意是文件内容，而不是文件 ID）放置在请求中
        },
        {"role": "user", "content":question},#"请简单介绍 论文介绍.pdf 的具体内容"
    ]

    # 然后调用 chat-completion, 获取 Kimi 的回答
    completion = client.chat.completions.create(
        model="moonshot-v1-32k",
        messages=messages,
        temperature=0.3,
    )
    response = completion.choices[0].message.content
    return response
