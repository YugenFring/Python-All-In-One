from decorators import do_twice

@do_twice
def say_hi():
    print("Hi")

# Get the name of the decorated func.
print(say_hi.__name__)