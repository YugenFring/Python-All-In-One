from vehicles_abc import Vehicle

class Car(Vehicle):
    def start(self):
        print("The car is starting")

    def stop(self):
        print("The car is stopping")

    def drive(self):
        print("The car is driving")

class Truck(Vehicle):
    def start(self):
        print("The truck is starting")

    def stop(self):
        print("The truck is stopping")

    def drive(self):
        print("The truck is driving")