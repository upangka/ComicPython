from collections.abc import Iterable, Iterator

class A:
    def __iter__(self):
        return self
    def __next__(self):
        ...
a = A()

print(isinstance(a, Iterable))  # True
print(isinstance(a, Iterator))  # True
