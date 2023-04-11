# Implicit class
class MyFirstClass:
    pass


c1 = MyFirstClass()


class Person:
    # init variables' class
    def __init__(self, name):
        self.name = name
        print(self.name)

    # add a print_name() method
    def print_name(self):
        print(self.name)


p1 = Person("Ionut")
print(p1.name)
p1.print_name()
