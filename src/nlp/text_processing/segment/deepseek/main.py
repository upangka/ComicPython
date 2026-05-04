from tokenizers import Tokenizer
tokenize = Tokenizer.from_file("tokenizer.json")

encoding = tokenize.encode("大家好，我爱深圳图书馆")
print(f"token count {len(encoding)}")
print([tokenize.decode([token_id]) for token_id in encoding.ids])
print(encoding.ids)

"""
token count 5
['大家好', '，', '我爱', '深圳', '图书馆']
[61256, 303, 60147, 16718, 20978]
"""

