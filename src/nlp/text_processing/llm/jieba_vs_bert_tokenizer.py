import os
from tokenizers import Tokenizer
import jieba
import tiktoken


def load_bert_tokenizer(path: str) -> Tokenizer:
    """从 tokenizer.json 加载 BERT 分词器"""
    return Tokenizer.from_file(os.path.join(path, "tokenizer.json"))


def tokenize_with_jieba(text: str) -> list[str]:
    """jieba 精确模式分词"""
    return jieba.lcut(text)


def tokenize_with_bert(text: str, tokenizer: Tokenizer) -> tuple[list[str], list[int]]:
    """BERT WordPiece 分词，返回可读的 token 列表和对应的 ID 列表"""
    encoded = tokenizer.encode(text)
    return encoded.tokens, encoded.ids


def tokenize_with_gpt(text: str, model: str = "gpt-4o") -> tuple[list[str], list[int]]:
    """
    使用 tiktoken 为 GPT 模型分词。
    返回 (token字符串列表, token_id列表)
    """
    enc = tiktoken.encoding_for_model(model)
    token_ids = enc.encode(text)
    # 解码每个 token 为可读字符串
    token_strs = [enc.decode([t]) for t in token_ids]
    return token_strs, token_ids


def compare(text: str, bert_tokenizer: Tokenizer) -> None:
    """三方并排对比 jieba / BERT / GPT 分词结果"""
    jieba_result = tokenize_with_jieba(text)
    bert_tokens, bert_ids = tokenize_with_bert(text, bert_tokenizer)
    gpt_tokens, gpt_ids = tokenize_with_gpt(text)

    print(f"原文：{text}")
    print(f"字符数：{len(text)}\n")

    # jieba
    print(f"{'jieba (精确模式)':<25} 词数: {len(jieba_result)}")
    print("  " + " | ".join(jieba_result))

    # BERT
    print(f"\n{'BERT (WordPiece)':<25} token数: {len(bert_tokens)}")
    print("  Tokens: " + " | ".join(bert_tokens))
    print(f"  IDs:    {bert_ids}")

    # GPT
    print(f"\n{'GPT-4o (BPE)':<25} token数: {len(gpt_tokens)}")
    print("  Tokens: " + " | ".join(gpt_tokens))
    print(f"  IDs:    {gpt_ids}")

    # 差异高亮
    print("\n" + "─" * 65)
    highlight_diff(jieba_result, bert_tokens, gpt_tokens)


def highlight_diff(
    jieba_tokens: list[str],
    bert_tokens: list[str],
    gpt_tokens: list[str],
) -> None:
    """高亮三方差异"""
    # 去掉 BERT 的特殊标记
    bert_clean = [t for t in bert_tokens if t not in ("[CLS]", "[SEP]")]

    # BERT 的 [UNK] 问题
    unk_count = bert_tokens.count("[UNK]")
    if unk_count > 0:
        print(f"⚠️  BERT 出现 {unk_count} 个 [UNK]（未知词），信息丢失！")

    # 粒度对比
    print(f"粒度对比：jieba={len(jieba_tokens)} 词 | BERT={len(bert_clean)} token | GPT={len(gpt_tokens)} token")

    # 列出关键差异词
    jieba_set = set(jieba_tokens)
    gpt_set = set(gpt_tokens)
    only_jieba = jieba_set - gpt_set
    only_gpt = gpt_set - jieba_set
    if only_jieba:
        print(f"仅 jieba 有：{only_jieba}")
    if only_gpt:
        print(f"仅 GPT 有：{only_gpt}")


def show_vocab_sample(tokenizer: Tokenizer, start: int = 100, n: int = 10) -> None:
    """查看 BERT 词表中实际词汇区域（跳过特殊标记区）"""
    vocab = tokenizer.get_vocab()
    sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])
    print(f"\nBERT 词表第 {start}~{start + n - 1} 个 token（实际词汇区）：")
    for token, idx in sorted_vocab[start : start + n]:
        print(f"  {idx:>5} → {token}")


def show_gpt_vocab_sample(model: str = "gpt-4o", n: int = 10) -> None:
    """查看 GPT 词表的前 n 个 token"""
    enc = tiktoken.encoding_for_model(model)
    print(f"\nGPT 词表前 {n} 个 token：")
    for i in range(n):
        token_str = enc.decode([i])
        print(f"  {i:>5} → {token_str!r}")


if __name__ == "__main__":
    # 加载 BERT 多语言分词器
    bert_tokenizer = load_bert_tokenizer("./bert-multilingual-tokenizer")

    # 瞄一眼两个词表
    show_vocab_sample(bert_tokenizer, start=100, n=10)
    show_gpt_vocab_sample(n=10)

    # 深圳主题测试句
    print("\n" + "=" * 65)
    print("三方分词对比：jieba vs BERT vs GPT")
    print("=" * 65)

    texts = [
        "深圳图书馆北馆在龙华区,五一我在学习Java和Python",
        "周六下午去深圳湾公园散步",
    ]

    for text in texts:
        compare(text, bert_tokenizer)
        print()