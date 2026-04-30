
class CreateCounter:
    count = 0 # 类特性(class attribute)

    def __init__(self):
        CreateCounter.count += 1
        self.id = CreateCounter.count

    def __str__(self):
        return f"id: {self.id}"