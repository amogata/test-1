#Class
class Vehicle:

    def __init__(self, typeV, horespower, carId):
        #attributes
        self.typeV = typeV
        self.horespower = horespower
        self.carId = carId


    def getHorsepower(self):
        return self.horespower

    def getType(self):
        return self.typeV

    def getCarID(self):
        return self.carId

class CarCollection:

    def __init__(self):
        #attributes
        self.collection = []

    def addToCollection(self, carType, horespower):
        carID = len(self.collection)
        newVehicle = Vehicle(carType, horespower, carID)
        self.collection.append(newVehicle)
        return self.collection

    def printCollection(self):
        print("My Carzzz: ")
        for vehicle in self.collection:
            #print("\tCar {}: {}".format(vehicle.getType(), vehicle.getHorsepower(), vehicle.getCarID))
            print((str(vehicle.getType()) + " " + str(vehicle.getHorsepower()) + " "
            + str(vehicle.getCarID())))


#Object/Instance
myCarCollection = CarCollection()

myCarCollection.addToCollection("Honda", "1500 cc")

myCarCollection.addToCollection("BMW", "2500 cc")

myCarCollection.printCollection()



# car = Vehicle(
#     "Car",
#     "1500 cc"
# )
#
# truck = Vehicle(
#     "Truck",
#     "2500 cc"
# # )
#
# print(car.typeV)
# print(car.getHorespower)
