from __future__ import annotations

from abc import ABC, abstractmethod


class BaseState(ABC):
    def __init__(self, radio: Radio):
        """每个子类都要持有上下文，通过上下文改变状态"""
        self.radio = radio
        self.pos = 0

    def scan(self):
        """扫描"""
        self.pos = (self.pos + 1) % len(self.stations)
        print(f"Radio 收听的是 {self.name} 频道: {self.stations[self.pos]}")

    @abstractmethod
    def toggle_amfm(self):
        """改变上下文状态的方法
        抽象方法强制子类实现,让子类状态转向下一个状态
        """
        ...


class AmState(BaseState):
    def __init__(self, radio: Radio):
        super().__init__(radio)
        self.name = "AM"
        self.stations = ["530", "540", "550"]

    def toggle_amfm(self):
        """转化为FM"""
        self.radio.state = RadioState.FM


class FmState(BaseState):
    def __init__(self, radio: Radio):
        super().__init__(radio)
        self.name = "FM"
        self.stations = ["90.1", "91.1", "92.1"]

    def toggle_amfm(self):
        """转化为AM"""
        self.radio.state = RadioState.AM


from enum import Enum


class RadioState(Enum):
    AM = "AM"
    FM = "FM"
    OTHER = "OTHER"


class Radio:
    def __init__(self):
        # 这里有点像策略，但是与策略相比，具体执行是在维护的这几个元素之间相互切换的
        self._states = {
            RadioState.AM: AmState(self),
            RadioState.FM: FmState(self)
        }
        self._state = self._states[RadioState.AM]

    def toggle_amfm(self):
        """切换AMFM
        让状态流转，具体怎么流转，让子类自己去处理
        """
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_type: RadioState):
        if state_type not in self._states:
            raise ValueError(f"{state_type} is not a valid state")
        self._state = self._states[state_type]


if __name__ == '__main__':
    radio = Radio()
    from typing import Callable

    actions: list[Callable] = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    [c() for c in actions]
