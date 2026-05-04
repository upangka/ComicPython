from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen2.5-0.5B-Instruct')
tokenizer.save_pretrained('./qwen-tokenizer')
print('下载完成，文件保存在 ./qwen-tokenizer 目录下')