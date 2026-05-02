from openai import OpenAI

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system", "content": "你是一个Python编程专家，并且话非常多答"},
        {"role":"assistant", "content": "好的，我是编程专家，并且话很多，你要问什么？"},
        {"role":"user", "content":"输出1-10的数字，使用Python代码"}
    ],
    stream=True # 开启了流式输出的功能
)
# 输出结果
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",  #每一段之间以空格分隔
        flush=True  #立刻刷新缓冲区
    )


# messages=[
#         {"role": "system", "content": "你是一个Python编程专家，并且不说废话简单回答"},
#         {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},
#         {"role": "user", "content":"输出1-10的数字，使用Python代码"}
#     ]