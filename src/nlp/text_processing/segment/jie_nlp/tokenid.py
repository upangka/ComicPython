import jieba

text = "大家好，我爱深圳图书馆"

def tokenize(text):
    return jieba.lcut(text)

tokens = set(tokenize(text))
vacab = {token: i for i, token in enumerate(tokens)}
print(vacab)
"""
{'好': 0, '我': 1, '，': 2, '图书馆': 3, '大家': 4, '深圳': 5, '爱': 6}
"""
