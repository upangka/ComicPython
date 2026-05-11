zen_of_python = """
The Zen of Python, by Tim Peters
Python 之禅，作者 Tim Peters

Beautiful is better than ugly.
优美胜于丑陋

Explicit is better than implicit.
明了胜于晦涩

Simple is better than complex.
简单胜于复杂

Complex is better than complicated.
复杂胜于凌乱

Flat is better than nested.
扁平胜于嵌套

Sparse is better than dense.
稀疏胜于密集

Readability counts.
可读性很重要

Special cases aren't special enough to break the rules.
特例不足以打破规则

Although practicality beats purity.
尽管实用性胜过纯粹性

Errors should never pass silently.
错误不应被悄无声息地放过

Unless explicitly silenced.
除非明确地保持沉默

In the face of ambiguity, refuse the temptation to guess.
面对歧义，拒绝猜测的诱惑

There should be one-- and preferably only one --obvious way to do it.
应该有一种——最好只有一种——显而易见的方法去完成它

Although that way may not be obvious at first unless you're Dutch.
尽管这种方式一开始可能并不明显，除非你是荷兰人

Now is better than never.
现在做胜过永远不做

Although never is often better than *right* now.
尽管“永远不做”往往比“立刻做”更好

If the implementation is hard to explain, it's a bad idea.
如果实现很难解释，那它是个坏主意

If the implementation is easy to explain, it may be a good idea.
如果实现很容易解释，那它可能是个好主意

Namespaces are one honking great idea -- let's do more of those!
命名空间是一个非常棒的主意——让我们多使用它吧
"""

with open("zen_of_python.txt", mode="w",encoding="utf-8") as f:
    f.write(zen_of_python.strip())
    print("success :)")
