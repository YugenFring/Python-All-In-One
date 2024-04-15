from decorators import singleton

@singleton
class Cat:
    pass

first_one = Cat()
another_one = Cat()

print(id(first_one), id(another_one))
print(first_one is another_one)