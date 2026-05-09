from abc import ABC,abstractmethod
class Localizer(ABC):
    """
      ┌─────────────────────────────────────────────┐
      │  抽象基类                                    │
      │  定义所有子类必须遵守的接口                     │
      └─────────────────────────────────────────────┘
    """
    @abstractmethod
    def localize(self, msg: str) -> str:
        ...


class ChineseLocalizer(Localizer):
    def localize(self, msg: str) -> str:
        return msg


class EnglishLocalizer(Localizer):
    def localize(self, msg: str) -> str:
        ...

# 任何有 localize 方法的对象都可以传进来
def use_localizer(l: Localizer) -> str:
    return l.localize("hello")


use_localizer(ChineseLocalizer())
use_localizer(EnglishLocalizer())



