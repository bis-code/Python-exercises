# helper added to show the results for each question
import datetime
from abc import abstractmethod


def printElementsInList(list):
    text = "[ "
    for element in list:
        text += str(element) + ", "
    return text + "]"


# Python - Multi-paradigm programming in Python
# Question 7a
# Write a Python program such that it uses imperative way to compute the sum of the list
def sumList(list):
    sum = 0
    for num in list:
        sum += num
    return sum


numList = [1, 2, 3, 4, 5]
sum = sumList(numList)
print("Result from question 7A -> " + str(sum))  # Result is 15
print("")

# Question 7b
# Using the imperative way of programming, check for even numbers given a user input:
# Write a program, which repeatedly prompts the user for an integer.
# If the integer is even, print the integer. If the integer is odd, don't print anything.
# Print "Bye for now!" and Exit the program if the user enters the integer 123

print("Question 7B")


def checkEvenNumberOnPrompting():
    isProgramRunning = True
    while isProgramRunning:
        number = int(input("(!) Prompting '123' you will exit the program\n"
                           "Prompt a number to check if it is even: "))
        if number == 123:
            print("Bye for now!")
            isProgramRunning = False
        else:
            if number % 2 == 0:
                print("Number is even " + str(number))


# checkEvenNumberOnPrompting()
print("")

print("Question 8A")

data = [1, 2, 3, 4, 5]


def adds10ToEachElementInList(listNumbers):
    return list(map(lambda n: n + 10, listNumbers))


newDataWith10Added = adds10ToEachElementInList(data)

print("Result after adding 10 -> " + printElementsInList(newDataWith10Added)) # Result after adding 10 ->  11 12 13 14 15
print("")

print("Question 8B")


def filterEvenNumbers(listNumbers):
    return list(filter(lambda n: n % 2 == 0, listNumbers))


naturalNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evenNaturalNumbers = filterEvenNumbers(naturalNumbers)
print("Result after filtering even numbers -> " + printElementsInList(evenNaturalNumbers)) # Result after filtering even numbers ->  0 2 4 6 8
print("")

print("Question 9")
print("Question 9A")
# Using the imperative coding style, implement a function groupList that given a list (list) and a group
# length (glength), returns a list of lists with length glength
# Example: testList = [1,2,3,4,5,6]
# groupList(list,2) gives [[1,2],[3,4],[5,6]] while groupList(list,3) gives [[1,2,3],[4,5,6]]
def groupList(list, glength):
    result = []
    current_group = []

    for item in list:
        current_group.append(item)

        if len(current_group) == glength:
            result.append(current_group)
            current_group = []

    if current_group:
        result.append(current_group)

    return result

testList = [1,2,3,4,5,6]
resultedList = groupList(testList, 2)
print("Resulted list with glength 2 -> " + printElementsInList(resultedList))

resultedList = groupList(testList, 3)
print("Resulted list with glength 3 -> " + printElementsInList(resultedList))
print("")

print("Question 9B")

dkCities = ["Copenhagen", "Aarhus", "Aalborg", "Horsens", "Odense"]
startingLetters = 'Aa'
def filterCitiesThatStartsWithAa(cities):
    return list(filter(lambda city: city.startswith(startingLetters), cities))

filteredCities = filterCitiesThatStartsWithAa(dkCities)
print("Resulted list of cities after filtering -> " + printElementsInList(filteredCities))
print("")

print("Question 10")
print("Question 10A")

class CourseNote:
    def __init__(self, jotting, creationDate, keyWords):
        self.jotting = jotting
        self.creationDate = creationDate
        self.keyWords = keyWords

    def isAmatch(self, searchFilter) -> bool:
        return self.keyWords == searchFilter # filter on what?

class Notebook:
    def __init__(self, courseNotes):
        self.courseNotes = courseNotes

    def search(self, filter_str):
        return list(filter(lambda courseNote: courseNote.isAmatch(str(filter_str)), self.courseNotes))

    def addNotes(self, jotting, keywords):
        courseNote = CourseNote(jotting, datetime.date, keywords)
        self.courseNotes.append(courseNote)


# create list of courseNotes
courseNote1 = CourseNote("PCL first session is the best", datetime.date, "PCL")
courseNote2 = CourseNote("Python the best", datetime.date, "Python")
listCourseNotes = [courseNote1, courseNote2]

# create notebook
notebook = Notebook(courseNotes = listCourseNotes)

print("Course notes before adding -> " +
      printElementsInList(list(
          map(lambda courseNote: courseNote.jotting, notebook.courseNotes))
      ))
# add new course note
notebook.addNotes("The best course ever", "PCL")
print("Course notes after adding -> " +
      printElementsInList(list(
          map(lambda courseNote: courseNote.jotting, notebook.courseNotes))
      ))


print("Course notes filtered on 'PCL' value" +
      printElementsInList(list(
        map(lambda courseNote: courseNote.jotting, notebook.search("PCL"))
      )))
print("")

print("Question 10B")

class SingerSongwriter:

    @abstractmethod
    def strum(self):
        print("Strum")

    @abstractmethod
    def actSensitive(self):
        pass
class Singer(SingerSongwriter):

    def __init__(self):
        super().__init__()
    def sing(self):
        print("Singer sings")

    def strum(self):
        print("Singer strums")

    def actSensitive(self):
        print("Singer acts sensitive")

class SongWriter(SingerSongwriter):

    def __init__(self):
        super().__init__()
    def compose(self):
        print("Songwriter composes")

    def strum(self):
        print("Songwriter strums")

    def actSensitive(self):
        print("SongWriter acts sensitive")

songWriter = SongWriter()
singer = Singer()

songWriter.actSensitive()
songWriter.strum()
songWriter.compose()

singer.actSensitive()
singer.strum()
singer.sing()










