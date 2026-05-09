from abc import ABC, abstractmethod
from typing import Type


class Pet(ABC):
    """宠物的抽象基类
  ┌─────────────────────────────────────────────┐
  │  抽象产品（AbstractProduct）                  │
  │  定义所有产品必须遵守的接口                     │
  └─────────────────────────────────────────────┘
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self):
        ...

    @abstractmethod
    def __str__(self):
        ...


class Dog(Pet):
    """狗
      ┌─────────────────────────────────────────────┐
      │  具体产品（ConcreteProduct）                  │
      │  同时，Dog 类本身也是——                       │
      │  具体工厂（ConcreteFactory）                  │
      │  "调用 Dog(name)" 就是工厂的创建方法           │
      └─────────────────────────────────────────────┘
    """

    def speak(self):
        print(f"{self.name}汪汪汪")

    def __str__(self):
        return f"Dog<{self.name}>"


class Cat(Pet):
    """猫
      ┌─────────────────────────────────────────────┐
      │  具体产品（ConcreteProduct）                  │
      │  同时，Cat 类本身也是——                       │
      │  具体工厂（ConcreteFactory）                  │
      │  "调用 Cat(name)" 就是工厂的创建方法           │
      └─────────────────────────────────────────────┘
    """
    def speak(self):
        print(f"{self.name}喵喵喵")

    def __str__(self):
        return f"Cat<{self.name}>"


class PetShop:
    """宠物店"""
    def __init__(self, animal_factory: Type[Pet]):
        """
      ┌─────────────────────────────────────────────────┐
      │  animal_factory 的类型注解 Type[Pet]             │
      │  这就是"抽象工厂（AbstractFactory）"的角色         │
      │  它说：我需要一个可调用对象，调用后返回 Pet 实例      │
      │  任何满足这个签名的类/函数都可以注入                 │
      └─────────────────────────────────────────────────┘
        """
        self.pet_factory  = animal_factory

    def buy_pet(self, name: str):
        pet = self.pet_factory(name)
        print(f"这是可爱的{pet}")
        return pet

if __name__ == '__main__':
    animal_factories = [Dog, Cat]
    import random
    animal_factory = random.choice(animal_factories)
    pet = PetShop(animal_factory).buy_pet("小橙子")
    pet.speak()