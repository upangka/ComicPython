
class Person:
    def __init__(self):
        self._age = 18 # 幕后变量

    @property
    def age(self):
        print("准备获取年龄")
        return self._age

    # @age.setter @age.deleter