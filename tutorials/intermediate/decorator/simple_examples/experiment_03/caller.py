from decorators import do_twice

# Reuse decorator
@do_twice
def say_hi():
    print("Hi!")

say_hi()