
class Father:
    def __init__(self):
        print("Father")
        super().__init__()

class Mother:
    def __init__(self):
        print("Mother")
        super().__init__()

class Son(Father,Mother):
    pass

class Daughter(Mother,Father):
    pass

if __name__ == '__main__':
    Son() # Father Mother
    Daughter() # Mother Father
    Son.mro()