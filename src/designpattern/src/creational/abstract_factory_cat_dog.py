from abc import ABC, abstractmethod
from typing import Type


class Pet(ABC):
    """宠物的抽象基类"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speek(self):
        ...

    @abstractmethod
    def __str__(self):
        ...


class Dog(Pet):
    """狗"""

    def speek(self):
        print(f"{self.name}汪汪汪")

    def __str__(self):
        return f"Dog<{self.name}>"


class Cat(Pet):
    """猫"""

    def speek(self):
        print(f"{self.name}喵喵喵")

    def __str__(self):
        return f"Cat<{self.name}>"


class PetShop:
    """宠物店"""
    def __init__(self, animal_factory: Type[Pet]):
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
    pet.speek()