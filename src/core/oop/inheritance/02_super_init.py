


class Parent:
    def __init__(self,name):
        print("Parent")
        self.name = name

    def hello(self):
        print(f"Parent: hello {self.name}")


class Child(Parent):
    """使用父类的__init__"""
    pass

Child("Pkmer").hello()

