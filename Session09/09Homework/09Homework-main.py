import exercises
if __name__ == '__main__':
    # exercise 9.1 - classes and objects
    myRecipe1 = exercises.MyRecipe(500, 30)
    myRecipe2 = exercises.MyRecipe(300, 20)
    myRecipe3 = exercises.MyRecipe(100, 10)
    myRecipe4 = exercises.MyRecipe(200, 10)
    myRecipe5 = exercises.MyRecipe(500, 10)
    listOfRecipes = [myRecipe1, myRecipe2, myRecipe3, myRecipe4, myRecipe5]
    for recipe in listOfRecipes:
        recipe.cook()

    # exercise 9.2 - Inheritance
    friend = exercises.Friend("50235931")
    addressHolder = exercises.AddressHolder("Kamtjatka", "8700", "Horsens", friend)
    contact = exercises.Contact("Ioan-Sorin Baicoianu", "zerofrags000@gmail.com", friend)
    print(addressHolder.__str__())
    print(contact.__str__())

    # exercise 9.3 - Polymorphism
    fish = exercises.Fish()
    shark = exercises.Shark()
    dolphin = exercises.Dolphin()
    fish.eat()
    shark.eat()
    dolphin.eat()
    fish.swim()
    shark.swim()
    dolphin.swim()

    # exercise 9.4 - Extra
    caffeineDrink = exercises.CaffeineDrink("Caffeine is good", 10)
    # TODO have to ask proffesor for this because i don't know if it's instantiate correctly
    coffee = exercises.Coffee(10, 2, caffeineDrink.description, caffeineDrink.size)
    tea = exercises.Tea(5, caffeineDrink.description, caffeineDrink.size)
    print(coffee.get_price())
    print(tea.get_price())