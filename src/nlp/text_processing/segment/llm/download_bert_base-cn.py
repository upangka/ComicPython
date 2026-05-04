from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
tokenizer.save_pretrained('./bert-chinese-tokenizer')
print('下载完成，文件保存在 ./bert-chinese-tokenizer 目录下')