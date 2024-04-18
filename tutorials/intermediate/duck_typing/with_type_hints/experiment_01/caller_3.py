# The type cooresponding to the `grades` arg
# must support iteration and the `len()` func,
# this abstract base class `Collection` defines
# both behavior.
from collections.abc import Collection

def mean(grades: Collection) -> float:
    return sum(grades) / len(grades)

print(mean([4, 3, 3, 4, 5]))

print(mean((4, 3, 3, 4, 5)))