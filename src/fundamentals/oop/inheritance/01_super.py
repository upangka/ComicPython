


class Parent:
    def __init__(self,name):
        print("Parent")
        self.name = name

    def hello(self):
        print("Parent: hello")


class Child(Parent):
    def __init__(self,name):
        print("Child")
        super().__init__(name) # 不像Java需要放在第一行，需要显示调用父类的__init__方法

    def hello(self):  # 重写父类方法
        super().hello() # 调用父类方法
        print(f"Child: hello {self.name}") # 能够访问父类特征(attribute)


Child("Pkmer").hello()

"""输出
Child
Parent
Parent: hello
Child: hello Pkmer
"""
