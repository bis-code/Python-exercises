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


class Person2:
    # init variables' class
    def __init__(self, name):
        self.name = name
        print(self.name)

    # add a print_name() method
    def print_name(self):
        print(self.name)


p2 = Person2("Sorin")
print(p2)  # it tells us is an object - the usual toString() output before modifying it


# Form of a class / object for class
class ViaStudent:
    where = "VIA"

    def __init__(self):
        self.where = "VIA-Horsens"


print(ViaStudent.where) # output: VIA
print(ViaStudent().where) # output VIA-Horsens
