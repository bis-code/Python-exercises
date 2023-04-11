# Implicit class
class MyFirstClass:
    pass


class Person:
    # init variables' class
    def __init__(self, name):
        self.name = name
        print(self.name)
        pass


c1 = MyFirstClass()
p1 = Person("Ionut")
