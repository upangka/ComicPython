import os

import jieba
from tokenizers import Tokenizer


def load_bert_tokenizer(path: str) -> Tokenizer:
    """从 tokenizer.json 加载 BERT 分词器"""
    return Tokenizer.from_file(os.path.join(path, "tokenizer.json"))


def tokenize_with_jieba(text: str) -> list[str]:
    """jieba 精确模式分词"""
    return jieba.lcut(text)


def tokenize_with_bert(text: str, tokenizer: Tokenizer) -> tuple[list[str], list[int]]:
    """BERT WordPiece 分词，返回可读的 token 列表和对应的 ID 列表"""
    encoded = tokenizer.encode(text)
    print(encoded)
    return encoded.tokens, encoded.ids


def compare(text: str, bert_tokenizer: Tokenizer) -> None:
    """对比 jieba / BERT 分词结果"""
    jieba_result = tokenize_with_jieba(text)
    bert_tokens, bert_ids = tokenize_with_bert(text, bert_tokenizer)

    print(f"原文：{text}")
    print(f"字符数：{len(text)}\n")

    # jieba
    print(f"{'jieba (精确模式)':<25} 词数: {len(jieba_result)}")
    print("  " + " | ".join(jieba_result))

    # BERT
    print(f"\n{'BERT':<25} token数: {len(bert_tokens)}")
    print("  Tokens: " + " | ".join(bert_tokens))
    print(f"  IDs:    {bert_ids}")

    # 差异高亮
    print("\n" + "─" * 65)
    highlight_diff(jieba_result, bert_tokens)


def highlight_diff(
        jieba_tokens: list[str],
        bert_tokens: list[str],
) -> None:
    """高亮两方差异"""
    # 去掉 BERT 的特殊标记
    bert_clean = [t for t in bert_tokens if t not in ("[CLS]", "[SEP]")]

    # BERT 的 [UNK] 问题
    unk_count = bert_tokens.count("[UNK]")
    if unk_count > 0:
        print(f"⚠️  BERT 出现 {unk_count} 个 [UNK]（未知词），信息丢失！")

    # 粒度对比
    print(f"粒度对比：jieba={len(jieba_tokens)} 词 | BERT={len(bert_clean)} token")


def show_vocab_sample(tokenizer: Tokenizer, start: int = 100, n: int = 10) -> None:
    """查看 BERT 词表中实际词汇区域（跳过特殊标记区）"""
    vocab = tokenizer.get_vocab()
    sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])
    print(f"\nBERT 词表第 {start}~{start + n - 1} 个 token（实际词汇区）：")
    for token, idx in sorted_vocab[start: start + n]:
        print(f"  {idx:>5} → {token}")


if __name__ == "__main__":
    # 加载 BERT 多语言分词器
    bert_tokenizer = load_bert_tokenizer("bert-multilingual-tokenizer")

    # 瞄一眼 BERT 词表
    show_vocab_sample(bert_tokenizer, start=100, n=10)

    # 对比测试句
    print("\n" + "=" * 65)
    print("分词对比：jieba vs BERT")
    print("=" * 65)

    texts = [
        "深圳图书馆北馆在龙华区,五一我在学习Java和Python",
        "周六下午去深圳湾公园散步",
    ]

    for text in texts:
        compare(text, bert_tokenizer)
        print()
