"""
python → json：json.dumps()
JSON → python：json.loads()
"""

import json

d = {
    "name": "tyros",
    "age": 18,
    "gender": "女"
}
print(str(d))
# 将Python里面的字典转化为json格式（引号标准就是双引号）
s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
    {
    "name": "tyros",
    "age": 18,
    "gender": "女"
    },
    {
    "name": "ty",
    "age": 18,
    "gender": "男"
    },
    {
    "name": "tos",
    "age": 15,
    "gender": "女"
    },
]

print(json.dumps(l, ensure_ascii=False))