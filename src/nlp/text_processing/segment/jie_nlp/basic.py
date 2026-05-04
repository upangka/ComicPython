import jieba

text = "大家好，我爱深圳图书馆"
words = jieba.lcut(text)
print(len(words))
print(" / ".join(words))