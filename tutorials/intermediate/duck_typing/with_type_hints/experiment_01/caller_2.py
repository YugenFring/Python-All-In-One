# Use union type expression, but it is cumbersome.
def mean(grades: list | tuple | set) -> float:
    return sum(grades) / len(grades)

print(mean([4, 3, 3, 4, 5]))

print(mean((4, 3, 3, 4, 5)))