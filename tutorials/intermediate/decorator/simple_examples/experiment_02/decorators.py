# Put simply, a decorator wrpas a function,
# modifying its behavior.
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Syntactic sugar
# The decorated func will be used as the first
# argument to the decorator func.
@decorator
def say_hi():
    print("Hi!")