"""book 模块

表示图书馆中的一本书。
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    """书籍类"""
    title: str
    """书名"""

    author: str
    """作者"""

    isbn: str = ""
    """ISBN 编号（可选）"""
