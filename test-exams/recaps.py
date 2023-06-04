# Exercise 9.1 - Classes and Objects
from abc import abstractmethod


class MyRecipe:
    def __init__(self, calories, cookTimeMinutes):
        self.calories = calories
        self.cookTimeMinutes = cookTimeMinutes

    def cook(self):
        print("This recipe is cooking in " + str(self.cookTimeMinutes) + " minutes, and it has " + str(
            self.calories) + " calories")


recipe1 = MyRecipe(2300, 30)
recipe2 = MyRecipe(200, 5)
recipe3 = MyRecipe(500, 10)
recipe4 = MyRecipe(1000, 20)
recipe5 = MyRecipe(3000, 120)
recipe1.cook()
recipe2.cook()
recipe3.cook()
recipe4.cook()
recipe5.cook()


# Exercise 9.2 - Inheritance
class Friend:
    def __init__(self, phone):
        self.phone = phone

    @abstractmethod
    def __str__(self):
        pass

class AddressHolder(Friend):
    def __init__(self, street, post_code, city, phone):
        self.street = street
        self.post_code = post_code
        self.city = city
        super().__init__(phone)


    def __str__(self):
        print(f"{self.phone}, Street {self.street}, post code: {self.post_code}, {self.city}")


class Contact(Friend):
    def __init__(self, name, email, phone):
        self.email = email
        self.name = name
        super().__init__(phone)

    def __str__(self):
        print(f"Name {self.name}, email contact: {self.email}, {self.phone}")


# Exercise 9.3 - Polymorphism
class Fish:

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def swim(self):
        pass

class Shark(Fish):
    def eat(self):
        print("Shark is eating")


    def swim(self):
        print("Shark is swimming")

class Dolphin(Fish):
    def eat(self):
        print("Dolphin is eating")

    def swim(self):
        print("Dolphin is swimming")

# Exercise 9.4 - Extra

class CaffeineDrink:
    def __init__(self, description, size):
        self.description = description
        self.size = size

    def drink_info(self):
        print(f"Description: {self.description}, with size {self.size}")

    @abstractmethod
    def get_price(self):
        pass

class Coffee(CaffeineDrink):
    def __init__(self, description, size, quantity, tax_rate):
        super().__init__(description, size)
        self.quantity = quantity
        self.tax_rate = tax_rate

    def get_price(self):
        print(f"Quantity: {self.quantity}, with tax rate of {self.tax_rate} and price 3")


class Tea(CaffeineDrink):
    def __init__(self, description, size, quantity):
        super().__init__(description, size)
        self.quantity = quantity

    def get_price(self):
        print(f"Quantity: {self.quantity}, with price 5")

