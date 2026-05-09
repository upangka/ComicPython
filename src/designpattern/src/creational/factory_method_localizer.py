from typing import Protocol, Type


class Localizer(Protocol):
    """协议类"""

    def localize(self, msg: str) -> str:
        ...

class ChineseLocalizer:
    def localize(self, msg: str) -> str:
        return msg

class EnglishLocalizer:
    def __init__(self):
        self.translation_dict = {
            "深圳图书馆北馆": "Shenzhen Library North Branch",
            "Python编程入门与实践": "Introduction to Python Programming and Practice",
            "设计模式": "Design Patterns"
        }

    def localize(self, msg: str) -> str:
        """将中文翻译成英文，无法翻译则返回原文"""
        return self.translation_dict.get(msg, msg)

def get_localizer(language: str) -> Localizer:
    """工厂方法"""
    localizers: dict[str, Type[Localizer]] = {
        "zh": ChineseLocalizer,
        "en": EnglishLocalizer
    }
    return localizers.get(language, ChineseLocalizer)()

if __name__ == '__main__':
    en, cn = get_localizer("en"), get_localizer("zh")
    for msg in ["Pkmer", "在", "深圳图书馆北馆", "学习", "Python编程入门与实践", "设计模式"]:
        print(f"{cn.localize(msg)} -> {en.localize(msg)}")
