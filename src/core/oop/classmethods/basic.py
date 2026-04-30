class ExampleClass:
    def example_regular_method(self):
        """常规方法与对象绑定
        """
        print("常规方法")

    @classmethod
    def example_class_method(cls):
        """类方法与类绑定
        """
        print("类方法")
        # <class '__main__.ExampleClass'> <class 'type'> <class '__main__.ExampleClass'>
        print(f"{cls} {ExampleClass.__class__} {ExampleClass().__class__}")  # True


if __name__ == "__main__":
    # 类直接调用
    ExampleClass.example_class_method()

    # 对象也可以调用
    obj = ExampleClass()
    obj.example_class_method()

    # 通过__class__
    obj.__class__.example_class_method()
