class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Pkmer", 18)

# 这两种写法等价
print(p.__dict__)  # {'name': 'Pkmer', 'age': 18}
print(vars(p))     # {'name': 'Pkmer', 'age': 18} 推荐用法
