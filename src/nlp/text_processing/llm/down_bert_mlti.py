from transformers import AutoTokenizer

# 下载多语言模型的分词器，这是 Google 官方推荐的版本[citation:6]
tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')

# 保存到新文件夹，方便和之前的中文模型做对比
tokenizer.save_pretrained('./bert-multilingual-tokenizer')
print('多语言分词器已保存到 ./bert-multilingual-tokenizer')