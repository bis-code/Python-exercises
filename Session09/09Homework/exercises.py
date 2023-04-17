# Exercise 9.1 - Classes and Objects
from abc import abstractmethod


class MyRecipe:
    def __init__(self, calories, cookingTime):
        self.calories = calories
        self.cookingTime = cookingTime

    def getCalories(self):
        return self.calories

    def getCookingTime(self):
        return self.cookingTime

    def cook(self):
        print(f"Cooking my recipe with {self.calories} calories. Ready in about {self.cookingTime}.")


# Exercise 9.2 - Inheritance

class Friend:
    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return f"Phone {self.phone}"


class Contact(Friend):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        super().__init__(phone)

    def __str__(self):
        return f"Name {self.name}, email contact: {self.email}, {self.phone}"


class AddressHolder(Friend):
    def __init__(self, street, post_code, city, phone):
        self.street = street
        self.post_code = post_code
        self.city = city
        super().__init__(phone)

    def __str__(self):
        return f"{self.phone}, Street {self.street}, post code: {self.post_code}, {self.city}"


#Exercise 9.3 - Polymorphism
class Fish:
    def eat(self):
        print("Fish says: 'I am eating'")

    def swim(self):
        print("Fish is swimming")

class Shark(Fish):
    def eat(self):
        print("Shark says: 'I am eating'")

    def swim(self):
        print("Shark is swimming")


class Dolphin(Fish):
    def eat(self):
        print("Dolphin says: 'I am eating'")

    def swim(self):
        print("Dolphin is swimming")

#Exercise 9.4 - Extra
class CaffeineDrink:
    def __init__(self, description, size):
        self.description = description
        self.size = size

    def drink_info(self):
        return f"{self.description} with size of {self.size}"
    @abstractmethod
    def get_price(self):
        pass

class Coffee(CaffeineDrink):
    def __init__(self, quantity, tax_rate, description, size):
        super().__init__(description, size)
        self.quantity = quantity
        self.tax_rate = tax_rate

    def get_price(self):
        return 5

class Tea(CaffeineDrink):
    def __init__(self, quantity, description, size):
        super().__init__(description, size)
        self.quantity = quantity

    def get_price(self):
        return 3
