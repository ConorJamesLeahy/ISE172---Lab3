# OOP

class Car:
    def __init__(self, model):
        self.distance = 0.0
        self.model = model

    def __str__ (self):
        return "Car: %s, drove, %f"%(self.model, self.distance)

    def logDistance(self, newDistance):
        self.distance += newDistance


car = Car("Toyota Corolla")

car.logDistance(12.6)


print(car)

class Truck(Car):

    def load(self, newload):
        pass
truck = Truck("Ford 150")

print(truck)
