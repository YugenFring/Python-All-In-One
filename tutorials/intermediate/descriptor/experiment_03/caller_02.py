# lookup chain
class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car('Red')

print(my_car.color)
print(my_car.number_of_weels)
print(my_car.can_fly)


# First, you’ll get the result returned from the __get__ method of the data descriptor
# named after the attribute you’re looking for.

# If that fails, then you’ll get the value of your object’s __dict__ for the key named
# after the attribute you’re looking for.

# If that fails, then you’ll get the result returned from the __get__ method of the
# non-data descriptor named after the attribute you’re looking for.

# If that fails, then you’ll get the value of your object type’s __dict__ for the key
# named after the attribute you’re looking for.

# If that fails, then you’ll get the value of your object parent type’s __dict__ for
# the key named after the attribute you’re looking for.

# If that fails, then the previous step is repeated for all the parent’s types in the
# method resolution order of your object.

# If everything else has failed, then you’ll get an AttributeError exception.