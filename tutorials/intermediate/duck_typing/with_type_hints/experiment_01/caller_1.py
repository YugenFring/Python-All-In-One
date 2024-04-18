# The type hint for `grades` arg is limited to
# `list` object and collides with duck tying.
def mean(grades: list) -> float:
    return sum(grades) / len(grades)


print(mean([4, 3, 3, 4, 5]))

print(mean((4, 3, 3, 4, 5)))