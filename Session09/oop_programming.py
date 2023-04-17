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

print("\n \nUsing class method")
# using @classmethod
class PersonClassMethod:
    TITLES = ("Software Engr", "Systems analyst", "Business Analyst")
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self): # instance method
        return "%s %s" % (self.firstname, self.lastname)

    # The @classmethod decorator is used to decorate an ordinary method
    # sometimes we write classes to group related constants together
    # with functions which act on them and we may never instantiate inside the class object
    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        return [t for t in cls.TITLES if t.startswith(startswith)]
pcm = PersonClassMethod("Ion", "Rokas")
print(pcm.fullname())
print(PersonClassMethod.fullname(pcm))
print(pcm.allowed_titles_starting_with("S"))
print(PersonClassMethod.allowed_titles_starting_with("S"))

print("\n \nUsing static method")
# using @staticmethod
class PersonStaticMethod:
    TITLES = ("Software Engr", "Systems analyst", "Business Analyst")
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self): # instance method
        return "%s %s" % (self.firstname, self.lastname)

    # a static method doesn't have the calling object passed into it as the parameter
    # it doesn't have access to the rest of the class of instance
    # are most commonly used from class objects, like class methods
    @staticmethod
    def allowed_titles_ending_with(endswith):  # class method
        return [t for t in PersonStaticMethod.TITLES if t.endswith(endswith)]
psm = PersonStaticMethod("Lucian", "Abdul")
print(psm.fullname())
print(PersonStaticMethod.fullname(psm))
print(psm.allowed_titles_ending_with("t"))
print(PersonStaticMethod.allowed_titles_ending_with("t"))

print("\n \nUsing property and setter")
# using @property
class Car(object):
    def __init__(self):
        self._speed = 50

    @property
    def speed(self):
        print("The Speed is ", self._speed)
        return self._speed
    @speed.setter
    def speed(self, newSpeed):
        print("Setting to ", newSpeed)
        self._speed = newSpeed
mikkels_car = Car()
mikkels_car._speed = 120
m_speed = mikkels_car.speed

print("\n \nUsing Inheritance")
class PersonInheritance:
    def speak(self):
        print("I can speak many languages, including PYTHON :-)")

class Student(PersonInheritance):
    #redefine speak method from person object
    def speak(self):
        print("I can speak all languages")
    def watch_movie(self):
        print("I like to watch marvel movies")

class Staff(PersonInheritance):
    def watch_movie(self):
        print("I like to watch science fiction")

student = Student()
student.speak()
student.watch_movie()
staff = Staff()
staff.speak()
staff.watch_movie()


