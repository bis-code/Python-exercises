# Exercise 8.1 - Iteration
# Python provides for and while loop that enable us to repeat blocks
# of instructions several times. For example to write “Python is cool” 5 times:
print("This program prints a string 5 times")
for count in range(5):
    print("Python is cool")

# Exercise 8.1A
# Write a program that will print your full name and student number 10 times.
def printStudentNumberAndFullname10Times(studentNumber, fullName):
    for count in range(10):
        print(str(count + 1) + " " + studentNumber + " " + fullName)

printStudentNumberAndFullname10Times("304145", "Ioan-Sorin Baicoianu")


# Exercise 8.1B
# Write another program that will ask the user for a “wish” (eg. What do you wish for on your birthday)
# and the number of time they want that wish to be displayed.
# Then print the wish the number of times specified.
def wishForBirthday(yourWish, times):
    for count in range(times):
        print(str(count + 1) + " " + yourWish)


wishForBirthday("I want a bike for my birthday", 10)

# Exercise 8.2 - Sum
def sumList(lst):
    sum_list = 0
    for num in lst:
        sum_list += num
    return sum_list

print("Sum of the list: " + str(sumList([1, 2, 3, 4, 5])))

# Exercise 8.5 - Dictionaries
lst_key_pairs = [
    {'name': 'Bob Builder', 'specialle': 'IoT' },
    {'name': 'Dora Explorer', 'specialle': 'Interactive Media'},
    {'name': 'Paw Patrol', 'specialle': 'Data Engineering'}
]

def print_values_on_keys(key_pairs):
    print("")
    for dictionary in key_pairs:
        specialty = dictionary['specialle']
        print(specialty)

print("")
print("List before changing bob's value ")
print_values_on_keys(lst_key_pairs)
def change_value_on_key(keyName, keyValue, valueName, newValue, key_pairs):
    for dictionary in key_pairs:
        if(dictionary[keyName] == keyValue):
            dictionary[valueName] = newValue
            break

change_value_on_key('name','Bob Builder', 'specialle', 'Data Engineering', lst_key_pairs)

print("")
print("List after changing bob's specialle")
print_values_on_keys(lst_key_pairs)

# Print dora's specialisation
def print_value_on_key(keyName, keyValue, valueName, key_pairs):
    for dictionary in key_pairs:
        if dictionary[keyName] == keyValue:
            print("")
            print(dictionary[keyName] + "'s specialle -> " + dictionary[valueName])
            break

print_value_on_key('name','Dora Explorer', 'specialle', lst_key_pairs)









