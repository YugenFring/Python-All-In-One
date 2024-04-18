from vehicles import Car, Truck

my_vehicles = [
    Car('Food', 'Mustang', 'Red'),
    Truck('Ford', 'F-150', 'Blue')
]

for vehicle in my_vehicles:
    vehicle.start()
    vehicle.drive()
    vehicle.stop()