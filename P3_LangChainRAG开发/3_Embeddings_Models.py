# 阿里云千问模型访问方式
from langchain_community.embeddings import DashScopeEmbeddings
# 默认使用模型是text-embedding-v1
embed = DashScopeEmbeddings()

#测试
print(embed.embed_query("我喜欢你"))
print(embed.embed_documents(['我喜欢你', '我爱你', '晚上吃啥']))