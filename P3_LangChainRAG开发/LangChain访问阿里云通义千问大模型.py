# langchain_community

from langchain_community.llms.tongyi import Tongyi

#这里不是qwen3-max，因为他是聊天模型，而qwen-max是大语言模型
model = Tongyi(model="qwen-max")

#调用invoke向模型提问
res = model.invoke(input="你是谁啊？你能做什么？")

print(res)