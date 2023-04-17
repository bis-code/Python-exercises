class Vehicle:
    def __init__(self, numberOfTires):
        self.numberOfTires = numberOfTires

    def getNumberOfTires(self):
        return self.numberOfTires

    def setNumberOfTires(self, numberOfTires):
        self.numberOfTires = numberOfTires

    def getDescription(self):
        return "A description of a vehicle"

class Car(Vehicle):
    def __init__(self, plateNumber):
        super().__init__(4)
        self.plateNumber = plateNumber

    def setPlateNumber(self, plateNumber):
        self.plateNumber = plateNumber

    def getDescription(self):
        return "Vehicle with " + self.numberOfTires + " tires."


class Motorcycle(Vehicle):
    def __init__(self, plateNumber):
        super().__init__(2)
        self.plateNumber = plateNumber

    def getPlateNumber(self):
        return self.plateNumber

    def setPlateNumber(self, plateNumber):
        self.plateNumber = plateNumber

    def getDescription(self):
        return "Motorcycle with " + self.numberOfTires + " tires."


def print_car_info(car):
    print(car.getDescription())
    print("Tires: ", car.getNumberOfTires())

car = Car("DKCAR")
car.plateNumber = "DKCAR"
print_car_info(car)

motorcycle = Motorcycle("DKMOTOR")
motorcycle.plateNumber = "DKMOTOR"
motorcycle.getDescription()

