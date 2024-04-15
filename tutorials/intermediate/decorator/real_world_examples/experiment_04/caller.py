from decorators import set_unit
import math

@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height

print(volume(3, 5))
print(volume.unit)